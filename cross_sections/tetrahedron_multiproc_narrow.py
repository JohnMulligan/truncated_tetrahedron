from transforms import rotate
from sympy.geometry import Point,Point3D, Line3D,Plane,Segment3D
from sympy import cos, sin, sqrt,pi,N,Float
import sys
import os
import math
from multiprocessing import Pool, TimeoutError
import time
from tetrahedron_multiproc import main as f
import random


if __name__ == '__main__':
	angle='1.2'
	
	for n in range(1,5):
		#print(angle)
		start_time=time.time()
		
		accuracy=len(angle.split('.')[1])
		pointone='0.'+''.join(['0' for i in range(accuracy)])+'1'
		
		
		base_angle= float(angle+'0')-float(pointone)
		end_angle=  float(angle+'9')+float(pointone)
		step=       float(pointone)
		
		angle=base_angle
		work=[]
		while angle<end_angle:
			work.append(angle)
			angle+=step
			angle=round(angle,accuracy+1)
		
		with Pool(6) as p:
			distances=p.map(f,work)
		distances={float(i[0]):i[1] for i in distances}
		
		for d in distances:
			print(d,distances[d])
		
		min_distance=min(distances)
		best_angle=distances[min_distance]
		loop_time=time.time()-start_time
		print("best angle is --> ",best_angle, " // with distance -->",min_distance, "in", int(loop_time),"seconds")
		
		angle=str(best_angle)'''