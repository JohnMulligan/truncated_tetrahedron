import os
import plotly.graph_objects as go
import numpy as np
import json
import sys

def readtxtfile(filepath):
	d=open(filepath)
	t=d.read()
	d.close()
	return(t)

def main(N):
	N=int(N)
	
	outputfile='../nots/outputs/%d/consolidated.txt' %N
	
	consolidated=readtxtfile(outputfile)
	
	consolidatedlines=[c for c in consolidated.split('\n\n') if c!='']
	
	angles=[]
	hits=[]
	np_ids=[]
	
	for line in consolidatedlines:
		j=json.loads(line)
		this_folding_np_id=j['this_folding_np_id']
		close_neighborings_count=j['close_neighborings_count']
		angle=j['angle']
		angles.append(angle)
		hits.append(close_neighborings_count)
		n,np_id=[int(i) for i in this_folding_np_id.split('_')]
		np_ids.append(np_id)

	fig = go.Figure(data=[go.Scatter3d(x=angles, y=np_ids, z=hits,
									   mode='markers')])
	

	fig.update_layout(scene = dict(
		xaxis_title="angle",
		yaxis_title="np_id",
		zaxis_title="hit count"
	))

	fig.show()

if __name__=="__main__":
	N=int(sys.argv[1])
	main(N)
