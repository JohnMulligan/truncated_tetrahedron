from transforms import rotate
from sympy.geometry import Point,Point3D, Line3D,Plane,Segment3D
from sympy import cos, sin, sqrt,pi,N,Float
import sys
import os
import math
from multiprocessing import Pool, TimeoutError
import time
from tetrahedron_multiproc import main as f
from decimal import Decimal



if __name__ == '__main__':
	angle='1.2'
	
	for n in range(1,50):
		start_time=time.time()
		
		prev_digit=int(angle[-1])
		
		batch=[]
		
		for x in [(prev_digit-1)%10,prev_digit,(prev_digit+1)%10]:
			
			a=angle[:-1]+str(x)
			
			for i in range(10):
				#print(a+str(i),type(a+str(i)))
				b=str(Decimal(a+str(i)))
				batch.append(b)
				#print(N(a+str(i)),n))
		
		batch=[Float(i,n+2) for i in batch]		
		with Pool(6) as p:
			distances=p.map(f,batch)
		distances={float(i[0]):i[1] for i in distances}
		
		min_distance=min(distances)
		best_angle=distances[min_distance]
		loop_time=time.time()-start_time
		print("best angle is --> ",best_angle, " // with distance -->",min_distance, "in", int(loop_time),"seconds")
		
		angle=str(best_angle)