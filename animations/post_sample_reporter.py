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
	
	flaggedbasepath="optimizer_outputs/%d/" %N
	flaggedtxt=readtxtfile(os.path.join(flaggedbasepath,"flagged.tsv"))
	unfinished_flagged=[l.split('\t') for l in flaggedtxt.split("\n") if l!='']
	
	finished_work_filepath=os.path.join(flaggedbasepath,"finished_flagged.tsv")
	
	if os.path.exists(finished_work_filepath):
		finished_flagged=readtxtfile(finished_work_filepath)
		finished_flagged=[l.split('\t') for l in finished_flagged.split("\n") if l!='']
	else:
		finished_flagged=[]
	
	print("work remaining before this run:",len(unfinished_flagged))
	print("work finished before this run:", len(finished_flagged))
	
	checkpointbasepath='outputs/%d/checkpoints' %N
	checkpointfiles=os.listdir(checkpointbasepath)
	print(checkpointfiles)	
	work_finished_this_run=[]
	for checkpointfile in checkpointfiles:
		
		this_worker_txt=readtxtfile(os.path.join(checkpointbasepath,checkpointfile))
		this_worker_finished_lines=[l for l in this_worker_txt.split("\n") if l!='']
		for l in this_worker_finished_lines:
			print(l)	
			thismatch=json.loads(l)
			this_folding_np_id=thismatch['this_folding_np_id']
			n,np_id=[i for i in this_folding_np_id.split('_')]
			angle=thismatch['angle']
			item=[str(np_id),str(angle)]
			work_finished_this_run.append(item)
	
	print("work finished during this run:",len(work_finished_this_run))
	
	revised_unfinished_work_list=[]
	
	for flagged in unfinished_flagged:
		
		if flagged in work_finished_this_run:
			finished_flagged.append(flagged)
		else:
			revised_unfinished_work_list.append(flagged)
	
	print("new remaining work list length:",len(revised_unfinished_work_list))
	
	print("new finished work list length:",len(finished_flagged))
	d=open(os.path.join(flaggedbasepath,"flagged.tsv"),"w")
	d.write("\n".join(['\t'.join(i) for i in revised_unfinished_work_list]))
	d.close()
	
	d=open(os.path.join(flaggedbasepath,"finished_flagged.tsv"),"w")
	d.write("\n\n".join(['\t'.join(i) for i in finished_flagged]))
	d.close()
	
	for checkpointfile in checkpointfiles:
		os.remove(os.path.join(checkpointbasepath,checkpointfile))
	
if __name__=="__main__":
	N=int(sys.argv[1])
	main(N=N)
