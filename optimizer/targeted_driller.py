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

def main(N,max_level,current_accuracy,r=1000):
	
	G=make_graph.main(N,r)
	
	N=int(N)
	
	knownanglesfile="outputs/%d/known_angles.txt" %N
	
	d=open(knownanglesfile,'r')
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
	
	possible_folds=product([i for i in [-1,1]],repeat=len(fold_spoke_indices))
	
	#right now i'm just testing on the first (or last) folding, as it seems to hit pretty consistently
	##but i've seen hits around index 25 as well. not clear what the logic is, and i'm not doing that insane of a parameter sweep
	this_folding=list(possible_folds)[0]
	
	print("fold spoke indices",fold_spoke_indices)
	
	levels=range(current_accuracy,max_level)
	threshold=r*.1
	print(known_angles)
	for known_angle in known_angles:
		prev_angle=None
		base_angle=known_angle
		print("BASE ANGLE:",base_angle)
		for level in levels:
			prev_distance=None
			if prev_angle==None:
				min_angle = base_angle-.1**level
				max_angle = base_angle+.1**level
			else:
				min_angle=prev_angle
				max_angle = base_angle+.1**level
			print("level",level)
			print("min/max",min_angle,max_angle)
			sampling_steps=100
			folding_angles=np.linspace(min_angle,max_angle,sampling_steps)
			for folding_angle in folding_angles:
				print("angle",folding_angle)
				G=make_graph.main(N,r)
				G=folder.main(
					G=G,
					this_folding=this_folding,
					angle=folding_angle
				)
				close_neighborings,mean_close_neighborings=evaluate_folding(G,threshold)
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
	d=open('outputs/%s/targeted_driller_running_time.txt' %str(N),'w')
	d.write(str(running_time))
	d.close()
		
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
