from graph import main as graph
from transforms import rotate
import math
from sympy.geometry import Point,Point3D, Line3D,Plane,Segment3D
from math import cos, sin, sqrt, pi
import sys
import os

global s

magical_angle=2.034443043
a={i:None for i in 'ABCDEFGHIJKLMNOPQ'}

def rotate_list(point_list,axisp1label,axisp2label,angle):
	axis=Line3D(a[axisp1label],a[axisp2label])
	if "i" in point_list:
		point_list=[i+'i' for i in point_list.split('i') if i!='']
	else:
		point_list=[i for i in point_list]
	
	for point_label in point_list:
		point=a[point_label]
		new_point=rotate(axis,point,angle)
		a[point_label]=new_point

r=300	

##############DECAGON
A,B,C,D,E,F,G,H,I,J=[Point3D(r*sin(i*math.pi/5),r*cos(i*math.pi/5),0) for i in range(10)]

points=[A,B,C,D,E,F,G,H,I,J]
s='ABCDEFGHIJ'
for i in range(len(s)):
	#print(i,points[i])
	a[s[i]]=points[i]

##############
a['K']=A
K=A

##############TRIANGLE CUTOUTS
intersections=[[[A,D],[C,F]],[[C,F],[E,H]],[[E,H],[G,J]],[[G,J],[I,B]],[[I,B],[K,D]]]
intersecting_lines=[[Line3D(i[0][0],i[0][1]),Line3D(i[1][0],i[1][1])] for i in intersections]

M,N,O,P,L=[i[0].intersection(i[1])[0] for i in intersecting_lines]

points=[L,M,N,O,P]
s='LMNOP'
for i in range(len(s)):
	#print(i,points[i])
	a[s[i]]=points[i]


s='ABCDEFGHIJKLMNOPQ'

Q=L
a['Q']=L


for p in a:
	print(p,a[p])

##############FOLDING

triangles=[
	['A','B','L'],
	['B','L','M'],['B','C','M'],
	['C','D','M'],
	['D','M','N'],['D','E','N'],
	['E','N','F'],
	['N','F','O'],['F','O','G'],
	['G','H','O'],
	['H','O','P'],['H','P','I'],
	['P','I','J'],
	['J','P','Q'],['J','Q','K']
	]

steps_dict={i+j:[] for j in 'xyz' for i in s}
def updatesteps(steps_dict,a):
	for v in s:
		vx=(a[v].x).evalf()
		vy=(a[v].y).evalf()
		vz=(a[v].z).evalf()
		
		steps_dict[v+'x'].append(vx)
		steps_dict[v+'y'].append(vy)
		steps_dict[v+'z'].append(vz)
	
	return steps_dict

# beginShape();
# vertex(lx[t],ly[t],lz[t]);
# vertex(sx[t],sy[t],sz[t]);
# vertex(tx[t],ty[t],tz[t]);
# endShape(CLOSE);

for t in triangles:
	print("beginShape()")
	for v in t:
		print("vertex("+','.join([v.lower()+i+'[t]' for i in 'xyz'])+');')
	print('endShape(CLOSE);')
	
steps_dict=updatesteps(steps_dict,a)
graph(a,triangles)

steps=[
	('A','B','L',magical_angle),
	('ABL','C','M',magical_angle),
	('ABLC','D','M',magical_angle),
	('ABLCMD','E','N',-magical_angle),
	('ABLCMDE','F','N',-magical_angle),
	('ABLCMDENF','G','O',-magical_angle),
	('KQJPI','H','O',pi+magical_angle),
	('KQJ','I','P',magical_angle),
	('KQ','J','P',magical_angle),
]

for step in steps:
	pointlist,r0,r1,angle=step
	rotate_list(pointlist,r0,r1,angle)
	#graph(a,triangles)
	steps_dict=updatesteps(steps_dict,a)

for v in steps_dict:
	print("float[] " + v.lower() + " = {" + ", ".join([str(i) for i in steps_dict[v]]) + "};")	