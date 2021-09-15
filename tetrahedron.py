### Shark ###

import graphics.engine
from transforms import rotate
import math
from sympy.geometry import Point,Point3D, Line3D,Plane,Segment3D
from math import cos, sin, sqrt

#OUTER, DODECAGON VERTICES: ABCDEFGHIJKL + T
#INNER, HEXAGON VERTICES: MNOPQR + S 
# (S AND T ARE DUPLICATES OF R AND A, RESPECTIVELY)

a={i:None for i in 'ABCDEFGHIJKLMNOPQRST'}

def rotate_list(point_list,axisp1,axisp2,angle):
	for point_label in point_list:
		point=a[point_label]
		new_point=rotate(axisp1,axisp2,point,angle)
		a[point_label]=new_point

def graph(triangles,pointstr='ABCDEFGHIJKLMNOPQRST'):
	p=[i for i in pointstr]
	points_array=[[a[i].x,a[i].y,a[i].z] for i in p]
	triangles_idx=[[p.index(i[0]),p.index(i[1]),p.index(i[2])] for i in triangles]
	test = graphics.engine.Engine3D(points_array, triangles_idx, title='dodecagon')
	test.render()
	test.screen.window.mainloop()

r=3






##############DODECAGON
A,B,C,D,E,F,G,H,I,J,K,L=[Point3D(r*sin(i*math.pi/6),r*cos(i*math.pi/6),0) for i in range(12)]

triangles=[['A','B','D'],['C','D','F'],['E','F','H'],['G','H','J'],['I','J','L'],['K','L','B']]

points=[A,B,C,D,E,F,G,H,I,J,K,L]
s='ABCDEFGHIJKL'
for i in range(len(s)):
	#print(i,points[i])
	a[s[i]]=points[i]

#graph(triangles,s)
##############






##############TRIANGLE CUTOUTS
intersections=[[[L,C],[B,E]],[[B,E],[D,G]],[[D,G],[F,I]],[[F,I],[H,K]],[[H,K],[J,A]],[[J,A],[L,C]]]
intersecting_lines=[[Line3D(i[0][0],i[0][1]),Line3D(i[1][0],i[1][1])] for i in intersections]

M,N,O,P,Q,R=[i[0].intersection(i[1])[0] for i in intersecting_lines]

triangles=[['L','R','A'],['B','M','C'],['D','N','E'],['O','G','F'],['H','I','P'],['J','Q','K']]

points=[M,N,O,P,Q,R]
s='MNOPQR'
for i in range(len(s)):
	#print(i,points[i])
	a[s[i]]=points[i]

#graph(triangles,s)
##############






##############FOLDING

#first, duplicate A and R so we can snip and fold
a['S']=R
a['T']=A

#then, test the full schmeer because we're going to want to be able to constantly test the look

triangles=[
	['L','S','T'],
	['A','R','M'],['A','M','B'],
	['B','M','C'],
	['C','M','N'],['C','N','D'],
	['D','N','E'],
	['N','E','O'],['E','O','F'],
	['F','O','G'],
	['G','H','O'],['P','O','H'],
	['H','I','P'],
	['J','I','P'],['J','P','Q'],
	['J','Q','K'],
	['K','Q','S'],['K','L','S']	
	]

#graph(triangles,'ABCDEFGHIJKLMNOPQRST')

magical_angle=math.sqrt(2)

rotate_list('AR',B,M,magical_angle)

#graph(triangles,'ABCDEFGHIJKLMNOPQRST')

rotate_list('ARB',C,M,magical_angle)

#graph(triangles)

rotate_list('ARBMC',D,N,magical_angle)

#graph(triangles)

rotate_list('ARBCMD',N,E,-magical_angle)

#graph(triangles)

rotate_list('ARBMCDNE',O,F,-magical_angle)

#graph(triangles)

rotate_list('ARBMCDNEF',O,G,-magical_angle)

#graph(triangles)

rotate_list('ARBMCDNEFOG',P,H,magical_angle)

#graph(triangles)

rotate_list('ARBMCDNEFOGH',P,I,magical_angle)

#graph(triangles)

rotate_list('ARBMCDNEFOGHPI',J,Q,-magical_angle)

#graph(triangles)

rotate_list('ARBMCDNEFOGHPIJ',K,Q,-magical_angle)

#graph(triangles)

rotate_list('ARBMCDNEFOGHPIJKQ',L,R,-magical_angle)

print("\n\n-------\nclose hits: A~G (T~G) | R~O (S~O) | M~P | B~H\n-------")
for i in a:
	print("\n%s = %s\n" %(i,a[i].evalf()))
graph(triangles)


