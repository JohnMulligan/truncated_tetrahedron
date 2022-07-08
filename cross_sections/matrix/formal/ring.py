from graph import main as graph
import math
from math import cos, sin, sqrt,asin
import sys
import os
from vars import *

vertices={i:None for i in 'ABCDEFGHIJKLMN'}

##############ALTERNATING TRAPEZOIDS w 60 AND 120 DEGREE INTERIOR ANGLES
####SHORT SIDE ON ONE IS THE LONG SIDE ON THE OTHER
top_vs="ABCDEFG"

for v in top_vs:
	n=top_vs.index(v)
	if n!=0:
		previous_offset=vertices[top_vs[n-1]][0]
		x=[ss,ll][n%2]+ "+" + previous_offset
	else:
		x="0"
	vertices[v]=[x,"0","0"]

print(vertices)

bottom_vs="HIJKLMN"

for v in bottom_vs:
	n=bottom_vs.index(v)
	if n==0:
		x=x_offsets
	else:
		previous_offset=vertices[bottom_vs[n-1]][0]
		x=previous_offset + "+" + [ss,ls][n%2]
	vertices[v]=[x,"-"+y_offset,"0"]

print(vertices)

triangles=[	['A','B','H'],['H','I','B'],['B','I','C'],['C','I','J'],
			['C','J','K'],['C','D','K'],['D','E','L'],['D','K','L'],
			['E','L','F'],['F','L','M'],['F','M','G'],['G','M','N']
		]

graph(vertices,triangles)

















#graph(vertices,triangles)


rotate_list('CDEFGJKLMN','B','I',magical_angle)


#graph(vertices,triangles)

rotate_list('DEFGKLMN','C','J',magical_angle)

#graph(vertices,triangles)


rotate_list('EFGLMN','D','K',magical_angle)

#graph(vertices,triangles)


rotate_list('FGMN','E','L',magical_angle)

#graph(vertices,triangles)

rotate_list('GN','F','M',magical_angle)

graph(vertices,triangles)
