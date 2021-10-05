import sys
import os
from multiprocessing import Pool, TimeoutError
import time
from tetrahedron_multiproc import main as f


if __name__ == '__main__':
	base_angle= 1.230999000000
	end_angle=  1.231000100000
	step=       0.000000000001
	angle=base_angle
	work=[]
	while angle<end_angle:
		work.append(angle)
		angle+=step
	with Pool(processes=8) as pool:
		pool.map(f,work)