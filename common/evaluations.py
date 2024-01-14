from math import sqrt

from common import make_graph

from math import cos, sin, sqrt, floor, pi

from itertools import product,islice
from common.transforms import folder

def get_euclidean_distance(a,b):
	ax,ay,az=a
	bx,by,bz=b
	ed=sqrt((ax-bx)**2+(ay-by)**2+(az-bz)**2)
	return ed

def evaluate_folding(G,closeness_threshold):
	nodelist={n:0 for n in G.nodes()}
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
		min_close_neighborings=min(all_close_distances)
# 		mean_close_neighborings=sum(all_close_distances)/len(all_close_distances)
	else:
		min_close_neighborings=None
# 	print("minimum:",min(all_distances),"mean",mean_close_neighborings)
	return close_neighborings,min_close_neighborings

def get_loc(angle,folding_idx,N,r=1000,threshold=10):
	'''
		This is where the magic happens.
	'''
	if type(angle)==str:
		angle=float(angle)
	if type(folding_idx):
		folding_idx==int(folding_idx)
	G=make_graph.main(N,r)
	spokes={e:G.edges[e] for e in G.edges if G.edges[e]['set']=='spokes'}
	spokes_by_index={spokes[e]['index']:e for e in spokes}
	fold_spoke_indices=[spokes[s_id]['index'] for s_id in spokes][1:-1]
	folding=islice(product([i for i in [-1,1]],repeat=len(fold_spoke_indices)),folding_idx,folding_idx+1).__next__()
	G=folder(G=G,this_folding=folding,angle=angle)
	close_neighborings,min_close_neighborings=evaluate_folding(G,threshold)
	nodes_and_edges_dict=make_graph.graph_position_dump(G)
	return close_neighborings,folding,min_close_neighborings,nodes_and_edges_dict