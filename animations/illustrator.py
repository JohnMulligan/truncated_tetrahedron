from operator import itemgetter
import csv
import plotly.graph_objects as go
import numpy as np
import json
import re
import os 
import shutil
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





def readtxtfile(filepath):
	d=open(filepath)
	t=d.read()
	d.close()
	return(t)
	
def makeextrafiles(N):

	N=int(N)
	
	outputfile='../optimizer/outputs/%d/consolidated.txt' %N
	
	consolidated=readtxtfile(outputfile)
	
	consolidatedlines=[c for c in consolidated.split('\n\n') if c!='']
	
	angles=[]
	hits=[]
	np_ids=[]
	
	xyzlist=[]
	
	for line in consolidatedlines:
		j=json.loads(line)
		this_folding_np_id=j['this_folding_np_id']
		close_neighborings_count=j['close_neighborings_count']
		angle=j['angle']
		angles.append(angle)
		hits.append(close_neighborings_count)
		n,np_id=[int(i) for i in this_folding_np_id.split('_')]
		xyzlist.append([angle,np_id,close_neighborings_count])

	sortedxyz=sorted(xyzlist, key=itemgetter(0))
	
	fig = go.Figure(data=[go.Scatter3d(x=angles, y=np_ids, z=hits,
									   mode='markers')])
	
	fig.update_layout(scene = dict(
		xaxis_title="angle",
		yaxis_title="np_id",
		zaxis_title="hit count"
	))
	
	
# 	d=open('html_template.txt','r')
# 	html_template=d.read()
# 	d.close()
# 	
# 	htmlscriptblocklines=[]
	processingscriptblocklines=[]
	
	shutil.copyfile(outputfile, '../../dihedral_flask/static/%d/consolidated.txt' %N)
	
# 	with open('../../dihedral_flask/static/%d/%d.csv' %(N,N), 'w', newline='') as csvfile:
# 		spamwriter = csv.writer(csvfile, delimiter=',',
# 								quotechar='|', quoting=csv.QUOTE_MINIMAL)
# 		headers=['x1','y1','z1','x2','y2','z2']
# 		spamwriter.writerow(headers)
# 		
	for xyz in sortedxyz:
		
		x,y,z=[str(i) for i in xyz]
		print(x,y,z)
# 		1.41547199,22,8,,,
		
		if os.path.exists('../../dihedral_flask/static/%s/processing_%s_%s_%s.js' %(N,N,y,x)):
			xyzbuffered=xyz+[None,None,None]
# 				htmlscriptblocklines.append('<script src="../outputs/%s/processing_%s_%s_%s.js"></script>' %(N,N,y,x))
			jsfriendlyname=re.sub("\.","_",x)
			pfilename='p_%s_%s_%s' %(N,y,jsfriendlyname)
			processingscriptname="if(sketchname == '%s') {%s();}" %(pfilename,pfilename)
			processingscriptblocklines.append(processingscriptname)
			exampleprocessingscriptname=pfilename
		else:
			xyzbuffered=[None,None,None]+xyz
# 			spamwriter.writerow(xyzbuffered)
			
			
			
			
# 	htmlscriptblock="\n".join(htmlscriptblocklines)
# 	
# 	
# 	html=re.sub("____processing_scripts_block____",htmlscriptblock,html_template)
# 	html_appendix="<script src='scatterplot_%s.js'></script>\n<script src='processinganimation_%s.js'></script>\n</html>" %(N,N)
# 	html+=html_appendix
	
# 	d=open("%s.html" %N,'w')
# 	d.write(html)
# 	d.close()
	
	d=open("html/processinganimation_template.txt",'r')
	js_template=d.read()
	d.close()
	
	jsblock="\n".join(processingscriptblocklines)
	js=re.sub('____sketches____',jsblock,js_template)
	js=re.sub('____sketchnumberone____',exampleprocessingscriptname,js)
	
	d=open("../../dihedral_flask/static/js/processinganimation_%s.js" %N,'w')
	d.write(js)
	d.close()
	
# 	d=open("scatterplot_template.txt",'r')
# 	scatterplot_template=d.read()
# 	d.close()
# 	
# 	scatterplot=re.sub('____csv_uri____','https://raw.githubusercontent.com/JohnMulligan/dihedral_public/main/%s.csv' %N,scatterplot_template)
# 	scatterplot=re.sub("____var_n____","var N='%s'" %N,scatterplot)
# 	
# 	d=open("scatterplot_%s.js" %N,"w")
# 	d.write(scatterplot)
# 	d.close()
	
	
	
	##there's got. to. be. a. better. way!
	## (i need a partner who can use javascript)




def make_processing_animation(fname):
	
	ints=[re.sub("\.json","",i) for i in fname.split("_")]
	
	print("-->",ints)
	
	N,np_id,max_angle=ints
	
	if os.path.exists('../../dihedral_flask/static/'):
		basedirpath_w=('../../dihedral_flask/static/')
		os.makedirs(basedirpath_w+'%s/' %str(N), exist_ok=True)
	else:
		basedirpath_w='outputs/'
	basedirpath_r='outputs/'
	os.makedirs(basedirpath_r+'%s/' %str(N), exist_ok=True)
	
	
	d=open("animationblock.txt","r")
	t=d.read()
	
	animation_template=t
	
	d.close()
	
	thisfname=basedirpath_r+ "%s/%s" %(str(N),fname)
	print(thisfname)

	d=open(thisfname,"r")
	t=d.read()
	d.close()
	
	j=json.loads(t)
	vertices=j

	d=open(basedirpath_r+ "%s/%s_faces.js" %(str(N),str(N)),'r')
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
	

	d=open(basedirpath_w+"%s/processing_%s" %(str(N),re.sub("\.json",".js",fname)),"w")
	d.write(final_text)
	d.close()
	
if __name__=="__main__":
	make_processing_animation(fname="12_0_10_A__G*A__M*B_C__H_I*B__H*C__I*D_E__J_K*D__J*E__K*F_G__first*F_G__last*F__L*G__A*G__M*H_I__B_C*H__B*I__C*J_K__D_E*J__D*K__E*L__F*M__A*M__G*first__F_G*last__F_G.json")