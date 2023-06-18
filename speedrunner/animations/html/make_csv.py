from operator import itemgetter
import os
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
	
	
	
	with open('%d.csv' %N, 'w', newline='') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',',
								quotechar='|', quoting=csv.QUOTE_MINIMAL)
		headers=['x1','y1','z1','x2','y2','z2']
		spamwriter.writerow(headers)
		
		for xyz in sortedxyz:
			
			x,y,z=xyz
# 		1.41547199,22,8,,,
			
			if os.path.exists('../outputs/%s/processing_%s_%s_%s.js' %(N,N,y,x)):
				xyzbuffered=xyz+[None,None,None]
			else:
				xyzbuffered=[None,None,None]+xyz
			spamwriter.writerow(xyzbuffered)
			
		
if __name__=="__main__":
	N=int(sys.argv[1])
	main(N)
