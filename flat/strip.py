from graph import main as graph
import math
from sympy.geometry import Point,Point3D, Line3D,Plane,Segment3D
from math import cos, sin, sqrt,asin,tan,radians
import sys
import os

#magical_angle=1.2309594173409
magical_angle=(asin(sqrt(3)/3)*2)

vertices={i:None for i in 'ABCDEFGHIJKLMN'}

ll=10000
r=3000000

y_offset=sin(math.pi/3)*r
x_offsets=cos(math.pi/3)*r

ls=ll-x_offsets*2

sl=ls

ss=sl-x_offsets*2


##############ALTERNATING TRAPEZOIDS w 60 AND 120 DEGREE INTERIOR ANGLES
####SHORT SIDE ON ONE IS THE LONG SIDE ON THE OTHER

top_vs='ABCDEFG'


for v in top_vs:
	n=top_vs.index(v)
	if n!=0:
		previous_offset=vertices[top_vs[n-1]].x
		x=[ss,ll][n%2]+previous_offset
	else:
		x=0
	
	vertices[v]=Point3D(x,0,0)

bottom_vs='HIJKLMN'

for v in bottom_vs:
	n=bottom_vs.index(v)
	if n==0:
		x=x_offsets
	else:
		previous_offset=vertices[bottom_vs[n-1]].x
		x=previous_offset+[sl,ls][n%2]
	vertices[v]=Point3D(x,-y_offset,0)

#triangles=[	['A','B','H'],['H','I','B'],['B','I','C'],['C','I','J'],
#			['C','J','K'],['C','D','K'],['D','E','L'],['D','K','L'],
#			['E','L','F'],['F','L','M'],['F','M','G'],['G','M','N']
#		]

triangles=[
	['A','B','H'],['H','I','B'],
	['B','I','C'],['C','I','J']
]

#graph(vertices,triangles,''.join([i for i in vertices]))

A=vertices['A']
B=vertices['B']
C=vertices['C']
H=vertices['H']
I=vertices['I']
J=vertices['J']


def findlength(pointa,pointb):
	
	x1=pointa.x
	x2=pointb.x
	y1=pointa.y
	y2=pointb.y
	
	l=sqrt((x2-x1)**2+(y2-y1)**2)
	return l
	

print("-----------\nAB (small trap short side)")
AB=findlength(A,B)
print("length",AB)

print("-----------\nBC (large trap long side)")
BC=findlength(B,C)
print("length",BC)

print("-----------\nHI (small trap long side)")
HI=findlength(H,I)
print("length",HI)

print("-----------\nIJ (large trap short side)")
IJ=findlength(I,J)
print("length",IJ)

print("-----------\nCJ (shared diagonal sides)")
CJ=findlength(C,J)
print("length",CJ)


###
print("\n+++++NOW SOME RATIOS+++++")

height=A.y-H.y
print("height",height.evalf())

print("BC==IJ+2*(tan(30)*height)")
print(BC,IJ+2*(tan(radians(30))*height))

print("CJ==height/cos(30)")
print(CJ,height/cos(radians(30)))

print("CJ==height/cos(30)")
print(CJ,height/cos(radians(30)))

print("AB==-HI+2*height/tan(60)")
print(AB,-HI+2*height/tan(radians(60)))

