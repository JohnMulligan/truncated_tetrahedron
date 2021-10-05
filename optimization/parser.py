import re
import os
import sys

filedir=sys.argv[1]


input_files=[i for i in os.listdir(filedir) if i.endswith('.txt')]
e=open('output.csv','a')
e.write("SEGMENT,DISTANCE,ANGLE\n")
for f in input_files:
	print(f)
	d=open(os.path.join(filedir,f),'r')
	t=d.read()
	d.close()
	blocks=t.split('ANGLE: ')
	#print(blocks[0:5])
	for block in blocks:
		lines=block.split('\n')
		#print(lines[0])
		angle=lines[0]
		for line in lines[1:]:
			cols=[i for i in line.split('\t') if i!='']
			print(cols)
			if len(cols)==3 and cols[0]!="LOOP:":
				out_list=[cols[0]+cols[1],cols[2],angle]
				outline=','.join(out_list)
				e.write(outline)
				e.write('\n')
e.close()