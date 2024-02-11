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
from common.evaluations import get_euclidean_distance,get_loc
from pathlib import Path

def main(N,worker_numbers):
	r=1000
	threshold=10
	
	st=time.time()

	number_of_possible_folds=2**(N-1)
	print("total amount of work/possible folds:",number_of_possible_folds)
	print("-------")
	
	checkpointpath='checkpoint_%d_%d.txt' %(N,worker_number)
	outputpath='optimized_angles_worker_%d_%d.txt' %(N,worker_number)
	
	if os.path.exists(checkpointpath):
		d=open(checkpointpath,'r')
		t=d.read()
		d.close()
		t=t.strip()
		if t!='':
			folds_idx_checkpoint=int(t.strip())
		else:
			print("bad checkpoint file, starting from zero")
			folds_idx_checkpoint=0
	else:
		Path(checkpointpath).touch()
		Path(outputpath).touch()
		folds_idx_checkpoint=0
	
	print("work remaining",number_of_possible_folds-folds_idx_checkpoint)
	
	#on local:
# 	anglesfile='outputs/%d/angles_improved_consolidated.txt' %N
	#on condor
	anglesfile='angles_improved_consolidated.txt'
	d=open(anglesfile,'r')
	t=d.read()
	d.close()
	lines=[l for l in t.split('\n') if t!='']
	print(lines)
	angle=float(lines[worker_number])
	print(angle)
	for folding_idx in range(folds_idx_checkpoint,number_of_possible_folds):
		print("++++++++\nfolding idx",folding_idx,"\n++++++++")
		st_loop=time.time()
		close_neighborings,folding,min_close_neighborings,nodes_and_edges_dict=get_loc(angle,folding_idx,N,r,threshold)
		if close_neighborings !={}:
			print("-------\n->match. angle:",angle,"\n",
				"count:",len(close_neighborings),"\n",
				"folding:",folding_idx,folding,"\n",
				"min distance:",min_close_neighborings
			)
			d=open(outputpath,'a')
			d.write('\t'.join([str(i) for i in [
				angle,
				folding_idx,
				folding,
				min_close_neighborings,
				json.dumps(close_neighborings),
				json.dumps(nodes_and_edges_dict)]]
			)+'\n')
			d.close()
		d=open(checkpointpath,'w')
		d.write("%d" %folding_idx)
		d.close()
			
if __name__=="__main__":
	N=int(sys.argv[1])
	worker_number=int(sys.argv[2])
	main(N,worker_number)
