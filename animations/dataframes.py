import os
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import json
import sys
import sys
from decimal import *
import pandas as pd

def df_from_consolidatedfile(N,consolidatedfile,improvedanglesfile,consolidate_tolerance=5):
	consolidated=readtxtfile(consolidatedfile)
	consolidatedlines=[c for c in consolidated.split('\n') if c!='']
	improvedangles=readtxtfile(improvedanglesfile)
	improvedangleslines=[c for c in improvedangles.split('\n') if c!='']
	
	#we are going to bundle these together out to "consolidated_tolerance" decimal places
	#and pick the angle with the minimum distance
	anglemap_prelim={}
	for angle_line in improvedangleslines:
		improved_angle_str,base_angle_str,sample_folding_idx_str, median_distance=angle_line.split('\t')
		rounded_angle=str(Decimal(improved_angle_str[:consolidate_tolerance]))
		this_distance=float(median_distance)
		record={
			'improved_angle_str':improved_angle_str,
			'base_angle_str':base_angle_str,
			'np_id':sample_folding_idx_str,
			'n':N,
			'median_distance':float(median_distance)
		}
		if rounded_angle in anglemap_prelim:
			anglemap_prelim[rounded_angle].append(record)
		else:
			anglemap_prelim[rounded_angle]=[record]
	anglemap={}
	for k in anglemap_prelim:
		records=anglemap_prelim[k]
		minimum_distance=1000
		minimum_distance_improved_angle_str=''
		for r in records:
			improved_angle_str=r['improved_angle_str']
			base_angle_str=r['base_angle_str']
			distance=r['median_distance']
			if distance<minimum_distance:
				minimum_distance=distance
				minimum_distance_improved_angle_str=improved_angle_str
				
		for r in records:
			base_angle_str=r['base_angle_str']
			anglemap[base_angle_str]=minimum_distance_improved_angle_str
	
	records=[]
	for line in consolidatedlines:
		angle_str,np_id_str,median_distance_str,close_neighborings_str=line.split('\t')
		if angle_str in anglemap:
			angle=float(anglemap[angle_str])
			np_id=int(np_id_str)
			close_neighborings_count=len(json.loads(close_neighborings_str))
			record={
				'n':N,
				'np_id':np_id,
				'angle':angle,
				'close_neighborings_count':close_neighborings_count
			}
			records.append(record)
		else:
			pass
			print("angle",angle_str,"not in map derived from angles_improved.txt")
	
	
	
	df=pd.DataFrame.from_records(records)
	df=df.groupby(by=['n','np_id','angle']).max().reset_index()
	df=df.sort_values(by=['np_id'])
	return df

def readtxtfile(filepath):
	d=open(filepath)
	t=d.read()
	d.close()
	return(t)

if __name__=="__main__":
	N=int(sys.argv[1])
	consolidatedfile=sys.argv[2]
	improvedanglesfile=sys.argv[3]
	df_from_consolidatedfile(N,consolidatedfile,improvedanglesfile)
