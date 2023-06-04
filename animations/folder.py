import json
import illustrator
from sympy.geometry import Point,Point3D, Line3D,Plane,Segment3D
from transforms import rotate

def main(G,this_folding,angle,fold_spoke_indices,nodes_by_index,spokes_by_index):
	print("-->",angle)
	for r in fold_spoke_indices:
	
# 			print("---")
		this_spoke_name=spokes_by_index[r]
	
# 			print("this spoke",r,this_spoke_name)
	
		subsequent_spoke_idxs=fold_spoke_indices[r:]
	
# 			print("subsequent spokes",[(r2,spokes_by_index[r2]) for r2 in subsequent_spoke_idxs])
	
		affected_nodes=[]
	
		rna=G.nodes[this_spoke_name[0]]
		rnb=G.nodes[this_spoke_name[1]]
	
		rotation_axis=Line3D(
			Point3D(rna['pos']),
			Point3D(rnb['pos'])
		)
	
# 			print("rotation axis",r,this_spoke_name[0],this_spoke_name[1],rotation_axis)
	
		these_affected_nodes=[]
	
		for node_idx in nodes_by_index:
			if node_idx > r:
# 					print(node_idx,nodes_by_index[node_idx],i[node_idx-2])
				these_affected_nodes+=[(n_id,this_folding[node_idx-2]) for n_id in nodes_by_index[node_idx]]
# 			print('---')
# 			print("affected nodes:")

		for n_t in these_affected_nodes:
			n_id,sign=n_t
			
			n=G.nodes[n_id]
			affected_point=Point3D(n['pos'])
			affected_point_post_rotation=rotate(rotation_axis,affected_point,angle*sign)
		
			G.nodes[n_id]['pos']=(
				affected_point_post_rotation.x,
				affected_point_post_rotation.y,
				affected_point_post_rotation.z
			)
	return G
