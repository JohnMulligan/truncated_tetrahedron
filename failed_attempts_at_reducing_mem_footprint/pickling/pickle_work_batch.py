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
import pickle

def main(N,worker_number,number_of_workers):
	
# 	tracemalloc.start()
	
	N=int(N)
	
	#we get spurious hits at the beginning and end of the run
	#my old drilldown had a clever way of figuring that out but it didn't work in an htc run
	#right now i'm hard-coding a buffer from observations to avoid a lot of unnecessary false positives that would crud up my outputs
	## but i might be losing some interesting cases as N becomes very large
	zero_buffer=0.05

	r=1000
	min_angle=0+zero_buffer
	max_angle=pi-zero_buffer

	number_samples=1000

	threshold=r*.010

	step_size=(max_angle-min_angle)/number_samples

	number_of_possible_folds=2**(N-1)
	print("possible folds:",number_of_possible_folds)

	sample_angles_idxs=np.arange(number_samples)
	possible_folds_idxs=np.arange(number_of_possible_folds)

	total_work_list=product(sample_angles_idxs,possible_folds_idxs)

	total_amount_of_work=len(sample_angles_idxs)*len(possible_folds_idxs)
	
	work_per_worker=int(total_amount_of_work/number_of_workers)
	
	this_worker_start_idx=work_per_worker*worker_number
	this_worker_end_idx=work_per_worker*(worker_number+1)
	
	checkpointpath='outputs/%d/checkpoints/worker_%d.txt' %(N,worker_number)
	outputpath='outputs/%d/approximate_angles_worker_%d.txt' %(N,worker_number)
	
	if os.path.exists(checkpointpath):
		d=open(checkpointpath,'r')
		t=d.read()
		d.close()
		t=t.strip()
		if t!='':
			left_off_at_idx=int(t.strip())
		else:
			left_off_at_idx=this_worker_start_idx
	else:
		os.makedirs('outputs/%s/checkpoints/' %str(N), exist_ok=True)
		left_off_at_idx=this_worker_start_idx
	
	this_work_batch=islice(total_work_list,left_off_at_idx,this_worker_end_idx)
	
	with open("%d_%d_%d.pickle" %(N,worker_number,number_of_workers), 'wb') as f:
		pickle.dump(this_work_batch,f)

if __name__=="__main__":
	N=int(sys.argv[1])
	worker_number=int(sys.argv[2])
	number_of_workers=int(sys.argv[3])
	main(N,worker_number,number_of_workers)