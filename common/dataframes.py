import pandas as pd
import os
import re

def approx_angle_txtfiles_to_df(basepath,approximate_angle_files):

	approximate_angles={
		"angle":[],
		"folding_id":[],
		"median_distance":[],
		"close_neighborings":[]
	}

	for aaf in approximate_angle_files:
		d=open(os.path.join(basepath,aaf),'r')
		t=d.read()
		d.close()
		goodlines=[line for line in t.split("\n") if line!='']
		for line in goodlines:
			linevals=line.split('\t')
			#i should have kept the intersections in order to score these properly for exploratory purposes later
			if len(linevals)==4:
				angle_str,folding_id_str,folding_pattern_str,median_distance_str=linevals
				#I've been dropping the folding patterns, argh
				if not len(re.findall("(-*1,)+",folding_pattern_str))>5:
						angle_str,folding_id_str,median_distance_str,close_neighborings=linevals
				else:
					close_neighborings=None
			elif len(linevals)==5:
				angle_str,folding_id_str,folding_pattern_str,median_distance_str,close_neighborings=linevals
			
			print('angle_str',angle_str)
			print('folding_id_str',folding_id_str)
			print('median_distance_str',median_distance_str)
			print('close_neighborings',close_neighborings)
			


			angle=float(angle_str)
			folding_id=int(folding_id_str)
			median_distance=float(median_distance_str)
			approximate_angles['angle'].append(angle)
			approximate_angles['folding_id'].append(folding_id)
			approximate_angles['median_distance'].append(median_distance)
			
			if close_neighborings is not None:
				approximate_angles['close_neighborings'].append(close_neighborings)

	df=pd.DataFrame.from_dict(approximate_angles)
	
	return df