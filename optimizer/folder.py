import json
import illustrator
from sympy.geometry import Point,Point3D, Line3D,Plane,Segment3D
from transforms import rotate

def main(G,this_folding,angle,fold_spoke_indices,nodes_by_index,spokes_by_index):
# 	print("-->",angle)
# 	print("fold spoke indices:")
# 	print(len(this_folding),fold_spoke_indices)
	fold_spoke_indices=[f for f in fold_spoke_indices if f>0]
# 	print("this folding:")
# 	print(len(this_folding),this_folding)
	for r in fold_spoke_indices:
	
# 		print("---")
		this_spoke_name=spokes_by_index[r]
	
# 		print("this spoke",r,this_spoke_name)
	
		subsequent_spoke_idxs=fold_spoke_indices[r:]
	
# 		print("subsequent spokes",[(r2,spokes_by_index[r2]) for r2 in subsequent_spoke_idxs])
	
		affected_nodes=[]
	
		rna=G.nodes[this_spoke_name[0]]
		rnb=G.nodes[this_spoke_name[1]]
	
		rotation_axis=Line3D(
			Point3D(rna['pos']),
			Point3D(rnb['pos'])
		)
	
# 		print("rotation axis",r,this_spoke_name[0],this_spoke_name[1],rotation_axis)
	
		sign=this_folding[fold_spoke_indices.index(r)]
	
		these_affected_nodes=[]
		for node_idx in nodes_by_index:
			
			if node_idx > r:
				these_affected_nodes+=[n_id for n_id in nodes_by_index[node_idx]]
# 		print("affected nodes:",these_affected_nodes)

		for n_id in these_affected_nodes:
			
			n=G.nodes[n_id]
			affected_point=Point3D(n['pos'])
			affected_point_post_rotation=rotate(rotation_axis,affected_point,angle*sign)
		
			G.nodes[n_id]['pos']=(
				affected_point_post_rotation.x,
				affected_point_post_rotation.y,
				affected_point_post_rotation.z
			)
# 			if angle!=0:
# 				illustrator.draw_graph(G)
	return G