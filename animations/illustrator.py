import numpy as np
import json
import re
import os 
# import matplotlib.pyplot as plt

def make_facia(G):
	
	facia=[]
	
	outernodes = {x:y['index'] for x,y in G.nodes(data=True) if y['set']=='outer'}
	
	outernodes_sorted={k: v for k, v in sorted(outernodes.items(), key=lambda item: item[1])}
	
	outernode_labels_sorted=list(outernodes_sorted.keys())
	
	for n_id in outernode_labels_sorted[:-1]:
		this_surface=[n_id]
# 		print('---')
		n_idx=outernodes[n_id]
# 		print(n_id)
		g_adj=G.adj[n_id].items()
		
		for item in g_adj:
# 			print(item)
			neighbor_id=item[0]
			if G.nodes[neighbor_id]['index']>n_idx:
				this_surface.append(neighbor_id)
				for next_neighbor in G.adj[neighbor_id].items():
					if G.nodes[next_neighbor[0]]['set']=='inner':
						this_surface.append(next_neighbor[0])
			if G.nodes[item[0]]['set']=="inner":
				this_surface.append(neighbor_id)
		this_surface=list(set(this_surface))
		this_surface.sort()
		facia.append(this_surface)
	
	for f in facia:
		print(f)

	return facia

def draw_faces(G,N):
	basedirpath='outputs/'
	os.makedirs(basedirpath+'%s/' %str(N), exist_ok=True)

	facia=make_facia(G)
	
	triangle_block_text_lines=[]
	for s in facia:
		triangle_block_text_lines.append("beginShape();")
		for v in s:
			triangle_block_text_lines.append("vertex(%s_x[t],%s_y[t],%s_z[t]);" %(v,v,v))
		triangle_block_text_lines.append("endShape(CLOSE);")
	
	triangle_block="\n".join(triangle_block_text_lines)
	
	d=open(basedirpath+"%s/%s_faces.js" %(str(N),str(N)),'w')
	d.write(triangle_block)
	d.close()



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

def make_processing_animation(fname):
	
	ints=[re.sub("\.json","",i) for i in fname.split("_")]
	
	print("-->",ints)
	
	N,np_id,max_angle=ints
	
	basedirpath='outputs/'
	os.makedirs(basedirpath+'%s/' %str(N), exist_ok=True)

	d=open("animationblock.txt","r")
	t=d.read()
	
	animation_template=t
	
	d.close()

	d=open(basedirpath+ "%s/%s" %(str(N),fname),"r")
	t=d.read()
	d.close()
	
	j=json.loads(t)
	vertices=j

	d=open(basedirpath+ "%s/%s_faces.js" %(str(N),str(N)),'r')
	facia_block=d.read()
	d.close()
		
	verticesarray=[]
	
	stepcount=None
	
	for v_id in vertices:
		v_pos=vertices[v_id]
		stepcount=len(v_pos)
		v_x=[v[0] for v in v_pos]
		v_y=[v[1] for v in v_pos]
		v_z=[v[2] for v in v_pos]
		
		for v in [['x',v_x],['y',v_y],['z',v_z]]:
			label,positions=v
			vstr="let %s_%s=%s;" %(v_id,label,str(positions))
			verticesarray.append(vstr)
	
	verticesblock="\n".join(verticesarray)
	
	l=list(range(stepcount))
	l2=l.copy()
	l2.reverse()
	l2=l2[1:-1]
	l+=l2
	
	# let qz=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7.10542735760100e-15, 5.99663610211028e-15, 3.96090706465646e-15, 1.68143784854474e-15, 2.60119342575891e-16, 197.514870584543, 530.900814607706, 701.342803333195, 216.145802862731, -631.718466211573, -463.444955608968, -32.5484001794068, 588.720630085246, 758.110791324301, -173.946115986103];
	
	steparrayblock="let steparray=%s;\nlet t=steparray[sec" %(str(l))
	steparrayblock+="%" + str(len(l)) + "];"

	animation_text=re.sub("___VERTICES___",verticesblock,animation_template)
	animation_text=re.sub("___STEPARRAY___",steparrayblock,animation_text)	
	animation_text=re.sub("___FACIABLOCK___",facia_block,animation_text)


	friendly_fname=re.sub("\.json","",fname)
	friendly_fname=re.sub("\.","_",friendly_fname)
	final_text="function p_%s(){\n%s}" %(friendly_fname,animation_text)
	

	d=open(basedirpath+"%s/processing_%s" %(str(N),re.sub("\.json",".js",fname)),"w")
	d.write(final_text)
	d.close()
	
if __name__=="__main__":
	make_processing_animation(fname="12_0_10_A__G*A__M*B_C__H_I*B__H*C__I*D_E__J_K*D__J*E__K*F_G__first*F_G__last*F__L*G__A*G__M*H_I__B_C*H__B*I__C*J_K__D_E*J__D*K__E*L__F*M__A*M__G*first__F_G*last__F_G.json")