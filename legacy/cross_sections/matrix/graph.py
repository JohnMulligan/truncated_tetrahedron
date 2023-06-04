import plotly.graph_objects as go
import math
from math import cos, sin, sqrt,asin
from vars import *

def main(a,triangles,pointstr='ABCDEFGHIJKLMN'):
	pa=[i for i in pointstr.split('|')[0]]
	try:
		pb=[i+'i' for i in pointstr.split('|')[1].split('i') if i!='']
		p=pa+pb
	except:
		p=pa
	#print("!!!!!",p)
	
	#for i in p:
	#	print(i,a[i])
	
	try:
		X=[eval(a[i][0]) for i in p]
		Y=[eval(a[i][1]) for i in p]
		Z=[eval(a[i][2]) for i in p]
	
		I=[p.index(i[0]) for i in triangles]
		J=[p.index(i[1]) for i in triangles]
		K=[p.index(i[2]) for i in triangles]
	except:
		X=[a[i][0] for i in p]
		Y=[a[i][1] for i in p]
		Z=[a[i][2] for i in p]
	
		I=[p.index(i[0]) for i in triangles]
		J=[p.index(i[1]) for i in triangles]
		K=[p.index(i[2]) for i in triangles]
	
	#triangles_idx=[[p.index(i[0]),p.index(i[1]),p.index(i[2])] for i in triangles]
	
	#intensities=[1 for i in range(len(X))]
	
	fig = go.Figure(data=[
		go.Mesh3d(
			x=X,
			y=Y,
			z=Z,
			i=I,
			j=J,
			k=K,
			name='y',
			showscale=True,
			colorbar_exponentformat="e"
		)
	])
	#print(fig)
	fig.show()
	wait = input("Press Enter for next step.")