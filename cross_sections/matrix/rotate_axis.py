import numpy as np
from math import cos,sin,sqrt

#from https://www.eng.uc.edu/~beaucag/Classes/Properties/OptionalProjects/CoordinateTransformationCode/Rotate%20about%20an%20arbitrary%20axis%20(3%20dimensions).html
def main(p,axispoint1,axispoint2,theta):
	
	#print(type(point),point)
	#print(type(axispoint1),axispoint1)
	#print(type(axispoint2),axispoint2)
	
	#print("INPUTS",p,axispoint1,axispoint2,theta)
	
	Ti=[
		[1,0,0,p[0]],
		[0,1,0,p[1]],
		[0,0,1,p[2]],
		[0,0,0,1]
	]
	
	
	T=[
		[1,0,0,-p[0]],
		[0,1,0,-p[1]],
		[0,0,1,-p[2]],
		[0,0,0,1]
	]
	
	
	v=sqrt(
		(axispoint2[0]-axispoint1[0])**2+
		(axispoint2[1]-axispoint1[1])**2+
		(axispoint2[2]-axispoint1[2])**2
	)
	
	
	print("v=",v)
	
	u=(np.array(axispoint2)-np.array(axispoint1))/v
	
	print("u=",u)
	
	a,b,c=[i for i in u]
	
	print("a,b,c=",a,b,c)
	
	Rz=[
		[cos(theta),sin(theta),0,0],
		[-sin(theta),cos(theta),0,0],
		[0,0,1,0],
		[0,0,0,1]
	]
	
	d=sqrt(b**2+c**2)
	
	print("d=",d)
	
	Rx = [
		[1,0,0,0],
		[0,cos(theta),-sin(theta),0],
		[0,sin(theta),cos(theta),0],
		[0,0,0,1]
	]
	
	Rxi = [
		[1,0,0,0],
		[0,cos(theta),sin(theta),0],
		[0,-sin(theta),cos(theta),0],
		[0,0,0,1]
	]
	
	Ry = [
		[d,0,-a,0],
		[0,1,0,0],
		[a,0,d,0],
		[0,0,0,1]
	]
	
	Ryi = [
		[d,0,a,0],
		[0,1,0,0],
		[-a,0,d,0],
		[0,0,0,1]
	]
	
	#print(p)
	
	pv=[p[0],p[1],p[2],1]
		
	#for i in ["Ti","Rxi","Ryi","Rz","Ry","Rx","T","p"]:
	#	print(i,eval(i))
	
	#print(p)
	
	point_p=np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(Ti,Rxi),Ryi),Rz),Ry),Rx),T),pv)
	
	point_p=point_p[:-1]
	
	#print("---->",point_p)
	#print(p,point_p)
	
	return point_p