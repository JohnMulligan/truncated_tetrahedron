from math import cos, sin, sqrt, floor, pi
import sys
import os
import networkx as nx
from common import make_graph
from itertools import product,islice
import numpy as np
import time
import json
from common.transforms import folder,rotate
from common.evaluations import evaluate_folding,get_euclidean_distance
import gc
import tracemalloc

zero_buffer=0.05

r=1000
min_angle=0+zero_buffer
max_angle=pi-zero_buffer

number_samples=1000

threshold=r*.010

def foldit(N,angle,angle_idx,folding,folding_idx,worker_number):
		
	G=make_graph.main(N,r)
	G=folder(
		G=G,
		this_folding=folding,
		angle=angle
	)
	close_neighborings,median_close_neighborings=evaluate_folding(G,threshold)
	if close_neighborings !={}:
		print("->match at",angle,"=",median_close_neighborings)
		d=open(outputpath,'a')
		d.write('\t'.join([str(i) for i in [angle,folding_idx,this_folding,median_close_neighborings,close_neighborings]])+'\n')
		d.close()

def checkpoint(checkpointpath,angle_idx,folding_idx):
	d=open(checkpointpath,'w')
	d.write("%d,%d" %(angle_idx,folding_idx))
	d.close()

def main(N,worker_number,number_of_workers):
	
	#we get spurious hits at the beginning and end of the run
	#my old drilldown had a clever way of figuring that out but it didn't work in an htc run
	#right now i'm hard-coding a buffer from observations to avoid a lot of unnecessary false positives that would crud up my outputs
	## but i might be losing some interesting cases as N becomes very large
	step_size=(max_angle-min_angle)/number_samples

	number_of_possible_folds=2**(N-1)
	print("possible folds:",number_of_possible_folds)
	
	sub_batches=200

	sample_angles_idxs=np.array_split(np.arange(number_samples),number_of_workers)[worker_number]
	worker_possible_folds_idxs=np.array_split(np.arange(number_of_possible_folds),number_of_workers)[worker_number]
	
	worker_base_angle_idx=sample_angles_idxs[0]
	worker_base_fold_idx=worker_possible_folds_idxs[0]
		
	checkpointpath='outputs/%d/checkpoints/worker_%d.txt' %(N,worker_number)
	outputpath='outputs/%d/approximate_angles_worker_%d.txt' %(N,worker_number)
	
	if os.path.exists(checkpointpath):
		d=open(checkpointpath,'r')
		t=d.read()
		d.close()
		t=t.strip()
		if t!='':
			clean=t.strip()
			angle_idx_checkpoint,folds_idx_checkpoint=[int(i) for i in clean.split(',')]
		else:
			print("bad checkpoint file, starting from zero")
			angle_idx_checkpoint=worker_base_angle_idx
			folds_idx_checkpoint=worker_base_fold_idx
			
	else:
		os.makedirs('outputs/%s/checkpoints/' %str(N), exist_ok=True)
		angle_idx_checkpoint=worker_base_angle_idx
		folds_idx_checkpoint=worker_base_fold_idx
# 	
# 	
# 	this_worker_relative_checkpoints=[this_worker_absolute_start_idx+(i)*int(work_per_worker/sub_batches) for i in range(sub_batches)]
# 	this_worker_relative_checkpoints.append(this_worker_absolute_end_idx)
# 	this_worker_relative_checkpoints.sort()
# 	
# 	print(this_worker_relative_checkpoints)
# 	
# 	remainingrelativestops=[i for i in this_worker_relative_checkpoints if left_off_at_idx<i]
# 	relative_end_idx=min(remainingrelativestops)
# 	remainingrelativestarts=[i for i in this_worker_relative_checkpoints if relative_end_idx>i]
# 	
# 	relative_start_idx=min(remainingrelativestarts)
# 	
# 	
# 	this_work_batch=islice(product(sample_angles_idxs,possible_folds_idxs),relative_start_idx,relative_end_idx)
# 	
# 	print("worker absolute start:",this_worker_absolute_start_idx,"worker absolute stop",this_worker_absolute_end_idx,"checkpoint",left_off_at_idx)
# 	print("worker %d already completed %d of %d steps" %(worker_number,left_off_at_idx-this_worker_absolute_start_idx,work_per_worker))
# 	print("worker relative start:",relative_start_idx,"worker relative stop",relative_end_idx,"checkpoint",left_off_at_idx)
# 	print("worker %d already completed %d of %d steps" %(worker_number,left_off_at_idx-this_worker_absolute_start_idx,relative_end_idx-relative_start_idx))

	#initial graph for spoke indices
	G=make_graph.main(N,r)
	spokes={e:G.edges[e] for e in G.edges if G.edges[e]['set']=='spokes'}
	spokes_by_index={spokes[e]['index']:e for e in spokes}
	fold_spoke_indices=[spokes[s_id]['index'] for s_id in spokes][1:-1]
	
	st=time.time()
	c=0
	
	initial=True
	for angle_idx in islice(sample_angles_idxs,angle_idx_checkpoint,sample_angles_idxs.size):
		angles=np.arange(min_angle,max_angle,(max_angle-min_angle)/number_samples)
		angle=islice(angles,angle_idx,angle_idx+1).__next__()

		if initial:
			for folding_idx in islice(worker_possible_folds_idxs,folds_idx_checkpoint,worker_possible_folds_idxs.size):
				possible_folds=product([i for i in [-1,1]],repeat=len(fold_spoke_indices))
				folding=islice(possible_folds,folding_idx,folding_idx+1).__next__()
				foldit(N,angle,angle_idx,folding,folding_idx,worker_number)
				checkpoint(checkpointpath,angle_idx,folding_idx)
				
				c+=1
				print(c)

			initial=False
		else:
			for folding_idx in islice(worker_possible_folds_idxs,worker_base_fold_idx,worker_possible_folds_idxs.size):
				possible_folds=product([i for i in [-1,1]],repeat=len(fold_spoke_indices))
				this_folding=islice(possible_folds,folding_idx,folding_idx+1).__next__()
				foldit(N,angle,angle_idx,folding,folding_idx,worker_number)
				checkpoint(checkpointpath,angle_idx,folding_idx)
			
				c+=1
				print(c)
		
# 
# 		
# 		relative_amount_of_remaining_work=((relative_end_idx-left_off_at_idx-c)*number_of_workers)
# 		estimated_seconds_remaining=time_per_step*(relative_amount_of_remaining_work)		
# 		print("estimated relative cpu hours remaining:", estimated_seconds_remaining/3600)
# 		
# 		total_amount_of_remaining_work=((this_worker_absolute_end_idx-left_off_at_idx-c)*number_of_workers)
# 		estimated_seconds_remaining=time_per_step*(total_amount_of_remaining_work)		
# 		print("estimated total cpu hours remaining:", estimated_seconds_remaining/3600)
		
	
if __name__=="__main__":
	N=int(sys.argv[1])
	worker_number=int(sys.argv[2])
	number_of_workers=int(sys.argv[3])
	main(N,worker_number,number_of_workers)