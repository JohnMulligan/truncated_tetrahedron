from graph import main as graph
from transforms import rotate
import math
from sympy.geometry import Point,Point3D, Line3D,Plane,Segment3D
from math import cos, sin, sqrt, pi
import sys
import os

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
	'''s=[]
	for i in a:
		s.append(i+"x=" + str(a[i].x.evalf()))
		s.append(i+"y=" + str(a[i].y.evalf()))
		s.append(i+"z=" + str(a[i].z.evalf()))
	
	d=open('testoutput.py','w')
	d.write('\n'.join(s))
	d.close()'''

r=100






##############DODECAGON
A,B,C,D,E,F,G,H,I,J=[Point3D(r*sin(i*math.pi/5),r*cos(i*math.pi/5),0) for i in range(10)]

#triangles=[['A','B','D'],['C','D','F'],['E','F','H'],['G','H','J'],['I','J','L'],['K','L','B']]

points=[A,B,C,D,E,F,G,H,I,J]
s='ABCDEFGHIJ'
for i in range(len(s)):
	#print(i,points[i])
	a[s[i]]=points[i]



print(points)


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

#print(a,triangles,s)

#graph(a,triangles,s)
##############






##############FOLDING

#first, duplicate A and R so we can snip and fold



#then, test the full schmeer because we're going to want to be able to constantly test the look

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

graph(a,triangles)

rotate_list('A','B','L',magical_angle)
graph(a,triangles)

rotate_list('ABL','C','M',magical_angle)
graph(a,triangles)


rotate_list('ABLC','D','M',magical_angle)
graph(a,triangles)

rotate_list('ABLCMD','E','N',-magical_angle)
graph(a,triangles)

rotate_list('ABLCMDE','F','N',-magical_angle)
graph(a,triangles)

rotate_list('ABLCMDENF','G','O',-magical_angle)
graph(a,triangles)

rotate_list('KQJPI','H','O',pi+magical_angle)
graph(a,triangles)

rotate_list('KQJ','I','P',magical_angle)
graph(a,triangles)

rotate_list('KQ','J','P',magical_angle)
graph(a,triangles)

# print("FOUR")
# rotate_list('ABLCMD','N','E',magical_angle)
# graph(a,triangles)

