import statistics
from math import cos, sin, sqrt, floor, pi
import sys
import os
from itertools import product,islice
import time
import json
import re

def readtxtfile(filepath,delete=False):
	d=open(filepath)
	t=d.read()
	d.close()
	if delete:
		os.remove(filepath)
	return(t)

def main(N):
	
	N=int(N)
	
	basedir='outputs/%d/' %N
	
	ngon_outputfiles=[i for i in os.listdir(basedir) if re.match('[0-9]+\.txt',i)]
	
	checkpointfilepath=os.path.join(basedir,'checkpoint.txt')
	
	checkpointfile=readtxtfile(checkpointfilepath)
	
	number_of_possible_folds=2**(N-1)
	
	finished_work=[int(i) for i in checkpointfile.split('\n') if i!='']
	
	print("total_work on %d:" %N,number_of_possible_folds)
	
	print("finished work:",len(finished_work))
	
	consolidated=open(os.path.join(basedir,'consolidated.txt'),'a')
	
	for ngon_outputfilename in ngon_outputfiles:
		
		ngon_outputfile=readtxtfile(os.path.join(basedir,ngon_outputfilename),delete=True)
		
		consolidated.write('\n\n'+ngon_outputfile)
	
	consolidated.close()
	
	minimal_report_data={}
	
	consolidated=readtxtfile(os.path.join(basedir,'consolidated.txt'))
	
	consolidatedlines=[c for c in consolidated.split('\n\n') if c!='']
	
	for line in consolidatedlines:
		j=json.loads(line)
		close_neighborings_count=j['close_neighborings_count']
		angle=j['angle']
		this_folding_np_id=j['this_folding_np_id']
		if angle not in minimal_report_data:
			minimal_report_data[angle]={
				'hitcount':1,
				'close_neighborings_counts':[close_neighborings_count]
			}
		else:
			minimal_report_data[angle]['hitcount']+=1
			minimal_report_data[angle]['close_neighborings_counts'].append(close_neighborings_count)
	
	for angle in minimal_report_data:
		
		hitcount=minimal_report_data[angle]['hitcount']
		close_neighborings_counts=minimal_report_data[angle]['close_neighborings_counts']
		
		mean=statistics.mean(close_neighborings_counts)
		minimum=min(close_neighborings_counts)
		maximum=max(close_neighborings_counts)
		print(angle,"-->","min:%d, max:%d, mean:%d. total hits:%d" %(minimum,maximum,mean,hitcount))
	

if __name__=="__main__":
	N=int(sys.argv[1])
	main(N=N)
