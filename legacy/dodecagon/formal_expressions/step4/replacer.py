from replacements import replacements
import re
from math import sin,cos,pi,sqrt
import os

from four import *

THT=1.415471989998
r=1

vars=["Rx","Ry","Rz","Ox","Oy","Oz"]


'''A=(2*sqrt(3))
B=(2-sqrt(3))
C=(1-2*sqrt(3))
D=sqrt(3)/2


8:{
	"replacements":
		[
			["(2*sqrt(3))","A"],
			["2-sqrt(3)","B"],
			["1-2*sqrt(3)","C"],
			["(1-cos(THT))*1","(1-cos(THT))"],
			["sqrt(3)/2","D"]
			
		],
	"label":"symbolic"
},
'''

def loadv(v):
	d=open("./tmp/"+v+".txt","r")
	t=d.read()
	d.close()
	return(t)

def dumpv(vname,vcontent):
	d=open("./tmp/"+vname+".txt","w")
	d.write(vcontent)
	d.close()

for v in vars:
	vcontent=eval(v)
	dumpv(v,vcontent)

for i in replacements:
	#rescapeA,rescapeB=replacements[i]['rescape']
	label=replacements[i]['label']
	step_replacements=replacements[i]['replacements']
	print(label)
	for replacement in step_replacements:
		a,b=replacement
		
		stepvals=[]
		for v in vars:
			varcontent=loadv(v)
			varcontent=varcontent.replace(a,b)
			stepvals.append(eval(varcontent))
			#print(v,eval(varcontent))
			dumpv(v,varcontent)
		print(stepvals)