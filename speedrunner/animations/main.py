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

def main(N,animation_steps=10):
	
	N=int(N)
	
	G=make_graph.main(N)
	
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
			
	G=make_graph.main(N)
	
	start_time=time.time()
	
	nodes_indices=[G.nodes[n]['index'] for n in G.nodes if G.nodes[n]['index'] is not None]
		
	illustrator.draw_faces(G,N)

	
	
	d=open("../nots/outputs/%s/consolidated.txt" %(str(N)))
	t=d.read()
	d.close()
	matchstrs=[l for l in t.split("\n\n") if l!='']
	
	d=open("../nots/outputs/%s/flagged.tsv" %(str(N)))
	t=d.read()
	d.close()
	flagged=[l.split('\t') for l in t.split("\n") if l!='']
	
# 	flagged=[l.split('\t') for l in t.split("\n\n") if l!='']
	
	for f in flagged:
		print(f)
	
	
	for thismatchline in matchstrs:
		thismatch=json.loads(thismatchline)
		animations={node_id:[] for node_id in G.nodes}
# 		print(thismatch)
		this_folding_np_id=thismatch['this_folding_np_id']
		n,np_id=[i for i in this_folding_np_id.split('_')]

		this_folding=thismatch['this_folding']
		
		close_neighbors=thismatch['close_neighbors']
		
		min_angle=0
		max_angle=thismatch["angle"]
		
		matchpair=[str(np_id),str(max_angle)]
		
		if matchpair in flagged:		
			print("making-->",matchpair)
			st=time.time()
			for folding_angle in np.linspace(min_angle,max_angle,animation_steps):
				G=make_graph.main(N)

				G=folder.main(
					G=G,
					this_folding=this_folding,
					angle=folding_angle
				)
			
		
				for node_id in G.nodes:
					animations[node_id].append([float(p) for p in G.nodes[node_id]['pos']])
# 			I NEED A SIMPLIFIED FILENAME STRUCTURE THAT CAN SERVE AS A LOOKUP ON THE APP
# 			outputfilename="_".join([str(N),str(hash(close_neighbors)),str(max_angle),str(animation_steps)])+'.json'
			outputfilename="_".join([str(N),str(np_id),str(max_angle)])+'.json'
			d=open('outputs/%s/%s' %(str(N),outputfilename),'w')
			d.write(json.dumps(animations))
			d.close()
			print("finished in %s seconds"%(str(int(time.time()-st))))
	
if __name__=="__main__":
	N=sys.argv[1]
	animation_steps=int(sys.argv[2])
	main(N,animation_steps)