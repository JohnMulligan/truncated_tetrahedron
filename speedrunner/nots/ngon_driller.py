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
	
	
	if len(all_close_distances)>0:
		mean_close_neighborings=sum(all_close_distances)/len(all_close_distances)
	else:
		mean_close_neighborings=None
	print("minimum:",min(all_distances),"mean",mean_close_neighborings)
	return close_neighborings,mean_close_neighborings

def main(N,r=1000):
	
	G=make_graph.main(N,r)
	
	N=int(N)
	
	thisngonknownanglesfile="outputs/%d/known_angles.txt" %N
	if os.path.exists(thisngonknownanglesfile):
		knownanglesfile=thisngonknownanglesfile
	else:
		knownanglesfile="known_angles.txt"
	
	d=open(knownanglesfile)
	t=d.read()
	d.close()
	lines=t.split('\n')
	known_angles=[]
	for l in lines:
		try:
			known_angles.append(float(l))
		except:
			print("error with line in angles file:",l)
		
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
	
	
# 	d=open("outputs/%s/angle_range.txt" %N,"r")
# 	t=d.read()
# 	d.close()
# 	min_angle,max_angle=[float(i) for i in t.split("\t")]
	min_angle=0
	max_angle=pi
	
	levels=range(1,10)
	
	sampling_steps=int((max_angle-min_angle)*100)
	
	this_folding=[-1 for i in range(len(fold_spoke_indices))]
	
# 	if min_angle==0:
# 		zerotrip=False
# 	else:
# 		zerotrip=True
	
	d=open("outputs/%s/drilldown.txt" %str(N),"a")
	
	folding_angle=min_angle
	while folding_angle < 3.1:
		zerotrip=False
		for level in levels:
		
			threshold=r*.1
			print("threshold:",threshold)
			print("min angle:",min_angle)
			print("max angle",max_angle)
		
			prev_distance=None
			prev_angle=min_angle
		
			print("sampling steps:",sampling_steps)
		
			folding_angles=np.linspace(min_angle,max_angle,sampling_steps)
		
			#we've got to get past the first downward slope

		
			for folding_angle in folding_angles:
				print(folding_angle)
				G=make_graph.main(N,r)
	
				G=folder.main(
					G=G,
					this_folding=this_folding,
					angle=folding_angle
				)
			
				close_neighborings,mean_close_neighborings=evaluate_folding(G,threshold)
			
				if mean_close_neighborings is not None:
				
					print(prev_distance,mean_close_neighborings,prev_distance<mean_close_neighborings)
					if prev_distance<mean_close_neighborings and prev_distance is not None:
						print("???",close_neighborings,mean_close_neighborings)
						if zerotrip:
							print("bottommed out",folding_angle,mean_close_neighborings)
							min_angle=prev_angle-.1**(level+1)
							max_angle=folding_angle
							sampling_steps=100
							prev_distance=None
							break
					prev_distance=mean_close_neighborings
				else:
					print("no close neighbors. continuing...")
					if not zerotrip:
						print("cleared the zero trap")
						zerotrip=True
			
				prev_angle=folding_angle
			print("BEST MATCH-->",folding_angle)
			d.write("\n\n"+str(folding_angle))
			folding_angle+=.1
			
	# 		print(folding_id,"time per folding attempt:",elapsed_seconds/folds_completed, 'seconds.',"total folding time:",int(elapsed_seconds/60),"minutes")

if __name__=="__main__":
	N=int(sys.argv[1])
	main(N)
