from replacements import replacements
import re
from math import sin,cos,pi,sqrt
import os

from four import *

THT=1.415471989998
r=1

d=open("RxOx.txt","r")
t=d.read()
d.close()

print(eval(t))
