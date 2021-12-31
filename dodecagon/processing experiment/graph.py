import plotly.graph_objects as go
from sympy.geometry import Point,Point3D, Line3D,Plane,Segment3D

def main(a,triangles,pointstr='ABCDEFGHIJKLMNOPQRST'):
	pa=[i for i in pointstr.split('|')[0]]
	try:
		pb=[i+'i' for i in pointstr.split('|')[1].split('i') if i!='']
		p=pa+pb
	except:
		p=pa
	#print(p)
	X=[float(a[i].x.evalf()) for i in p]
	Y=[float(a[i].y.evalf()) for i in p]
	Z=[float(a[i].z.evalf()) for i in p]
	
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
			showscale=True
		)
	])
	
	
	d=open('steps.txt','a')
	
	for i in range(len(X)):
		l='\t'.join([str(j) for j in [p[i],X[i],Y[i],Z[i]]])
		d.write(l)
		d.write('\n')
	d.close()
	
	
	
	
	
	#fig.show()
	#wait = input("Press Enter for next step.")