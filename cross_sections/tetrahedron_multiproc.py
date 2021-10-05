from transforms import rotate
from sympy.geometry import Point,Point3D, Line3D,Plane,Segment3D
from sympy import cos, sin, sqrt,pi,N,Float
import sys
import os
import math
import time
from decimal import Decimal
from env import *

vertices={i:None for i in 'ABCDEFGHIJKLMN'}

def rotate_list(point_list,axisp1label,axisp2label,angle):
	axis=Line3D(vertices[axisp1label],vertices[axisp2label])
	if "i" in point_list:
		point_list=[i+'i' for i in point_list.split('i') if i!='']
	else:
		point_list=[i for i in point_list]
	for point_label in point_list:
		point=vertices[point_label]
		new_point=rotate(axis,point,angle)
		vertices[point_label]=new_point

def main(angle):
	p_id=os.getpid()
	start_time=time.time()
	
	d=open(os.path.join(outdir,str(p_id)+'.txt'),'a')
	
	ll=float(100000)
	r=float(30)

	y_offset=sin(math.pi/float(3))*r
	x_offsets=cos(math.pi/float(3))*r

	ls=ll-x_offsets*float(2)

	sl=ls

	ss=sl-x_offsets*float(2)
	
	##############ALTERNATING TRAPEZOIDS w 60 AND 120 DEGREE INTERIOR ANGLES
	####SHORT SIDE ON ONE IS THE LONG SIDE ON THE OTHER

	top_vs='ABCDEFG'


	for v in top_vs:
		n=top_vs.index(v)
		if n!=float(0):
			previous_offset=vertices[top_vs[n-1]].x
			print(type(previous_offset))
			x=[ss,ll][n%2]+previous_offset
		else:
			x=float(0)
	
		vertices[v]=Point3D(x,float(0),float(0))
	
	bottom_vs='HIJKLMN'
	for v in bottom_vs:
		n=bottom_vs.index(v)
		if n==0:
			x=x_offsets
		else:
			previous_offset=vertices[bottom_vs[n-1]].x
			x=previous_offset+[sl,ls][n%2]
		vertices[v]=Point3D(x,-y_offset,float(0))


	triangles=[	['A','B','H'],['H','I','B'],['B','I','C'],['C','I','J'],
				['C','J','K'],['C','D','K'],['D','E','L'],['D','K','L'],
				['E','L','F'],['F','L','M'],['F','M','G'],['G','M','N']
			]
	
	print(vertices)
	
	rotate_list('CDEFGJKLMN','B','I',angle)
	rotate_list('DEFGKLMN','C','J',angle)
	rotate_list('EFGLMN','D','K',angle)
	rotate_list('FGMN','E','L',angle)
	rotate_list('GN','F','M',angle)
	
	d.write("RADIUS: "+str(r)+"\n")
	d.write("ANGLE: "+str(angle)+"\n")
	statstr=''
	for pair in [['A','G'],['H','N']]:
		i,j=pair
		statstr+='\t'.join([str(i),str(j),str(vertices[i].distance(vertices[j]).evalf()),'\n'])
	d.write(statstr)
	d.write('\t'.join(["LOOP:", str(p_id),str(time.time()-start_time)]))
	d.close()
	AG_distance=str(vertices['A'].distance(vertices['G']).evalf())
	#print(AG_distance,angle)
	return AG_distance,angle

