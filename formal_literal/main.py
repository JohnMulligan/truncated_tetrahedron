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

def main(N=12,worker_number=0,number_of_workers=1,animation_steps=1,angle=1.415471989998):

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
# 	
# 	print(len(list(possible_folds)),"possible folds")
	
	tasks_per_worker=floor(number_of_possible_folds/number_of_workers)
	
# 	print(tasks_per_worker,"tasks per worker with",number of workers,"workers")
	
	worker_start_idx=worker_number*tasks_per_worker
	worker_end_idx=(worker_number+1)*tasks_per_worker-1
	
	if worker_number==number_of_workers-1:
		worker_end_idx=number_of_possible_folds
	
# 	print("worker 1 batch:",worker_start_idx,worker_end_idx)
# 	
# 	print("number_of_entries:	",len(list(islice(possible_folds,worker_start_idx,worker_end_idx))),"items")
	
	timings=[]
	
	timings.append(time.time())
	c=0	
	
	for this_folding in islice(possible_folds,worker_start_idx,worker_end_idx):
		
		G=make_graph.main(N)
		
		folding_id="_".join([str(N),str(worker_start_idx+c)])
		
		start_time=time.time()
		
		node_idxs=sorted(list(nodes_by_index.keys()))
		
		if animation_steps>1:
			
			illustrator.draw_faces(G,N)

			animations={node_id:[] for node_id in G.nodes}

			animation_steps_range=list(range(animation_steps+1))
			
			animation_steps_range
			
			this_angle=angle/animation_steps

			for a in animation_steps_range:

				if animation_steps_range.index(a)==0:
					folding_angle=0
				else:
					folding_angle=this_angle

				folder.main(
					G=G,
					this_folding=this_folding,
					folding_id=folding_id,
					angle=folding_angle,
					fold_spoke_indices=fold_spoke_indices,
					spokes_by_index=spokes_by_index,
					nodes_by_index=nodes_by_index
				)
				
# 				illustrator.draw_graph(G)
				
				for node_id in G.nodes:
					animations[node_id].append([float(p) for p in G.nodes[node_id]['pos']])
			
			d=open('outputs/animations/%s/%s_%s.json' %(str(N),folding_id,str(animation_steps)),'w')
			d.write(json.dumps(animations))
			d.close()

			illustrator.make_processing_animation(folding_id,animation_steps)
			
		else:
			folder.main(
				G=G,
				this_folding=this_folding,
				folding_id=folding_id,
				angle=angle,
				fold_spoke_indices=fold_spoke_indices,
				spokes_by_index=spokes_by_index,
				nodes_by_index=nodes_by_index
			)
			illustrator.draw_graph(G)

		c+=1
		elapsed_seconds=time.time()-start_time
		print("time per folding attempt:",elapsed_seconds, 'seconds')
				
		exit()
	
if __name__=="__main__":
	N=int(sys.argv[1])
	worker_number=int(sys.argv[2])
	number_of_workers=int(sys.argv[3])
	animation_steps=int(sys.argv[4])
	main(N=N,worker_number=worker_number,number_of_workers=number_of_workers,animation_steps=animation_steps)
