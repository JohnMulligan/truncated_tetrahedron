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
	last_outernode_label=outernode_labels_sorted[1]
	
	terminal_outernodes=[first_outernode_label,last_outernode_label]
	
	close_neighborings={}
	
	all_close_distances=[]
	all_distances=[]
	for n_id_a in nodelist:
		for n_id_b in nodelist:
			if n_id_a!=n_id_b and not (n_id_a in terminal_outernodes and n_id_b in terminal_outernodes) and not (n_id_a in ['first','last'] and n_id_b in ['first','last']):
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

def main(N=12,worker_number=0,number_of_workers=1,sampling_steps=20,threshold_factor=20,min_angle=-pi/2,max_angle=pi/2,r=1000):
	
	G=make_graph.main(N,r)
	
	threshold=r/threshold_factor
	
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
		
		G=make_graph.main(N,r)
		
		folding_id="_".join([str(N),str(worker_start_idx+c)])
		
		start_time=time.time()
		
		node_idxs=sorted(list(nodes_by_index.keys()))
		
		print("threshold",threshold)
		print("min angle to max angle",min_angle,max_angle)

		matches={}
		
		folds_completed=0
		
		folding_id="_".join([str(N),str(worker_start_idx+c)])		
		
		for folding_angle in np.linspace(min_angle,max_angle,sampling_steps):
			
			G=make_graph.main(N,r)
			
			G=folder.main(
				G=G,
				this_folding=this_folding,
				folding_id=folding_id,
				angle=folding_angle,
				fold_spoke_indices=fold_spoke_indices,
				spokes_by_index=spokes_by_index,
				nodes_by_index=nodes_by_index
			)
			
			close_neighborings,mean_close_neighborings=evaluate_folding(G,threshold)
			
			if close_neighborings !={}:
				
				print("->match at",folding_angle,"=",mean_close_neighborings)
					
				close_neighborings_list=sorted(list(close_neighborings.keys()))
				
				if "*".join(close_neighborings_list) not in matches:
					
					matches["*".join(close_neighborings_list)]={
						'angle':folding_angle,
						'mean_close_neighborings':mean_close_neighborings
					}
				
				else:
					if mean_close_neighborings < matches["*".join(close_neighborings_list)]['mean_close_neighborings']:
						matches["*".join(close_neighborings_list)]['mean_close_neighborings']=mean_close_neighborings

				
			folds_completed+=1
			
		print("MATCHES--->",matches)
		
		if matches!={}:
			os.makedirs('outputs/%s/' %str(N), exist_ok=True)
			d=open('outputs/%s/%s.json' %(str(N),str(folding_id)),'w')
			d.write(json.dumps(matches,indent=2))
			d.close()
				
		c+=1
		elapsed_seconds=time.time()-start_time
		
		print(folding_id,"time per folding attempt:",elapsed_seconds/folds_completed, 'seconds.',"total folding time:",int(elapsed_seconds/60),"minutes")
		
	
if __name__=="__main__":
	N=int(sys.argv[1])
	worker_number=int(sys.argv[2])
	number_of_workers=int(sys.argv[3])
	sampling_steps=int(sys.argv[4])
	try:
		min_angle=sys.argv[5]
		max_angle=sys.argv[6]
	except:
		min_angle=-pi/2
		max_angle=pi/2
	main(N=N,worker_number=worker_number,number_of_workers=number_of_workers,sampling_steps=sampling_steps)
