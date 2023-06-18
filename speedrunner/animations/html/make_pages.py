from operator import itemgetter
import os
import re
import plotly.graph_objects as go
import numpy as np
import json
import sys
import csv

def readtxtfile(filepath):
	d=open(filepath)
	t=d.read()
	d.close()
	return(t)

def main(N):
	N=int(N)
	
	outputfile='../../nots/outputs/%d/consolidated.txt' %N
	
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
	
	
	d=open('html_template.txt','r')
	html_template=d.read()
	d.close()
	
	htmlscriptblocklines=[]
	processingscriptblocklines=[]
	
	with open('%d.csv' %N, 'w', newline='') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',',
								quotechar='|', quoting=csv.QUOTE_MINIMAL)
		headers=['x1','y1','z1','x2','y2','z2']
		spamwriter.writerow(headers)
		
		for xyz in sortedxyz:
			
			x,y,z=[str(i) for i in xyz]
			print(x,y,z)
# 		1.41547199,22,8,,,
			
			if os.path.exists('../outputs/%s/processing_%s_%s_%s.js' %(N,N,y,x)):
				xyzbuffered=xyz+[None,None,None]
				htmlscriptblocklines.append('<script src="../outputs/%s/processing_%s_%s_%s.js"></script>' %(N,N,y,x))
				jsfriendlyname=re.sub("\.","_",x)
				pfilename='p_%s_%s_%s' %(N,y,jsfriendlyname)
				processingscriptname="if(sketchname == '%s') {%s();}" %(pfilename,pfilename)
				processingscriptblocklines.append(processingscriptname)
				exampleprocessingscriptname=pfilename
			else:
				xyzbuffered=[None,None,None]+xyz
			spamwriter.writerow(xyzbuffered)
			
			
			
			
	htmlscriptblock="\n".join(htmlscriptblocklines)
	
	
	html=re.sub("____processing_scripts_block____",htmlscriptblock,html_template)
	html_appendix="<script src='scatterplot_%s.js'></script>\n<script src='processinganimation_%s.js'></script>\n</html>" %(N,N)
	html+=html_appendix
	
	d=open("%s.html" %N,'w')
	d.write(html)
	d.close()
	
	d=open("processinganimation_template.txt",'r')
	js_template=d.read()
	d.close()
	
	jsblock="\n".join(processingscriptblocklines)
	js=re.sub('____sketches____',jsblock,js_template)
	js=re.sub('____sketchnumberone____',exampleprocessingscriptname,js)
	
	d=open("processinganimation_%s.js" %N,'w')
	d.write(js)
	d.close()
	
	d=open("scatterplot_template.txt",'r')
	scatterplot_template=d.read()
	d.close()
	
	scatterplot=re.sub('____csv_uri____','https://raw.githubusercontent.com/JohnMulligan/dihedral_public/main/%s.csv' %N,scatterplot_template)
	scatterplot=re.sub("____var_n____","var N='%s'" %N,scatterplot)
	
	d=open("scatterplot_%s.js" %N,"w")
	d.write(scatterplot)
	d.close()
	
	
	
	##there's got. to. be. a. better. way!
	## (i need a partner who can use javascript)
	
		
if __name__=="__main__":
	N=int(sys.argv[1])
	main(N)
