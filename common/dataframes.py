import pandas as pd
from decimal import *
import json
import os
import re

def approx_angle_txtfiles_to_df(basepath,approximate_angle_files):

	approximate_angles={
		"angle":[],
		"folding_id":[],
		"min_distance":[],
		"close_neighborings":[]
	}
	
	for aaf in approximate_angle_files:
		print(aaf)
		d=open(os.path.join(basepath,aaf),'r')
		t=d.read()
		d.close()
		goodlines=[line for line in t.split("\n") if line!='']
		for line in goodlines:
			linevals=line.split('\t')
			#i should have kept the intersections in order to score these properly for exploratory purposes later
			if len(linevals)==4:
				angle_str,folding_id_str,folding_pattern_str,min_distance_str=linevals
				#I've been dropping the folding patterns, argh
				if not len(re.findall("(-*1,)+",folding_pattern_str))>5:
						angle_str,folding_id_str,min_distance_str,close_neighborings=linevals
				else:
					close_neighborings=None
			elif len(linevals)==5:
				angle_str,folding_id_str,folding_pattern_str,min_distance_str,close_neighborings=linevals
			

			angle=float(angle_str)
			folding_id=int(folding_id_str)
			min_distance=float(min_distance_str)
			approximate_angles['angle'].append(angle)
			approximate_angles['folding_id'].append(folding_id)
			approximate_angles['min_distance'].append(min_distance)
			
			if close_neighborings is not None:
				approximate_angles['close_neighborings'].append(close_neighborings)

	df=pd.DataFrame.from_dict(approximate_angles)
	
	return df



def df_from_consolidatedfile(N,consolidatedfile,improvedanglesfile,consolidate_tolerance=5):
	consolidated=readtxtfile(consolidatedfile)
	consolidatedlines=[c for c in consolidated.split('\n') if c!='']
	improvedangles=readtxtfile(improvedanglesfile)
	improvedangleslines=[c for c in improvedangles.split('\n') if c!='']
	
	#we are going to bundle these together out to "consolidated_tolerance" decimal places
	#and pick the angle with the minimum distance
	anglemap_prelim={}
	for angle_line in improvedangleslines:
		improved_angle_str,base_angle_str,sample_folding_idx_str, min_distance=angle_line.split('\t')
		rounded_angle=str(Decimal(improved_angle_str[:consolidate_tolerance]))
		this_distance=float(min_distance)
		record={
			'improved_angle_str':improved_angle_str,
			'base_angle_str':base_angle_str,
			'np_id':sample_folding_idx_str,
			'n':N,
			'min_distance':float(min_distance)
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
			distance=r['min_distance']
			if distance<minimum_distance:
				minimum_distance=distance
				minimum_distance_improved_angle_str=improved_angle_str
				
		for r in records:
			base_angle_str=r['base_angle_str']
			anglemap[base_angle_str]=minimum_distance_improved_angle_str
	
	records=[]
	for line in consolidatedlines:
		angle_str,np_id_str,min_distance_str,close_neighborings_str=line.split('\t')
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