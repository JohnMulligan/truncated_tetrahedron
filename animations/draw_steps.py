import re
from math import cos, sin, sqrt, floor, pi
import sys
import os
import networkx as nx
import make_graph
from itertools import product,islice
import numpy as np
import time
import json
import illustrator
from mpl_toolkits.mplot3d import Axes3D
import folder

def get_euclidean_distance(a,b):
	
	ax,ay,az=a
	bx,by,bz=b
	
	ed=sqrt((ax-bx)**2+(ay-by)**2+(az-bz)**2)
	
	return ed
	

def evaluate_folding(G):

	nodelist={n:0 for n in G.nodes()}
	
	closeness_threshold=.001
	
	close_neighborings={}
	
	for n_id_a in nodelist:
		for n_id_b in nodelist:
			if n_id_a!=n_id_b:
				ed=get_euclidean_distance(
					G.nodes[n_id_a]['pos'],
					G.nodes[n_id_b]['pos']
				)
			
				if ed < closeness_threshold:
				
					neighboring_id="__".join([n_id_a,n_id_b])
				
					if neighboring_id not in close_neighborings:
					
						close_neighborings[neighboring_id]=ed
				
					else:
						if ed < closeness_threshold:
						
							close_neighborings[neighboring_id]=ed
					
	print("close neighborings:",close_neighborings)
		
		










	
	

def main(fname,animation_steps):

	N=int(re.search("^[0-9]+",fname).group(0))
	folding_idx=int(re.search("(?<=_)[0-9]+(?=\.json)",fname).group(0))
	
	G=make_graph.main(N)	
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
			# 
# 	print(nodes_by_index)
	print("fold spoke indices",fold_spoke_indices)
	
	possible_folds=product([i for i in [-1,1]],repeat=len(fold_spoke_indices))
	
	number_of_possible_folds=2**(N-1)
	# 
	print("possible foldings:",number_of_possible_folds)

	for tf in islice(possible_folds,folding_idx,folding_idx+1):
		this_folding=tf
		
	G=make_graph.main(N)
	
	start_time=time.time()
	
	node_idxs=sorted(list(nodes_by_index.keys()))
	
	for thismatch in matches:
		print(thismatch)
		folding_angle=matches[thismatch]["angle"]
		
		min_angle=0
		max_angle=matches[thismatch]["angle"]
		
		G=make_graph.main(N)
		
		for folding_angle in np.linspace(min_angle,max_angle,animation_steps):

			G=folder.main(
				G=G,
				this_folding=this_folding,
				angle=folding_angle,
				fold_spoke_indices=fold_spoke_indices,
				spokes_by_index=spokes_by_index,
				nodes_by_index=nodes_by_index
			)
	
			illustrator.draw_graph(G)
	
if __name__=="__main__":
	fname=sys.argv[1]
# 	
# 	N=int(sys.argv[1])
# 	worker_number=int(sys.argv[2])
# 	number_of_workers=int(sys.argv[3])
# 	main(N=N,worker_number=worker_number,number_of_workers=number_of_workers,animation_steps=animation_steps)
	main(fname)