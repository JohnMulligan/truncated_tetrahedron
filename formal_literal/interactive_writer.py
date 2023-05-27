from math import cos, sin, sqrt, floor, pi
import sys
import os
import networkx as nx


N=int(sys.argv[1])

N=N+2

r=100000

alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

acycles=floor(N/len(alphabet))

outer_vertices=[]

G = nx.Graph()

#this will get us up to a 702-sided figure
buffer=''
idx=0
prev_v=None
for c in range(acycles+1):
	if c > 0:
		buffer=alphabet[c-1]
	if c == acycles:
		for a in alphabet[:N%len(alphabet)-1]:
			print('---')
			this_v=''.join([buffer,a])
			print("++",this_v)
			outer_vertices.append(this_v)
			G.add_node(this_v,set='outer',index=idx)
			print(G.nodes[this_v])
			if prev_v is not None:
				G.add_edge(prev_v,this_v,set='outer')
				print(G.edges([this_v]))
			prev_v=this_v
			print('---')
			idx+=1
	else:
		for a in alphabet:
			print('---')
			this_v=''.join([buffer,a])
			print(this_v)
			G.add_node(this_v,set='outer',index=idx)
			print(G.nodes[this_v])
			if prev_v is not None:
				G.add_edge(prev_v,this_v, set='outer')
				print(G.edges([this_v]))
			prev_v=this_v
			print('---')
			idx+=1

outernodeslist=[(n,G.nodes[n]['index']) for n in G.nodes]

print(outernodeslist)

innernodeslist=[
	"_".join(
		[
			outernodeslist[2*i][0],
			outernodeslist[(2*i)+1][0]
		]
	) for i in range(int((len(outernodeslist)-1)/2))
]

lastinnernode="_".join([outernodeslist[-2][0],outernodeslist[-1][0]])

innernodeslist.append(lastinnernode)

print(innernodeslist)

prev_v=None
for this_v in innernodeslist:
	
	print('---')
	G.add_node(this_v,set='inner')
	
	if prev_v is not None:
		G.add_edge(prev_v,this_v,set='inner')
	
	innernodeindices=[]
	
	for outernodename in this_v.split('_'):
		
		outernode=G.nodes[outernodename]
		
		G.add_edge(this_v,outernodename, set='spokes',index=outernode['index'])
		
		innernodeindices.append(outernode['index'])
	
		print(G.edges[this_v,outernodename])
		
	innernodeindex=min(innernodeindices)
	
	G.nodes[this_v]['index']=innernodeindex
	
	print(this_v,G.nodes[this_v])
	
	print('---')

for node in outernodeslist:
	
	node_id,node_idx=node
	
	print(node_idx,N,r,node_idx%N)
	
	node_x=r*cos(node_idx*pi/(N/2))*(node_idx%N)
	
	node_y=r*sin(node_idx*pi/(N/2))*(node_idx%N)
	
	G.nodes[node_id]['x']=node_x
	
	G.nodes[node_id]['y']=node_y
	
	G.nodes[node_id]['z']=0
	
	print(G.nodes[node_id])
