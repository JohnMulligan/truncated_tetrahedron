d=open('steps.txt','r')
t=d.read()
d.close()
lines=[i for i in t.split('\n') if i !='']

pointsteps={}



for l in lines:
	point,x,y,z=l.split('\t')
	point=str(point.lower())
	for c in [['x',x],['y',y],['z',z]]:
		label,val=c
		valf=float(val)
		labelstr=str(point+label)
		if labelstr not in pointsteps:
			pointsteps[labelstr]=[valf]
		else:
			pointsteps[labelstr].append(valf)



d=open("javaformatsteps.txt",'a')
for ps in pointsteps:
	c=str(pointsteps[ps])[1:-1]
	d.write("float[] %s = {%s};\n" %(ps,c))
	
d.close()
	