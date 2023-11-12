from math import cos, sin, sqrt, floor, pi
import sys
import os
import networkx as nx
from common import make_graph
from itertools import product,islice
import numpy as np
import time
import json
from common.transforms import *
from common.evaluations import *

def main(N,max_level,current_accuracy,r=1000):
	
	G=make_graph.main(N,r)
	
	N=int(N)
	
	knownanglesfile="outputs/%d/approximate_angles_consolidated.txt" %N
	
	d=open(knownanglesfile,'r')
	t=d.read()
	d.close()
	lines=[l for l in t.split('\n') if l!='']
	
	known_matches=[]
	for l in lines:
		angle_str,fold_idx_str=l.split('\t')
		angle=float(angle_str)
		fold_idx=int(fold_idx_str)
		known_matches.append([angle,fold_idx])
		
	spokes={e:G.edges[e] for e in G.edges if G.edges[e]['set']=='spokes'}
	
	spokes_by_index={spokes[e]['index']:e for e in spokes}
	
	nodes_by_index={}
	
	for n_id in G.nodes:
		idx=G.nodes[n_id]['index']
		if idx not in nodes_by_index:
			nodes_by_index[idx]=[n_id]
		else:
			nodes_by_index[idx].append(n_id)
	
	print("---")
	print("nodes")
	for node_idx in nodes_by_index:
		print(node_idx,nodes_by_index[node_idx])
	
	print('---')
	print('spokes')
	for spoke_id in spokes:
		print(spoke_id,spokes[spoke_id],spokes[spoke_id]['index'])
	print('---')
	
	fold_spoke_indices=[spokes[s_id]['index'] for s_id in spokes][1:-1]
	
	
	
	print("fold spoke indices",fold_spoke_indices)
	
	levels=range(current_accuracy,max_level)
	threshold=r*.1
	print(known_matches)
	
	for known_match in known_matches:
		
		base_angle,fold_idx=known_match
		possible_folds=product([i for i in [-1,1]],repeat=len(fold_spoke_indices))
		this_folding=islice(possible_folds,fold_idx,fold_idx+1).__next__()
		
		st=time.time()
		prev_angle=None
		print("BASE ANGLE:",base_angle)
		for level in levels:
			prev_distance=None
			if prev_angle==None:
				min_angle = base_angle-.1**level
				max_angle = base_angle+.1**level
			else:
				min_angle=prev_angle-.1**level
				max_angle = base_angle+.1**level
			print("level",level)
			print("min/max",min_angle,max_angle)
			sampling_steps=10
			folding_angles=np.linspace(min_angle,max_angle,sampling_steps)
			for folding_angle in folding_angles:
				G=make_graph.main(N,r)
				G=folder(
					G=G,
					this_folding=this_folding,
					angle=folding_angle
				)
				close_neighborings,mean_close_neighborings=evaluate_folding(G,threshold)
				print(folding_angle,mean_close_neighborings)
				if prev_distance is not None:
					if prev_distance<mean_close_neighborings:
						print("bottomed out at",prev_distance,"on angle",folding_angle)
						base_angle=prev_angle
						break
					else:
						prev_angle=folding_angle
				prev_distance=mean_close_neighborings

		print("BEST MATCH-->",folding_angle)
		d=open("outputs/%s/known_angles_improved.txt" %str(N),"a")
		d.write("\n\n"+str(folding_angle))
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
