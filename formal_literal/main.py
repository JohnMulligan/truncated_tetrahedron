from math import cos, sin, sqrt, floor, pi
import sys
import os
import networkx as nx
from sympy.geometry import Point,Point3D, Line3D,Plane,Segment3D
import matplotlib.pyplot as plt
import make_graph
from itertools import product,islice
import numpy as np
from transforms import rotate
import time
import json
from mpl_toolkits.mplot3d import Axes3D

def array_permutations(m, n):
	arrays=[]
	for vals in product([0,1], repeat=m*n):
		arr = np.array(vals).reshape((m, n))
		arrays.append(arr)
	return(arrays)

def posmaker(G):
	
	pos={
		node_id:G.nodes[node_id]['pos'] for node_id in G.nodes
	}
# 	print("positions",pos)
	return pos

def main(N=12,worker_number=0,number_of_workers=1,animation_steps=10,angle=1.415471989998):

	G=make_graph.main(N)
	
	facia=make_graph.make_facia(G)
	
	triangle_block_text_lines=["beginShape();"]
	for s in facia:
		for v in s:
			triangle_block_text_lines.append("vertex(%sx[t],%sy[t],%sz[t]);" %(v,v,v))
		triangle_block_text_lines.append("endShape(CLOSE);")
	
	triangle_block="\n".join(triangle_block_text_lines)
	
	d=open(str(N)+"_edges.js",'w')
	d.write(triangle_block)
	d.close()
	
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
	G=make_graph.main(N)
	
	animations={}
	for this_folding in islice(possible_folds,worker_start_idx,worker_end_idx):
		
		folding_id="_".join([str(N),str(worker_start_idx+c)])
		
		animations={folding_id:{node_id:[] for node_id in G.nodes}}
		
		start_time=time.time()
# 		print('do stuff.')
# 		
# 		print("signs",i)
		
# 		spoke_idxs=sorted([spokes[e]['index'] for e in spokes])
# 		
# 		print(spoke_idxs)
		
		node_idxs=sorted(list(nodes_by_index.keys()))
# 		print("SPOKES")
		
		for a in range(animation_steps+1):
			
			this_angle=angle*(a/animation_steps)
			print(this_angle)
			
			for r in fold_spoke_indices:
			
	# 			print("---")
				this_spoke_name=spokes_by_index[r]
			
	# 			print("this spoke",r,this_spoke_name)
			
				subsequent_spoke_idxs=fold_spoke_indices[r:]
			
	# 			print("subsequent spokes",[(r2,spokes_by_index[r2]) for r2 in subsequent_spoke_idxs])
			
				affected_nodes=[]
			
				rna=G.nodes[this_spoke_name[0]]
				rnb=G.nodes[this_spoke_name[1]]
			
				rotation_axis=Line3D(
					Point3D(rna['pos']),
					Point3D(rnb['pos'])
				)
			
	# 			print("rotation axis",r,this_spoke_name[0],this_spoke_name[1],rotation_axis)
			
				these_affected_nodes=[]
			
				for node_idx in nodes_by_index:
					if node_idx > r:
	# 					print(node_idx,nodes_by_index[node_idx],i[node_idx-2])
						these_affected_nodes+=[(n_id,this_folding[node_idx-2]) for n_id in nodes_by_index[node_idx]]
	# 			print('---')
	# 			print("affected nodes:")

				for n_t in these_affected_nodes:
					n_id,sign=n_t
					
					n=G.nodes[n_id]
					affected_point=Point3D(n['pos'])
					affected_point_post_rotation=rotate(rotation_axis,affected_point,this_angle*sign)
				
					G.nodes[n_id]['pos']=(
						affected_point_post_rotation.x,
						affected_point_post_rotation.y,
						affected_point_post_rotation.z
					)
			
			for node_id in G.nodes:
				animations[folding_id][node_id].append([float(p) for p in G.nodes[node_id]['pos']])
				
			make_graph.draw_graph(G)
		
		c+=1
		elapsed_seconds=time.time()-start_time
		print("time per folding attempt:",elapsed_seconds, 'seconds')
		
		d=open(folding_id+'.json','w')
		d.write(json.dumps(animations))
		d.close()
		
		exit()
		
# 		I gave up on this graphing library's nonsense. Used the tutorial cut-and-paste
# 		https://networkx.org/documentation/stable/auto_examples/3d_drawing/plot_basic.html			
	
if __name__=="__main__":
	N=int(sys.argv[1])
	worker_number=int(sys.argv[2])
	number_of_workers=int(sys.argv[3])
	main(N=N,worker_number=worker_number,number_of_workers=number_of_workers)
