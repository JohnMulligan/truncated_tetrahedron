from fpdf import FPDF
import sys
from math import tan, cos, sin, pi, radians,sqrt

pdf = FPDF()
# compression is not yet supported in py3k version
pdf.compress = False



pdf.add_page('L',(550,425))
# Unicode is not yet supported in the py3k version; use windows-1252 standard font

class Point:
	def __init__(self,x,y):
		self.x=x
		self.y=y

def inchestouserpoints(i):
	#why is that the conversion? I couldn't tell you.
	x=i*50
	return(x)

D=inchestouserpoints(1/8)
L=inchestouserpoints(4)

a=Point(0,0)
b=Point((D/2)/tan(radians(30))+a.x,D/2+a.y)
c=Point(b.x+L,b.y)
d=Point(c.x+L*cos(radians(60)),c.y+L*sin(radians(60)))
e=Point(d.x+D*cos(radians(30)),d.y-D*sin(radians(30)))
f=Point(c.x+D*cos(radians(30)),c.y-D*sin(radians(30)))

N=a.x+L+(D/2)/cos(radians(30))
k=Point(N,0)

i=Point(k.x+cos(radians(60))*N,k.y+sin(radians(60))*N)

M=sqrt(i.x**2+i.y**2)
#N=M*sin(radians(30))/sin(radians(120))
P=M+2*N*sin(radians(30))


g=Point(f.x+P-2*(f.x-k.x),f.y)
h=Point(e.x+M-2*(e.x-i.x),e.y)

p=Point(i.x+M,i.y)
q=Point(k.x+P,a.y)
r=Point(q.x+N,a.y)
u=Point(g.x+(f.x-c.x),c.y)
s=Point(u.x+L,c.y)
t=Point(h.x+(e.x-d.x),d.y)

def l(p1,p2):
	pdf.line(p1.x,p1.y,p2.x,p2.y)

dx=50
dy=50

#translate
for varname in "abcdefghikpqrstu":
	exec("%s.x+=%s" %(varname,str(dx)))
	exec("%s.y+=%s" %(varname,str(dy)))

#rotate
#......

#outer wide trap
l(a,i)
l(i,p)
l(p,r)
l(r,a)

#inner left triangle
l(s,t)
l(t,u)
l(u,s)

#inner tall trap
l(g,h)
l(h,e)
l(e,f)
l(f,g)

#inner right triangle
l(d,c)
l(c,b)
l(b,d)

pdf.output('trap.pdf', 'F')
