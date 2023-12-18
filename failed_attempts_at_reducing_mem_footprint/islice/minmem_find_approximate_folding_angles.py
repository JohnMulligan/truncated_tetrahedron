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

	total_amount_of_work=sample_angles_idxs.size*possible_folds_idxs.size
	
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
	
	print("worker start:",this_worker_start_idx,"worker stop",this_worker_end_idx,"checkpoint",left_off_at_idx)
	
	work_idxs=np.arange(left_off_at_idx,this_worker_end_idx)
	
	G=make_graph.main(N,r)
	spokes={e:G.edges[e] for e in G.edges if G.edges[e]['set']=='spokes'}
	spokes_by_index={spokes[e]['index']:e for e in spokes}
	fold_spoke_indices=[spokes[s_id]['index'] for s_id in spokes][1:-1]
	
	st=time.time()
	c=0
	
	print("worker %d already completed %d of %d steps" %(worker_number,left_off_at_idx-this_worker_start_idx,work_per_worker))
	
	for work_idx in work_idxs:
		work_item=islice(product(sample_angles_idxs,possible_folds_idxs),work_idx,work_idx+1).__next__()

		angle_idx,fold_idx=work_item
		
		this_angle=islice(np.arange(min_angle,max_angle,(max_angle-min_angle)/number_samples),angle_idx,angle_idx+1).__next__()
		
		this_folding=islice(product([i for i in [-1,1]],repeat=len(fold_spoke_indices)),fold_idx,fold_idx+1).__next__()
		
		G=make_graph.main(N,r)
		G=folder(
			G=G,
			this_folding=this_folding,
			angle=this_angle
		)
		close_neighborings,median_close_neighborings=evaluate_folding(G,threshold)
		if close_neighborings !={}:
			print("->match at",this_angle,"=",median_close_neighborings)
			d=open(outputpath,'a')
			d.write('\t'.join([str(i) for i in [this_angle,fold_idx,this_folding,median_close_neighborings,close_neighborings]])+'\n')
			d.close()
		
		d=open(checkpointpath,'w')
		d.write(str(c+left_off_at_idx))
		d.close()
		
		c+=1
		
		time_per_step=(time.time()-st)/c
		
		amount_of_remaining_work=((this_worker_end_idx-left_off_at_idx-c)*number_of_workers)
		estimated_seconds_remaining=time_per_step*(amount_of_remaining_work)
		
		print("estimated total cpu hours remaining:", estimated_seconds_remaining/3600)
	
if __name__=="__main__":
	N=int(sys.argv[1])
	worker_number=int(sys.argv[2])
	number_of_workers=int(sys.argv[3])
	main(N,worker_number,number_of_workers)