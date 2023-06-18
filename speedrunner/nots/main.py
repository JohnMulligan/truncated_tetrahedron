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

def main(N,worker_number,number_of_workers,r=1000):
	
	G=make_graph.main(N,r)
	
	threshold=5
	
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
	
	possible_folds=product([i for i in [-1,1]],repeat=len(fold_spoke_indices))
	
	number_of_possible_folds=2**(N-1)
	
	print("possible foldings:",number_of_possible_folds)
	
	total_work_list=np.array(range(number_of_possible_folds))
	
	checkpointfilepath="outputs/%s/checkpoint.txt" %str(N)
	if os.path.exists(checkpointfilepath):
		d=open(checkpointfilepath,'r')
		t=d.read()
		d.close()
		lines=t.split("\n")
		checkpoints=np.array([int(l) for l in lines if l!=''])
		remaining_work=np.array([i for i in total_work_list if i not in checkpoints])
	else:
		os.makedirs('outputs/%s/' %str(N), exist_ok=True)
		remaining_work=np.array(total_work_list)
	
	print("total amount of work remaining:",len(remaining_work))
	workbatches=np.array_split(remaining_work,number_of_workers)
	
	this_work_batch=workbatches[worker_number]
	
	print("work for this worker:",len(this_work_batch))
	
	for this_step in this_work_batch:
		worker_start_idx=this_step
		worker_end_idx=this_step+1
# 		print(worker_start_idx,worker_end_idx)

		d=open(checkpointfilepath,'a')
	
		G=make_graph.main(N,r)
	
		start_time=time.time()
		possible_folds=product([i for i in [-1,1]],repeat=len(fold_spoke_indices))
# 		node_idxs=sorted(list(nodes_by_index.keys()))
		for this_folding in islice(possible_folds,worker_start_idx,worker_end_idx):
# 			this_folding=(-1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1)
			print(this_folding)
			matches=[]
		
			folds_completed=0
	# 		known_angles=[1.41547199]
	# 		known_angles=[2.034443043]
			for folding_angle in known_angles:
				print("angle:",folding_angle)
				G=make_graph.main(N,r)
			
				G=folder.main(
					G=G,
					this_folding=this_folding,
					angle=folding_angle
				)
			
				close_neighborings,mean_close_neighborings=evaluate_folding(G,threshold)
				
				if close_neighborings !={}:
				
					print("->match at",folding_angle,"=",mean_close_neighborings)
					
					close_neighborings_list=sorted(list(close_neighborings.keys()))
					
					close_neighborings_id="*".join(close_neighborings_list)
					
					matches.append({
						"close_neighbors":close_neighborings_id,
						"close_neighborings_count":len(close_neighborings),
						"angle":folding_angle,
						"mean_close_neighborings":mean_close_neighborings,
						"this_folding":this_folding,
						"this_folding_np_id":"_".join([str(i) for i in [N,worker_start_idx]])
					})
			
			print("MATCHES--->",matches)

			if len(matches)>0:
				e=open('outputs/%s/%s.txt' %(str(N),str(worker_number)),'a')
				
				for thismatch in matches:
					e.write("\n\n"+json.dumps(thismatch))
				
				e.close()
		
			d.write('\n%s' %str(worker_start_idx))
			
			elapsed_seconds=time.time()-start_time
		
# 		print(folding_id,"time per folding attempt:",elapsed_seconds/folds_completed, 'seconds.',"total folding time:",int(elapsed_seconds/60),"minutes")

if __name__=="__main__":
	N=int(sys.argv[1])
	worker_number=int(sys.argv[2])
	number_of_workers=int(sys.argv[3])
	print(N,worker_number,number_of_workers)
	main(N,worker_number,number_of_workers)