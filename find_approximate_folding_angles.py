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

#for granular job profiling & debugging memory leaks (be warned, though, it's a hog)
# import gc
# import tracemalloc

#we want to strike a balance between a large radius, which makes spurious hits less likely
#and a threshold for detecting hits that is sufficiently broad to catch the near-hits
r=1000
threshold=r*.010

#... and the granularity that we're sampling the angles from 0 to pi at
number_samples=1000

#... also, we get spurious hits at the beginning and end of the run
#my old drilldown had a clever way of figuring that out but it didn't work in an htc run
#right now i'm hard-coding a buffer from observations to avoid a lot of unnecessary false positives that would crud up my outputs
## but i might be losing some interesting cases as N becomes very large
zero_buffer=0.05
min_angle=0+zero_buffer
max_angle=pi-zero_buffer

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
	
	st=time.time()
	
	step_size=(max_angle-min_angle)/number_samples

	number_of_possible_folds=2**(N-1)
	print("possible folds:",number_of_possible_folds)
	
	print("number of angles sampled:",number_samples)
	
	print("total amount of work:",number_of_possible_folds*number_of_possible_folds)
	
	print("-------")
	
	worker_sample_angles_idxs=np.array_split(np.arange(number_samples),number_of_workers)[worker_number]
	worker_possible_folds_idxs=np.array_split(np.arange(number_of_possible_folds),number_of_workers)[worker_number]
	
	total_work_for_this_worker=	worker_sample_angles_idxs.size*worker_possible_folds_idxs.size
	print("total work for worker number %d:" %worker_number,total_work_for_this_worker)
	
	worker_base_angle_idx=worker_sample_angles_idxs[0]
	worker_max_angle_idx=worker_sample_angles_idxs[-1]
	
	worker_base_fold_idx=worker_possible_folds_idxs[0]
	worker_max_fold_idx=worker_possible_folds_idxs[-1]
	
	print("worker %d sweeping angle indexes %d-%d and folding indexes %d-%d" %(
		worker_number,
		worker_base_angle_idx,
		worker_max_angle_idx,
		worker_base_fold_idx,
		worker_max_fold_idx
	))
	
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
			angle_idx_checkpoint+=1
			folds_idx_checkpoint+=1
			
		else:
			print("bad checkpoint file, starting from zero")
			angle_idx_checkpoint=worker_base_angle_idx
			folds_idx_checkpoint=worker_base_fold_idx
			
	else:
		os.makedirs('outputs/%s/checkpoints/' %str(N), exist_ok=True)
		angle_idx_checkpoint=worker_base_angle_idx
		folds_idx_checkpoint=worker_base_fold_idx
	
	if (angle_idx_checkpoint-worker_base_angle_idx)==0:
		work_finished_by_worker=(folds_idx_checkpoint-worker_base_fold_idx)
	else:
		work_finished_by_worker=((angle_idx_checkpoint-worker_base_angle_idx)-1)*worker_possible_folds_idxs.size*worker_sample_angles_idxs.size+(folds_idx_checkpoint-worker_base_fold_idx)
	
	remaining_work_for_worker=total_work_for_this_worker-work_finished_by_worker
	
	print("worker %d already finished %d steps. %d remaining." %(worker_number,work_finished_by_worker,remaining_work_for_worker))
	
	#initial graph for spoke indices
	G=make_graph.main(N,r)
	spokes={e:G.edges[e] for e in G.edges if G.edges[e]['set']=='spokes'}
	spokes_by_index={spokes[e]['index']:e for e in spokes}
	fold_spoke_indices=[spokes[s_id]['index'] for s_id in spokes][1:-1]
	
	seconds_to_initialize=int(time.time()-st)
	
	print("worker %d took %d seconds to initialize." %(worker_number,seconds_to_initialize))
	
	st=time.time()
	c=0
	lastc=0
	estimation_step=10
	
	initial=True
	for angle_idx in worker_sample_angles_idxs:
		angles=np.arange(min_angle,max_angle,(max_angle-min_angle)/number_samples)
		angle=islice(angles,angle_idx,angle_idx+1).__next__()
		if initial:
			work_batch=islice(worker_possible_folds_idxs,(folds_idx_checkpoint-worker_base_fold_idx),worker_possible_folds_idxs.size)
			initial=False
		else:
			work_batch=worker_possible_folds_idxs
		
		for folding_idx in work_batch:
			folding=islice(product([i for i in [-1,1]],repeat=len(fold_spoke_indices)),folding_idx,folding_idx+1).__next__()
			foldit(N,angle,angle_idx,folding,folding_idx,worker_number)
			checkpoint(checkpointpath,angle_idx,folding_idx)
			c+=1
			
			time_elapsed=time.time()-st
			
			seconds_per_step=time_elapsed/c
			
			relative_amount_of_remaining_work=remaining_work_for_worker-c
			estimated_seconds_remaining=seconds_per_step*relative_amount_of_remaining_work
			estimated_hours_remaining_for_worker=estimated_seconds_remaining/3600
			
			if c-lastc>=estimation_step:
				print("estimated hours remaining for worker %d: %d" %(worker_number,estimated_hours_remaining_for_worker))
				lastc=int(c)
			
	
if __name__=="__main__":
	N=int(sys.argv[1])
	worker_number=int(sys.argv[2])
	number_of_workers=int(sys.argv[3])
	main(N,worker_number,number_of_workers)