from transforms import rotate
from sympy.geometry import Point,Point3D, Line3D,Plane,Segment3D
from sympy import cos, sin, sqrt,pi,N,Float
import sys
import os
from multiprocessing import Pool, TimeoutError
import time
from decimal import Decimal

#OUTER, DODECAGON VERTICES: ABCDEFGHIJKL + T
#INNER, HEXAGON VERTICES: MNOPQR + S 
# (S AND T ARE DUPLICATES OF R AND A, RESPECTIVELY)



###TRYING TO SEE IF THERE'S A BETTER ANGLE




def f(angle):
	start_time=time.time()
	#print(angle,type(angle))
	magical_angle=angle
	
	p_id=os.getpid()
	d=open(str(p_id)+'.txt','a')

	a={i:None for i in 'ABCDEFGHIJKLMNOPQRST'}

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

	r=100000






	##############DODECAGON
	A,B,C,D,E,F,G,H,I,J,K,L=[Point3D(r*sin(i*pi/6),r*cos(i*pi/6),0) for i in range(12)]

	triangles=[['A','B','D'],['C','D','F'],['E','F','H'],['G','H','J'],['I','J','L'],['K','L','B']]

	points=[A,B,C,D,E,F,G,H,I,J,K,L]
	s='ABCDEFGHIJKL'
	for i in range(len(s)):
		#print(i,points[i])
		a[s[i]]=points[i]

	
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

	



	rotate_list('AR','B','M',magical_angle)

	

	rotate_list('ARB','C','M',magical_angle)

	

	rotate_list('ARBMC','D','N',magical_angle)

	

	rotate_list('ARBCMD','N','E',-magical_angle)

	

	rotate_list('ARBMCDNE','O','F',-magical_angle)

	

	rotate_list('ARBMCDNEF','O','G',-magical_angle)

	

	rotate_list('ARBMCDNEFOG','P','H',magical_angle)

	

	rotate_list('ARBMCDNEFOGH','P','I',magical_angle)

	

	rotate_list('ARBMCDNEFOGHPI','J','Q',-magical_angle)

	

	rotate_list('ARBMCDNEFOGHPIJ','K','Q',-magical_angle)

	

	rotate_list('ARBMCDNEFOGHPIJKQ','L','R',-magical_angle)
	
	d.write("RADIUS: "+str(r)+"\n")
	d.write("ANGLE: "+str(angle)+"\n")
	statstr=''
	for pair in [['A','G'],['T','G'],['A','T'],['R','O'],['S','O'],['R','S'],['M','P'],['B','H']]:
		i,j=pair
		statstr+='\t'.join([str(i),str(j),str(a[i].distance(a[j]).evalf()),'\n'])
	d.write(statstr)
	loop_time=str(time.time()-start_time)
	d.write('\t'.join(["LOOP:", str(p_id),loop_time]))
	d.close()
	AT_distance=str(a['A'].distance(a['T']).evalf())
	return AT_distance,angle


def find_optimal():
	return()


if __name__ == '__main__':
	angle='1.415'
	
	for n in range(3,50):
		
		print(angle)
		
		prev_digit=int(angle[-1])
		
		batch=[]
		
		
		
		for x in [(prev_digit-1)%10,prev_digit]:
			
			a=angle[:-1]+str(x)
			
			for i in range(10):
				#print(a+str(i),type(a+str(i)))
				b=str(Decimal(a+str(i)))
				batch.append(b)
				#print(N(a+str(i)),n))
		
		batch=[Float(i,n+2) for i in batch]
		#print(batch)
		
		with Pool(6) as p:
			distances=p.map(f,batch)
		distances={float(i[0]):i[1] for i in distances}
		
		min_distance=min(distances)
		best_angle=distances[min_distance]
		
		print("best angle is --> ",best_angle)
		
		
		
		angle=str(best_angle)
		
	
		
