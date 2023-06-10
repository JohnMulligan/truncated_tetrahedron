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

def main(fname,animation_steps=10):

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
			
	G=make_graph.main(N)
	
	start_time=time.time()
	
	node_idxs=sorted(list(nodes_by_index.keys()))
		
	illustrator.draw_faces(G,N)

	
	
	d=open("../optimizer/outputs/%s/%s" %(str(N),fname))
	t=d.read()
	matches=json.loads(t)
	d.close()
	
	for thismatch in matches:
		animations={node_id:[] for node_id in G.nodes}
		print(thismatch)
		
		this_folding=matches[thismatch]['this_folding']
		
		min_angle=0
		max_angle=matches[thismatch]["angle"]
		
		for folding_angle in np.linspace(min_angle,max_angle,animation_steps):
			G=make_graph.main(N)

			G=folder.main(
				G=G,
				this_folding=this_folding,
				angle=folding_angle,
				fold_spoke_indices=fold_spoke_indices,
				spokes_by_index=spokes_by_index,
				nodes_by_index=nodes_by_index
			)
			
# 			if folding_angle!=0:
# 			illustrator.draw_graph(G)
			
		
			for node_id in G.nodes:
				animations[node_id].append([float(p) for p in G.nodes[node_id]['pos']])
		outputfilename="_".join([str(N),str(folding_idx),str(max_angle),str(animation_steps),str(hash(thismatch))])+'.json'
		d=open('outputs/%s/%s' %(str(N),outputfilename),'w')
		d.write(json.dumps(animations))
		d.close()
	
if __name__=="__main__":
	fname=sys.argv[1]
	animation_steps=int(sys.argv[2])
	main(fname,animation_steps)