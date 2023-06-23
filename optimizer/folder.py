import json
import illustrator
from sympy.geometry import Point,Point3D, Line3D,Plane,Segment3D
from transforms import rotate
import networkx as nx

def main(G,this_folding,angle):
# 	print("--->",angle)
	spokes=nx.Graph([(u,v,d) for u,v,d in G.edges(data=True) if d['set']=='spokes'])
	spoke_indices=[spokes.edges[e]['index'] for e in spokes.edges if spokes.edges[e]['index'] is not None]
	spoke_indices.sort()
	fold_spoke_indices=spoke_indices[1:-1]
	
# 	print(fold_spoke_indices)	
# 	print(this_folding)
	for r in fold_spoke_indices:
	
# 		print("---")
		
		this_spoke_name=[e for e in spokes.edges if spokes.edges[e[0],e[1]]['index']==r][0]
	
		subsequent_spoke_idxs=fold_spoke_indices[r:]
	
# 		print("subsequent spoke_idxs", subsequent_spoke_idxs)
	
		affected_nodes=[]
		
		rna=G.nodes[this_spoke_name[0]]
		rnb=G.nodes[this_spoke_name[1]]
		rna['name']=this_spoke_name[0]
		rnb['name']=this_spoke_name[1]


		if rna['set']=='inner':
			tmp=rna
			rna=rnb
			rnb=tmp
# 		print("this spoke",r,(rna['name'],rnb['name']))

		rotation_axis=Line3D(
			Point3D(rna['pos']),
			Point3D(rnb['pos'])
		)


# 		print("rotation axis",r,this_spoke_name[0],this_spoke_name[1],rotation_axis)
	
		sign=this_folding[fold_spoke_indices.index(r)]
	
		these_affected_nodes=[]
		
		
# 		print("sign of folding",sign)
		
		for n_id in G.nodes():
			if G.nodes[n_id]['index']>r:
				these_affected_nodes.append(n_id)
# 		print("affected nodes:",these_affected_nodes)

		for n_id in these_affected_nodes:
			
			n=G.nodes[n_id]
			affected_point=Point3D(n['pos'])
			affected_point_post_rotation=rotate(rotation_axis,affected_point,angle*sign)
# 			print(n_id,affected_point_post_rotation)
			G.nodes[n_id]['pos']=(
				affected_point_post_rotation.x,
				affected_point_post_rotation.y,
				affected_point_post_rotation.z
			)
# 			if angle!=0:
# 				illustrator.draw_graph(G)
# 	exit()
	return G
