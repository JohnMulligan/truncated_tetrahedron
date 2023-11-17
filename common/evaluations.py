from math import sqrt
from statistics import median

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
		median_close_neighborings=median(all_close_distances)
# 		mean_close_neighborings=sum(all_close_distances)/len(all_close_distances)
	else:
		median_close_neighborings=None
# 	print("minimum:",min(all_distances),"mean",mean_close_neighborings)
	return close_neighborings,median_close_neighborings