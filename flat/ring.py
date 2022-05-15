#from graph import main as graph
import math
from sympy.geometry import Point,Point, Line,Plane,Segment
from math import cos, sin, sqrt,acos,asin,radians
import sys
import os

#OUTER, DODECAGON VERTICES: ABCDEFGHIJKL + T
#INNER, HEXAGON VERTICES: MNOPQR + S 
# (S AND T ARE DUPLICATES OF R AND A, RESPECTIVELY)

r=100
a={i:None for i in 'ABCDEFGHIJKLMNOPQRST'}

##############DODECAGON

A,B,C,D,E,F,G,H,I,J,K,L=[Point(r*sin(i*math.pi/6),r*cos(i*math.pi/6)) for i in range(12)]

triangles=[['A','B','D'],['C','D','F'],['E','F','H'],['G','H','J'],['I','J','L'],['K','L','B']]

points=[A,B,C,D,E,F,G,H,I,J,K,L]
s='ABCDEFGHIJKL'
for i in range(len(s)):
	#print(i,points[i])
	a[s[i]]=points[i]

##############TRIANGLE CUTOUTS
intersections=[[[L,C],[B,E]],[[B,E],[D,G]],[[D,G],[F,I]],[[F,I],[H,K]],[[H,K],[J,A]],[[J,A],[L,C]]]
intersecting_lines=[[Line(i[0][0],i[0][1]),Line(i[1][0],i[1][1])] for i in intersections]

M,N,O,P,Q,R=[i[0].intersection(i[1])[0] for i in intersecting_lines]

points=[M,N,O,P,Q,R]
s='MNOPQR'
for i in range(len(s)):
	#print(i,points[i])
	a[s[i]]=points[i]

s='ABCDEFGHIJKLMNOPQR'

a['S']=R
a['T']=A

triangles=[
	['L','R','A'],
	['A','R','M'],['A','M','B'],
	['B','M','C']
	]

#graph(a,triangles,'ABCDEFGHIJKLMNOPQRST')

def findlength(pointa,pointb):
	
	x1=pointa.x
	x2=pointb.x
	y1=pointa.y
	y2=pointb.y
	
	l=sqrt((x2-x1)**2+(y2-y1)**2)
	return l
	

print("-----------\nLC (equal sides of triangle)")
LC=findlength(L,C)
print("length",LC)

print("-----------\nLA (equal sides of triangle)")
LA=findlength(L,A)
print("length",LA)

print("-----------\nLR (equal sides of triangle)")
LR=findlength(L,R)
print("length",LR)

print("-----------\nAB (equal sides of triangle)")
AB=findlength(A,B)
print("length",AB)

print("-----------\nRM (equal sides of triangle)")
RM=findlength(R,M)
print("length",RM)

print("-----------\nRA (equal sides of triangle)")
RA=findlength(R,A)
print("length",RA)

print("-----------\nBM (equal sides of triangle)")
BM=findlength(B,M)
print("length",BM)

print("-----------\nMC (equal sides of triangle)")
MC=findlength(M,C)
print("length",MC)

print("-----------\nBC (equal sides of triangle)")
BC=findlength(B,C)
print("length",BC)

###
print("\n+++++NOW SOME RATIOS+++++")


print("AB==LR*sin(120)/sin(30)")
print(AB,LR*sin(radians(120))/sin(radians(30)))

print("RM==AB+2*RA*sin(30)")
print(RM,AB+2*RA*sin(radians(30)))

print("RM==RA*(sin(120)/sin(30)+2*sin(30))")
print(RM,RA*(sin(radians(120))/sin(radians(30))+2*sin(radians(30))))

print("RA==AB*sin(30)/sin(120)")
print(RA,AB*sin(radians(30))/sin(radians(120)))


