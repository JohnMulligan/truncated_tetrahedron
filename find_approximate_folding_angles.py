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
from pathlib import Path

#for granular job profiling & debugging memory leaks (be warned, though, it's a hog)
# import gc
# import tracemalloc

def homemade_range_split(i,worker_number,number_workers):
	'''
		numpy's range split is a memory hog, apparently -- not an iterator
	'''
	work_per_worker=int(i/number_workers)
	leftover=i%number_workers
	print("leftover--->",leftover)
	start_idx=worker_number*work_per_worker
	end_idx=work_per_worker*(worker_number+1)
	if worker_number<leftover:
		start_idx+=worker_number
		if start_idx!=0:
			start_idx-=1
		end_idx+=worker_number+1
	else:
		start_idx+=leftover
		if start_idx!=0:
			start_idx-=1
		end_idx+=leftover
	if worker_number==number_workers-1:
		end_idx=i-1
	return start_idx,end_idx

def main(N,worker_number,number_of_workers):
	#we want to strike a balance between a large radius, which makes spurious hits less likely
	#and a threshold for detecting hits that is sufficiently broad to catch the near-hits
	r=100*N
	threshold=r*.010

	#... and the granularity that we're sampling the angles from 0 to pi at
	number_angles_samples=1000

	#... also, we get spurious hits at the beginning and end of the run
	#my old drilldown had a clever way of figuring that out but it didn't work in an htc run
	#right now i'm hard-coding a buffer from observations to avoid a lot of unnecessary false positives that would crud up my outputs
	## but i might be losing some interesting cases as N becomes very large
	zero_buffer=0
	min_angle=0+zero_buffer
	max_angle=pi-zero_buffer
	st=time.time()
	
	step_size=(max_angle-min_angle)/number_angles_samples

	number_of_possible_folds=2**(N-1)
	print("possible folds:",number_of_possible_folds)
	
	print("number of angles sampled:",number_angles_samples)
	
	print("total amount of work:",number_of_possible_folds*number_angles_samples)
	
	print("-------")

	#we are going to split this up in a kind of clever way.
	#if we assume that we have an even number of workers (a condition that I set in __main__) then we can split up the work into a grid
	#each zone would be
	#height=sample angles /2 
	#width=possible folds / (# of workers/2)
	number_of_worker_rows=2
	number_of_worker_cols=int(number_of_workers/2)

	#test batch splitting
	#it's very close....
	#the difficulty is that when I add another "leftover" column of folding indexes, I get 500 new angles to sweep.
	#in the grand scheme of things, though, that's very very close.
	#we'll just have to account for some workers needing a little extra time.
	# running_worker_count=0
	# for worker_idx in range(number_of_workers):
	# 	if worker_idx >= number_of_worker_cols:
	# 		worker_row=1
	# 	else:
	# 		worker_row=0
	# 	# worker_row=worker_idx%number_of_worker_rows
	# 	worker_col=worker_idx%number_of_worker_cols
	# 	worker_sample_angles_start_idx,worker_sample_angles_end_idx=homemade_range_split(number_angles_samples,worker_row,number_of_worker_rows)
	# 	worker_possible_folds_start_idx,worker_possible_folds_end_idx=homemade_range_split(number_of_possible_folds,worker_col,number_of_worker_cols)
	# 	worker_angles_work=worker_sample_angles_end_idx-worker_sample_angles_start_idx+1
	# 	worker_folds_work=worker_possible_folds_end_idx-worker_possible_folds_start_idx+1
	# 	total_work_for_this_worker=	worker_angles_work*worker_folds_work
	# 	print("total work for worker number %d:" %worker_idx,total_work_for_this_worker)
		
	# 	print("worker %d sweeping angle indexes %d-%d and folding indexes %d-%d" %(
	# 		worker_idx,
	# 		worker_sample_angles_start_idx,
	# 		worker_sample_angles_end_idx,
	# 		worker_possible_folds_start_idx,
	# 		worker_possible_folds_end_idx
	# 	))
	# 	running_worker_count+=total_work_for_this_worker
	# print("total work, directly counted:",running_worker_count)
	# exit()

	folds_count=0
	angles_count=0

	if worker_idx >= number_of_worker_cols:
		worker_row=1
	else:
		worker_row=0

	# worker_row=worker_number%number_of_worker_rows
	worker_col=worker_number%number_of_worker_cols

	worker_sample_angles_start_idx,worker_sample_angles_end_idx=homemade_range_split(number_angles_samples,worker_row,number_of_worker_rows)

	worker_possible_folds_start_idx,worker_possible_folds_end_idx=homemade_range_split(number_of_possible_folds,worker_col,number_of_worker_cols)


	worker_angles_work=worker_sample_angles_end_idx-worker_sample_angles_start_idx+1
	worker_folds_work=worker_possible_folds_end_idx-worker_possible_folds_start_idx+1
	total_work_for_this_worker=	worker_angles_work*worker_folds_work
	print("total work for worker number %d:" %worker_number,total_work_for_this_worker)
	
	print("worker %d sweeping angle indexes %d-%d and folding indexes %d-%d" %(
		worker_number,
		worker_sample_angles_start_idx,
		worker_sample_angles_end_idx,
		worker_possible_folds_start_idx,
		worker_possible_folds_end_idx
	))
	
	checkpointpath='checkpoint.txt'
	outputpath='approximate_angles.txt'
	
	if os.path.exists(checkpointpath):
		d=open(checkpointpath,'r')
		t=d.read()
		d.close()
		t=t.strip()
		if t!='':
			clean=t.strip()
			angle_idx_checkpoint,folds_idx_checkpoint=[int(i) for i in clean.split(',')]
			angle_idx_checkpoint
			folds_idx_checkpoint+=1
			
		else:
			print("bad checkpoint file, starting from zero")
			angle_idx_checkpoint=worker_sample_angles_start_idx
			folds_idx_checkpoint=worker_possible_folds_start_idx
			
	else:
		Path(checkpointpath).touch()
		Path(outputpath).touch()
		angle_idx_checkpoint=worker_sample_angles_start_idx
		folds_idx_checkpoint=worker_possible_folds_start_idx
	
	print("worker folds work",worker_folds_work)
	print("worker angles work",worker_angles_work)
	print("angle_idx_checkpoint",angle_idx_checkpoint)
	print("worker_sample_angles_start_idx",worker_sample_angles_start_idx)
	print("folds_idx_checkpoint",folds_idx_checkpoint)
	print("worker_possible_folds_start_idx",worker_possible_folds_start_idx)

	if (angle_idx_checkpoint-worker_sample_angles_start_idx)==0:
		work_finished_by_worker=(folds_idx_checkpoint-worker_possible_folds_start_idx)
	else:
		work_finished_by_worker=(angle_idx_checkpoint+1-worker_sample_angles_start_idx-1)*worker_folds_work+(folds_idx_checkpoint+1-(worker_possible_folds_start_idx+1))
	
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


	for angle_idx in range(angle_idx_checkpoint,worker_sample_angles_end_idx+1):
		angles=np.arange(min_angle,max_angle,step_size)
		angle=islice(angles,angle_idx,angle_idx+1).__next__()
		if initial:
			work_batch_range=range(folds_idx_checkpoint,worker_possible_folds_end_idx+1)
			initial=False
		else:
			work_batch_range=range(worker_possible_folds_start_idx,worker_possible_folds_end_idx+1)

		for folding_idx in work_batch_range:
			st_loop=time.time()
			folding=islice(product([i for i in [-1,1]],repeat=len(fold_spoke_indices)),folding_idx,folding_idx+1).__next__()
			G=make_graph.main(N,r)
			G=folder(
				G=G,
				this_folding=folding,
				angle=angle
			)
			close_neighborings,median_close_neighborings=evaluate_folding(G,threshold)
			if close_neighborings !={}:
				print("->match. angle:",angle_idx,angle,"folding:",folding_idx,folding,"median distance:",median_close_neighborings)
				d=open(outputpath,'a')
				d.write('\t'.join([str(i) for i in [angle,folding_idx,folding,median_close_neighborings,close_neighborings]])+'\n')
				d.close()
			d=open(checkpointpath,'w')
			d.write("%d,%d" %(angle_idx,folding_idx))
			d.close()

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

	if not (number_of_workers)%2==0:
		print("NUMBER OF WORKERS MUST BE EVEN")
		exit()

	main(N,worker_number,number_of_workers)
