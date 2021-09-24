from graph import main as graph
from transforms import rotate
import math
from sympy.geometry import Point,Point3D, Line3D,Plane,Segment3D
from math import cos, sin, sqrt
import sys
import os

#OUTER, DODECAGON VERTICES: ABCDEFGHIJKL + T
#INNER, HEXAGON VERTICES: MNOPQR + S 
# (S AND T ARE DUPLICATES OF R AND A, RESPECTIVELY)






#magical_angle=166563979225162923748770640501998485171/117675500839377502664900100000000000000
#magical_angle=1.415652449
#magical_angle=1.4157
#magical_angle=1.41547207
magical_angle=1.415471989998
#magical_angle=1.4155
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

r=100000.00000






##############DODECAGON
A,B,C,D,E,F,G,H,I,J,K,L=[Point3D(r*sin(i*math.pi/6),r*cos(i*math.pi/6),0) for i in range(12)]

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

s='ABCDEFGHIJKLMNOPQR'

#print(a,triangles,s)

graph(a,triangles,s)
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

graph(a,triangles,'ABCDEFGHIJKLMNOPQRST')



rotate_list('AR','B','M',magical_angle)

graph(a,triangles,'ABCDEFGHIJKLMNOPQRST')

rotate_list('ARB','C','M',magical_angle)

graph(a,triangles)

rotate_list('ARBMC','D','N',magical_angle)

graph(a,triangles)

rotate_list('ARBCMD','N','E',-magical_angle)

graph(a,triangles)

rotate_list('ARBMCDNE','O','F',-magical_angle)

graph(a,triangles)

rotate_list('ARBMCDNEF','O','G',-magical_angle)

graph(a,triangles)

rotate_list('ARBMCDNEFOG','P','H',magical_angle)

graph(a,triangles)

rotate_list('ARBMCDNEFOGH','P','I',magical_angle)

graph(a,triangles)

rotate_list('ARBMCDNEFOGHPI','J','Q',-magical_angle)

graph(a,triangles)

rotate_list('ARBMCDNEFOGHPIJ','K','Q',-magical_angle)

graph(a,triangles)

rotate_list('ARBMCDNEFOGHPIJKQ','L','R',-magical_angle)

print("\n\n-------\nclose hits: A~G (T~G) | R~O (S~O) | M~P | B~H\n-------")


graph(a,triangles)



##### SECOND RING FORM -- I WAS TRYING TO MAKE THIS USING NORMALS OFF THE PLANES BUT THE NORMALS WERE BEING IMPROPERLY CALCULATED NO MATTER WHAT I DID


##### MATCH Pi TO R/S and Ii to L
Ai,Bi,Ci,Di,Ei,Fi,Gi,Hi,Ii,Ji,Ki,Li=[Point3D(r*sin(i*math.pi/6)-I.x+L.x,r*cos(i*math.pi/6)-I.y+L.y,0) for i in range(12)]


points2=[Ai,Bi,Ci,Di,Ei,Fi,Gi,Hi,Ii,Ji,Ki,Li]
s='ABCDEFGHIJKL'

for i in range(len(s)):
	#print(i,points[i])
	a[s[i]+'i']=points2[i]

intersections=[[[Li,Ci],[Bi,Ei]],[[Bi,Ei],[Di,Gi]],[[Di,Gi],[Fi,Ii]],[[Fi,Ii],[Hi,Ki]],[[Hi,Ki],[Ji,Ai]],[[Ji,Ai],[Li,Ci]]]
intersecting_lines=[[Line3D(i[0][0],i[0][1]),Line3D(i[1][0],i[1][1])] for i in intersections]

Mi,Ni,Oi,Pi,Qi,Ri=[i[0].intersection(i[1])[0] for i in intersecting_lines]


points=[Mi,Ni,Oi,Pi,Qi,Ri]
s='MNOPQR'
for i in range(len(s)):
	#print(i,points[i])
	a[s[i]+'i']=points[i]

##### BUT HERE WE HAVE TO SNIP THE TRIANGLE HALFWAY THROUGH BECAUSE WE'RE BASING OFF THE OTHER'S STARTING POINT


a['Si']=Qi
a['Ti']=Ki


triangles2=[
	['Ji','Si','Ti'],
	['Ai','Ri','Mi'],['Ai','Mi','Bi'],
	['Bi','Mi','Ci'],
	['Ci','Mi','Ni'],['Ci','Ni','Di'],
	['Di','Ni','Ei'],
	['Ni','Ei','Oi'],['Ei','Oi','Fi'],
	['Fi','Oi','Gi'],
	['Gi','Hi','Oi'],['Pi','Oi','Hi'],
	['Hi','Ii','Pi'],
	['Ji','Ii','Pi'],['Ji','Pi','Si'],
	['Li','Ai','Ri'],
	['Ki','Qi','Ri'],['Ki','Li','Ri']	
	]

##############


for pair in [['A','G'],['F','Hi'],['Pi','R'],['L','Ii']]:
	i,j=pair
	print(i,j,a[i].distance(a[j]).evalf())

rotate_list('AiBiCiDiEiFiGiHiIiJiKiLiMiNiOiPiQiRiSiTi','Ii','Pi',(math.pi/2-magical_angle)*2)

for pair in [['A','G'],['F','Hi'],['Pi','R'],['L','Ii']]:
	i,j=pair
	print(i,j,a[i].distance(a[j]).evalf())

graph(a,triangles+triangles2,'ABCDEFGHIJKLMNOPQRST|AiBiCiDiEiFiGiHiIiJiKiLiMiNiOiPiQiRiSiTi')


rotate_list(['Ji','Si','Ti'],'Ii','Pi',magical_angle)

graph(a,triangles+triangles2,'ABCDEFGHIJKLMNOPQRST|AiBiCiDiEiFiGiHiIiJiKiLiMiNiOiPiQiRiSiTi')


rotate_list(['Ti'],'Ji','Si',magical_angle)

graph(a,triangles+triangles2,'ABCDEFGHIJKLMNOPQRST|AiBiCiDiEiFiGiHiIiJiKiLiMiNiOiPiQiRiSiTi')


rotate_list(['Gi','Oi','Fi','Ni','Ei','Di','Ci','Mi','Bi','Ri','Ai','Li','Ki','Qi'],'Hi','Pi',-magical_angle)
graph(a,triangles+triangles2,'ABCDEFGHIJKLMNOPQRST|AiBiCiDiEiFiGiHiIiJiKiLiMiNiOiPiQiRiSiTi')

rotate_list(['Fi','Ni','Ei','Di','Ci','Mi','Bi','Ri','Ai','Li','Qi','Ki'],'Gi','Oi',-magical_angle)
graph(a,triangles+triangles2,'ABCDEFGHIJKLMNOPQRST|AiBiCiDiEiFiGiHiIiJiKiLiMiNiOiPiQiRiSiTi')

rotate_list(['Ni','Ei','Di','Ci','Mi','Bi','Ri','Ai','Li','Qi','Ki'],'Fi','Oi',-magical_angle)
graph(a,triangles+triangles2,'ABCDEFGHIJKLMNOPQRST|AiBiCiDiEiFiGiHiIiJiKiLiMiNiOiPiQiRiSiTi')

rotate_list(['Di','Ci','Mi','Bi','Ri','Ai','Li','Qi','Ki'],'Ni','Ei',-magical_angle)
graph(a,triangles+triangles2,'ABCDEFGHIJKLMNOPQRST|AiBiCiDiEiFiGiHiIiJiKiLiMiNiOiPiQiRiSiTi')

rotate_list(['Ci','Mi','Bi','Ri','Ai','Li','Qi','Ki'],'Ni','Di',-magical_angle)
graph(a,triangles+triangles2,'ABCDEFGHIJKLMNOPQRST|AiBiCiDiEiFiGiHiIiJiKiLiMiNiOiPiQiRiSiTi')

rotate_list(['Bi','Ri','Ai','Li','Qi','Ki'],'Ci','Mi',magical_angle)
graph(a,triangles+triangles2,'ABCDEFGHIJKLMNOPQRST|AiBiCiDiEiFiGiHiIiJiKiLiMiNiOiPiQiRiSiTi')

rotate_list(['Ri','Ai','Li','Qi','Ki'],'Bi','Mi',magical_angle)
graph(a,triangles+triangles2,'ABCDEFGHIJKLMNOPQRST|AiBiCiDiEiFiGiHiIiJiKiLiMiNiOiPiQiRiSiTi')

rotate_list(['Li','Qi','Ki'],'Ai','Ri',magical_angle)
graph(a,triangles+triangles2,'ABCDEFGHIJKLMNOPQRST|AiBiCiDiEiFiGiHiIiJiKiLiMiNiOiPiQiRiSiTi')

rotate_list(['Qi','Ki'],'Li','Ri',magical_angle)
graph(a,triangles+triangles2,'ABCDEFGHIJKLMNOPQRST|AiBiCiDiEiFiGiHiIiJiKiLiMiNiOiPiQiRiSiTi')



graph(a,triangles+triangles2,'ABCDEFGHIJKLMNOPQRST|AiBiCiDiEiFiGiHiIiJiKiLiMiNiOiPiQiRiSiTi')


