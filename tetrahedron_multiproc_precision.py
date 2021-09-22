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

	def graph(triangles,pointstr='ABCDEFGHIJKLMNOPQRST'):
		pa=[i for i in pointstr.split('|')[0]]
		try:
			pb=[i+'i' for i in pointstr.split('|')[1].split('i') if i!='']
			p=pa+pb
		except:
			p=pa
		print(p)
		points_array=[[a[i].x,a[i].y,a[i].z] for i in p]
		triangles_idx=[[p.index(i[0]),p.index(i[1]),p.index(i[2])] for i in triangles]
		test = graphics.engine.Engine3D(points_array, triangles_idx, title='dodecagon')
		test.render()
		test.screen.window.mainloop()

	r=100000






	##############DODECAGON
	A,B,C,D,E,F,G,H,I,J,K,L=[Point3D(r*sin(i*pi/6),r*cos(i*pi/6),0) for i in range(12)]

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
		['A','S','M'],['A','M','B'],
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



	rotate_list('AR','B','M',magical_angle)

	#graph(triangles,'ABCDEFGHIJKLMNOPQRST')
	print(1)
	rotate_list('ARB','C','M',magical_angle)

	#graph(triangles)
	print(2)
	rotate_list('ARBMC','D','N',magical_angle)

	#graph(triangles)
	print(3)
	rotate_list('ARBCMD','N','E',-magical_angle)

	#graph(triangles)
	print(4)
	rotate_list('ARBMCDNE','O','F',-magical_angle)
	print(5)
	#graph(triangles)

	rotate_list('ARBMCDNEF','O','G',-magical_angle)
	print(6)
	#graph(triangles)

	rotate_list('ARBMCDNEFOG','P','H',magical_angle)
	print(7)
	#graph(triangles)

	rotate_list('ARBMCDNEFOGH','P','I',magical_angle)

	#graph(triangles)
	print(8)
	rotate_list('ARBMCDNEFOGHPI','J','Q',-magical_angle)

	#graph(triangles)
	print(9)

	rotate_list('ARBMCDNEFOGHPIJ','K','Q',-magical_angle)

	#graph(triangles)
	print(10)
	
	rotate_list('ARBMCDNEFOGHPIJKQ','L','R',-magical_angle)

	'''print("\n\n-------\nclose hits: A~G (T~G) | R~O (S~O) | M~P | B~H\n-------")
	for i in a:
		print("\n%s = %s\n" %(i,a[i].evalf()))
	#graph(triangles)'''
	
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
		
		for x in [prev_digit-1,prev_digit]:
			
			a=angle[:-1]+str(x)
			
			for i in range(10):
				b=str(Decimal(a+str(i)))
				batch.append(b)
				#print(N(a+str(i)),n))
		
		batch=[Float(i,n+2) for i in batch]
		#print(batch)
		
		with Pool(6) as p:
			distances=p.map(f,batch)
		print(distances)
		distances={i[0]:i[1] for i in distances}
		
				
		
		'''for b in batch:
			AT_distance,this_angle=f(b)
			distances[AT_distance]=this_angle
			print(distances)'''
				
		best_angle=distances[min(distances)]
		angle=str(best_angle)
		
	
		

	
	
	'''step=.000001
	domain=0.001
	angle=base_angle-domain
	work=[]
	while angle<base_angle+domain:
		work.append(angle)
		angle+=step
	
	with Pool(processes=10) as pool:
		pool.map(f,work)'''





'''





from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))'''