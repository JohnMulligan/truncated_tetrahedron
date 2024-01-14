from math import cos, sin, sqrt, floor, pi
import sys
import os
import networkx as nx
import pandas as pd
from common import make_graph
from itertools import product,islice
import numpy as np
import re
import time
import json
from common.transforms import *
from common.evaluations import *

def main(N,max_level,current_accuracy,r=1000):
	
	G=make_graph.main(N,r)
	
	N=int(N)
	
	improved_angles_file="outputs/%s/angles_improved.txt" %str(N)
	
	
	#ADDING IN SOME CHECKPOINTING -- NOT PARALLELIZED
	already_improved_angles=[]
	if os.path.exists(improved_angles_file):
		print("FILE EXISTS")
		#os.remove(improved_angles_file)
		#this takes much longer than expected -- so we need some kind of checkpointing rather than blowing away the prior attempt
		d=open(improved_angles_file,'r')
		t=d.read()
		d.close()
		lines=[l for l in t.split('\n') if l!='']
		#LINES LIKE: 1.4154719913005755	1.4074335088082275	1400	1.2201723835589789e-08
		
		for l in lines:
			improved_angle_str,base_angle_str,matched_folding_id_str,distance_str=l.split('\t')
			already_improved_angles.append(base_angle_str)
	
	print("already improved angles-->",already_improved_angles)
	
	knownanglesfile="outputs/%d/approximate_angles_consolidated.txt" %N
	
	d=open(knownanglesfile,'r')
	t=d.read()
	d.close()
	lines=[l for l in t.split('\n') if l!='']
	
	records=[]
	screened_out_angles=[]
	for line in lines:
		angle_str,np_id_str,min_distance_str,close_neighborings_str=line.split('\t')
		if angle_str not in already_improved_angles:
			record={
				'np_id':int(np_id_str),
				'angle_str':angle_str,
				'min_distance':float(min_distance_str)
			}
			records.append(record)
		else:
			screened_out_angles.append(angle_str)
	
	print("screened out %d records" %len(list(set(screened_out_angles))))
	
	df=pd.DataFrame.from_records(records)
	df2=df[['angle_str','min_distance']]
	df2=df2.groupby(by=['angle_str']).min()
	df2d=df2.to_dict()['min_distance']
	for a in df2d:
		dist=df2d[a]
	
	
	test_cases={}
	for angle_str in df2d:
		min_distance=df2d[angle_str]
		candidate_np_id=df[(df['angle_str']==angle_str) &  (df['min_distance']==min_distance)]['np_id'].iloc[0]
		test_cases[angle_str]=int(candidate_np_id)
	
	print("%d remaining" %len(test_cases))		
	#END CHECKPOINTING
	
	spokes={e:G.edges[e] for e in G.edges if G.edges[e]['set']=='spokes'}
	
	spokes_by_index={spokes[e]['index']:e for e in spokes}
	
	nodes_by_index={}
	
	for n_id in G.nodes:
		idx=G.nodes[n_id]['index']
		if idx not in nodes_by_index:
			nodes_by_index[idx]=[n_id]
		else:
			nodes_by_index[idx].append(n_id)
	
# 	print("---")
# 	print("nodes")
# 	for node_idx in nodes_by_index:
# 		print(node_idx,nodes_by_index[node_idx])
# 	
# 	print('---')
# 	print('spokes')
# 	for spoke_id in spokes:
# 		print(spoke_id,spokes[spoke_id],spokes[spoke_id]['index'])
# 	print('---')
	
	fold_spoke_indices=[spokes[s_id]['index'] for s_id in spokes][1:-1]
	
# 	print("fold spoke indices",fold_spoke_indices)
	
	levels=range(current_accuracy,max_level)
	print("levels-->",levels)
	threshold=r*.01
	sampling_steps=20
	
	for angle_str in test_cases:
		base_angle=float(angle_str)
		fold_idx=test_cases[angle_str]
		test_case=[base_angle,fold_idx]
		possible_folds=product([i for i in [-1,1]],repeat=len(fold_spoke_indices))
		this_folding=islice(possible_folds,fold_idx,fold_idx+1).__next__()
		
		st=time.time()
		prev_angle=None
		print("BASE ANGLE:",base_angle)
		for level in levels:
			prev_distance=None
			print("prev angle-->",prev_angle)
			angle_test_margin=.1**level
			if prev_angle==None:
				min_angle = base_angle-angle_test_margin
				max_angle = base_angle+angle_test_margin
			else:
				min_angle=prev_angle-angle_test_margin
				max_angle = prev_angle
			
			
			bottomed_out=False
			while not bottomed_out:
				folding_angles=np.linspace(min_angle,max_angle,sampling_steps)
				print("level",level)
				print("min/max",min_angle,max_angle)
				print("angle step",(max_angle-min_angle)/sampling_steps)
				step_count=0
				shift_left=False
				for folding_angle in folding_angles:
					
					G=make_graph.main(N,r)
					G=folder(
						G=G,
						this_folding=this_folding,
						angle=folding_angle
					)
					close_neighborings,min_close_neighborings=evaluate_folding(G,threshold)
					print(folding_angle,min_close_neighborings)
					if prev_distance is not None:
						if prev_distance<min_close_neighborings:
							print("bottomed out at",prev_distance,"on angle",folding_angle)
							if step_count < 2:
								print("...however, we shouldn't hit that on our first step. shifting window left...")
								shift_left=True
								prev_angle=folding_angle
								break
							else:
								bottomed_out=True
								prev_angle=folding_angle
								break
					prev_angle=folding_angle
					
					prev_distance=min_close_neighborings
					step_count+=1
				if not bottomed_out:
					if shift_left:
						min_angle-=angle_test_margin/2
						max_angle=prev_angle
						prev_distance=None
						print("--> SHIFTING WINDOW LEFT & TIGHTENING")
					else:					
						min_angle=prev_angle
						max_angle+=angle_test_margin/2
						prev_distance=None
						print("--> SHIFTING WINDOW RIGHT & TIGHTENING")
			

		print("BEST MATCH-->",folding_angle)
		d=open(improved_angles_file,"a")
		base_angle,fold_idx=test_case
		line=[str(folding_angle),angle_str,str(fold_idx),str(min_close_neighborings)]
		d.write('\n'+'\t'.join(line))
		d.close()
		print("angle optimized in %d seconds" %int(time.time()-st))

if __name__=="__main__":
	N=int(sys.argv[1])
	try:
		max_level=int(sys.argv[2])
	except:
		max_level=11
	try:
		current_accuracy=int(sys.argv[3])
	except:
		current_accuracy=2
	main(N,max_level=max_level,current_accuracy=current_accuracy)
