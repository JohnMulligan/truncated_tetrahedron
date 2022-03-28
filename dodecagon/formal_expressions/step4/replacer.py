from replacements import replacements
import re
from math import sin,cos,pi,sqrt
import os

from four import *

THT=1.415471989998
r=1000

vars=["Rx","Ry","Rz"]

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