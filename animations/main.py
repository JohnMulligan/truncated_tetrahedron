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
import folder


def get_euclidean_distance(a,b):
	
	ax,ay,az=a
	bx,by,bz=b
	
	ed=sqrt((ax-bx)**2+(ay-by)**2+(az-bz)**2)
	
	return ed
	

def evaluate_folding(G,closeness_threshold):

	nodelist={n:0 for n in G.nodes()}
	
# 	closeness_threshold=.001
	
	outernodes = {x:y['index'] for x,y in G.nodes(data=True) if y['set']=='outer'}
	
	outernodes_sorted={k: v for k, v in sorted(outernodes.items(), key=lambda item: item[1])}
	
	outernode_labels_sorted=list(outernodes_sorted.keys())
	
	first_outernode_label=outernode_labels_sorted[0]
	last_outernode_label=outernode_labels_sorted[-1]
	
	terminal_outernodes=[first_outernode_label,last_outernode_label]
	
	close_neighborings={}
	
	all_close_distances=[]
	all_distances=[]
	for n_id_a in nodelist:
		for n_id_b in nodelist:
			if n_id_a!=n_id_b:
				ed=get_euclidean_distance(
					G.nodes[n_id_a]['pos'],
					G.nodes[n_id_b]['pos']
				)
				all_distances.append(ed)
				if ed < closeness_threshold:
					all_close_distances.append(ed)
				
					neighboring_id="__".join([n_id_a,n_id_b])
				
					if neighboring_id not in close_neighborings:
					
						close_neighborings[neighboring_id]=ed
				
					else:
						if ed < closeness_threshold:
						
							close_neighborings[neighboring_id]=ed
	
# 	print(min(all_distances),all_close_distances)
	if len(all_close_distances)>0:
		mean_close_neighborings=sum(all_close_distances)/len(all_close_distances)
	else:
		mean_close_neighborings=None
	return close_neighborings,mean_close_neighborings



def main(N,animation_steps=10):
	st = time.time()
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

	
	
	d=open("../optimizer/outputs/%s/consolidated.txt" %(str(N)))
	t=d.read()
	d.close()
	matchstrs=[l for l in t.split("\n\n") if l!='']
	
	d=open("../optimizer/outputs/%s/flagged.tsv" %(str(N)))
	t=d.read()
	d.close()
	flagged=[l.split('\t') for l in t.split("\n") if l!='']
	
# 	flagged=[l.split('\t') for l in t.split("\n\n") if l!='']
	
# 	for f in flagged:
# 		print(f)
	
	
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
			loopst=time.time()
			for folding_angle in np.linspace(min_angle,max_angle,animation_steps):
				G=make_graph.main(N)

				G=folder.main(
					G=G,
					this_folding=this_folding,
					angle=folding_angle
				)
				
				evaluate_folding(G,5)
			
		
				for node_id in G.nodes:
					animations[node_id].append([float(p) for p in G.nodes[node_id]['pos']])
# 			I NEED A SIMPLIFIED FILENAME STRUCTURE THAT CAN SERVE AS A LOOKUP ON THE APP
# 			outputfilename="_".join([str(N),str(hash(close_neighbors)),str(max_angle),str(animation_steps)])+'.json'
			outputfilename="_".join([str(N),str(np_id),str(max_angle)])+'.json'
			d=open('outputs/%s/%s' %(str(N),outputfilename),'w')
			d.write(json.dumps(animations))
			d.close()
			print("loop in %s seconds"%(str(int(time.time()-st))))
	print("finished in %s seconds"%(str(int(time.time()-st))))
	
if __name__=="__main__":
	N=sys.argv[1]
	animation_steps=int(sys.argv[2])
	main(N,animation_steps)
