
import re
from math import sin,cos
import os

THT=1.415471989998
r=1000

d=open("expanded.txt","r")
t=d.read()
d.close()

print(eval(t))