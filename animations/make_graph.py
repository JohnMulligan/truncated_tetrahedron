from math import cos, sin, sqrt, floor, pi
import sys
import os
import networkx as nx
from sympy.geometry import Point,Point3D, Line3D,Plane,Segment3D
# import matplotlib.pyplot as plt
import numpy as np

def main(N,r=1000):

	N=N

	alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	acycles=int(floor((N+2)/len(alphabet)))
# 	print(acycles)

	G = nx.Graph()

	#this will get us up to a 702-sided figure
	buffer=''
	idx=0
	prev_v=None
	for c in range(acycles+1):
# 		print("C=",c)
		if c > 0:
			buffer=alphabet[c-1]
		if c == acycles:
			leftoverlettersindex=(N+2)%len(alphabet)-1
# 			print("leftoverlettersindex",leftoverlettersindex)
			if leftoverlettersindex > 0:
				for a in alphabet[:leftoverlettersindex]:
# 					print('???')
					this_v=''.join([buffer,a])
# 					print("++",this_v)
					G.add_node(this_v,set='outer',index=idx)
# 					print(G.nodes[this_v])
					if prev_v is not None:
						G.add_edge(prev_v,this_v,set='outer',index=None)
# 						print(G.edges([this_v]))
					prev_v=this_v
# 					print('???')
					idx+=1
		else:
			for a in alphabet:
				if alphabet.index(a)<=N:
# 					print('---')
					this_v=''.join([buffer,a])
# 					print(this_v)
					G.add_node(this_v,set='outer',index=idx)
# 					print(G.nodes[this_v])
					if prev_v is not None:
						G.add_edge(prev_v,this_v, set='outer',index=None)
						print(G.edges([this_v]))
					prev_v=this_v
# 					print('---')
					idx+=1

	outernodeslist=[(n,G.nodes[n]['index']) for n in G.nodes]
	outervertexlabels=[v[0] for v in outernodeslist]

# 	print("outer nodes:",outernodeslist)

	innernodeslist=[
		"_".join(
			[
				outernodeslist[2*i-1][0],
				outernodeslist[(2*i)][0]
			]
		) for i in range(int((len(outernodeslist)-1)/2))
	]

	innernodeslist[0]="first"
	innernodeslist.append('last')
	
# 	print("inner nodes:",innernodeslist)

	prev_v=None

	spoke_indices=[]

	for this_v in innernodeslist:
	
# 		print('---')
		G.add_node(this_v,set='inner')
# 		print(this_v)
		if prev_v is not None:
	# 		print("-->",prev_v,this_v)
			G.add_edge(prev_v,this_v,set='inner',index=None)
	
		innernodeindices=[]
		if this_v not in ('first','last'):
			for outernodename in this_v.split('_'):
		
				outernode=G.nodes[outernodename]
		
				spoke_index=outernode['index']
				
				G.add_edge(this_v,outernodename, set='spokes',index=spoke_index)
		
				spoke_indices.append(spoke_index)
		
				innernodeindices.append(outernode['index'])
		
				prev_v=this_v
	
		# 		print(this_v,outernodename,G.edges[this_v,outernodename])
		
			innernodeindex=min(innernodeindices)
	
			G.nodes[this_v]['index']=innernodeindex
		elif this_v=='first':
			G.nodes[this_v]['index']=0
			G.add_edge('first',outervertexlabels[0],set='spokes',index=0)
		elif this_v=='last':
			G.nodes[this_v]
			G.add_edge('last',outervertexlabels[-2],set='spokes',index=None)
			G.add_edge('last',outervertexlabels[-1],set='spokes',index=None)

	G.nodes['last']['index']=max(spoke_indices)+1
	G.edges[('last'),outervertexlabels[-2]]['index']=max(spoke_indices)+1
	G.edges[('last'),outervertexlabels[-1]]['index']=max(spoke_indices)+2
	G.add_edge('first',innernodeslist[1],set='inner',index=None)

	for node in outernodeslist:
	
		node_id,node_idx=node
	
	# 	print(node_idx,N,r,node_idx%N)
	
		node_x=r*sin((node_idx%N)*pi/(N/2))
	
		node_y=r*cos((node_idx%N)*pi/(N/2))
		
		G.nodes[node_id]['pos']=(node_x,node_y,0)
		# 
# 		G.nodes[node_id]['x']=node_x
# 	
# 		G.nodes[node_id]['y']=node_y
# 	
# 		G.nodes[node_id]['z']=0
# 	
	# 	print(G.nodes[node_id])

	def node_xy(g,node_id):
		n=g.nodes[node_id]
	# 	print(n)
		return (n['x'],n['y'])

	for node_id in innernodeslist:
		if node_id not in ("first","last"):
			outer_a_label,outer_b_label=node_id.split("_")
		
			outer_a_counterpart_idx=(outervertexlabels.index(outer_a_label)+3)%len(outervertexlabels)
		
	# 		print(node_id,outer_a_counterpart_idx)
		
			if outer_a_counterpart_idx==1:
				outer_a_counterpart_idx=2
		
			outer_a_counterpart_label=outervertexlabels[outer_a_counterpart_idx]
		
			outer_b_counterpart_idx=(outervertexlabels.index(outer_a_label)-2)
		
			if outer_b_counterpart_idx==-1:
				outer_b_counterpart_idx=-2
			
			outer_b_counterpart_label=outervertexlabels[outer_b_counterpart_idx]
		
			outer_a=G.nodes[outer_a_label]
		
			outer_b=G.nodes[outer_b_label]
		
			outer_a_counterpart=G.nodes[outer_a_counterpart_label]
		
			outer_b_counterpart=G.nodes[outer_b_counterpart_label]
		
		else:
		
			outer_a_counterpart_label=outervertexlabels[+2]
		
			outer_a_counterpart=G.nodes[outer_a_counterpart_label]
		
			outer_b_counterpart_label=outervertexlabels[-4]
		
			outer_b_counterpart=G.nodes[outer_b_counterpart_label]
		
			outer_a_label=outervertexlabels[-2]
		
			outer_a=G.nodes[outer_a_label]
		
			outer_b_label=outervertexlabels[0]
		
			outer_b=G.nodes[outer_b_label]
		
	
	# 	print(node_id,outer_a_label,outer_a_counterpart_label,outer_b_label,outer_b_counterpart_label)
		
		A_Ac=Line3D(
			Point3D(outer_a['pos'][0],outer_a['pos'][1]),
			Point3D(outer_a_counterpart['pos'][0],outer_a_counterpart['pos'][1])
		)
	
		B_Bc=Line3D(
			Point3D(outer_b['pos'][0],outer_b['pos'][1]),
			Point3D(outer_b_counterpart['pos'][0],outer_b_counterpart['pos'][1])
		)
	
		np=A_Ac.intersection(B_Bc)[0]
		
		G.nodes[node_id]['pos']=(np.x,np.y,0)
# 		
# 		G.nodes[node_id]['x']=node_point[0].x
# 		G.nodes[node_id]['y']=node_point[0].y
# 		G.nodes[node_id]['z']=node_point[0].z
		G.add_edge("last",innernodeslist[-2],set="inner")

	first_inner_node=G.nodes[innernodeslist[0]]
	for i in [0,1,2]:
		G.nodes['last']['pos']=first_inner_node['pos']
	
	return G
	

def draw_graph(G):
	fig = plt.figure()
	ax = fig.add_subplot(111, projection="3d")

	node_xyz = np.array([G.nodes[v]['pos'] for v in sorted(G)])
	edge_xyz = np.array([
		(
			G.nodes[u]['pos'],
			G.nodes[v]['pos']
		) for u, v in G.edges()
	])

	ax.scatter(*node_xyz.T, s=100, ec="w")

	for vizedge in edge_xyz:
		ax.plot(*vizedge.T, color="tab:gray")
	
	def _format_axes(ax):
		"""Visualization options for the 3D axes."""
		# Turn gridlines off
		ax.grid(False)
		# Suppress tick labels
		for dim in (ax.xaxis, ax.yaxis, ax.zaxis):
			dim.set_ticks([])
		# Set axes labels
		ax.set_xlabel("x")
		ax.set_ylabel("y")
		ax.set_zlabel("z")
	
	_format_axes(ax)
	fig.tight_layout()
	plt.show()

if __name__=="__main__":
	N=int(sys.argv[1])
	g=main(N)
# 	draw_graph(g)
