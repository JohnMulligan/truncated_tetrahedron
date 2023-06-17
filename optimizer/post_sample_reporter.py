from math import cos, sin, sqrt, floor, pi
import sys
import os
from itertools import product,islice
import time
import json



def main(N):
	
	ngon_outputfiles=[i for i in os.listdir('outputs/%s/' %N) if i.endswith('json')]
	
	angle_scores={}
	
	vertex_scores={}
	
	for ngon_outputfile in ngon_outputfiles:
		
		d=open('outputs/%s/%s' %(N,ngon_outputfile),'r')
		t=d.read()
		d.close()
		
		hits=json.loads(t)
		
		for hit in hits:
			joints=hit.split("*")
			vertices=[]
			for j in joints:
				u,v=j.split("__")
				for w in [u,v]:
					if w in vertex_scores:
						vertex_scores[w]+=1
					else:
						vertex_scores[w]=1
			
			angle=hits[hit]['angle']
			
			roundedangle=round(angle,5)
			if roundedangle in angle_scores:
				angle_scores[roundedangle]+=1
			else:
				angle_scores[roundedangle]=1
	
	for a in angle_scores:
		print(a,a*180/pi,angle_scores[a])
	for j in vertex_scores:
		print(j,vertex_scores[j])
	
if __name__=="__main__":
	N=int(sys.argv[1])
	main(N=N)
