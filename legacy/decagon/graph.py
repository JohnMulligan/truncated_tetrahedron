import plotly.graph_objects as go
from sympy.geometry import Point,Point3D, Line3D,Plane,Segment3D

def main(a,triangles,pointstr='ABCDEFGHIJKLMNOPQ'):
	pa=[i for i in pointstr.split('|')[0]]
	try:
		pb=[i+'i' for i in pointstr.split('|')[1].split('i') if i!='']
		p=pa+pb
	except:
		p=pa
	X=[float(a[i].x.evalf()) for i in p]
	Y=[float(a[i].y.evalf()) for i in p]
	Z=[float(a[i].z.evalf()) for i in p]
	
	I=[p.index(i[0]) for i in triangles]
	J=[p.index(i[1]) for i in triangles]
	K=[p.index(i[2]) for i in triangles]
	
	labels=[i for i in p]
	
	fig = go.Figure(data=[
		go.Mesh3d(
			x=X,
			y=Y,
			z=Z,
			i=I,
			j=J,
			k=K,
			text=labels,
			showscale=True
		)
	])
	fig.show()
	#wait = input("Press Enter for next step.")