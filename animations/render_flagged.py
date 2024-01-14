from math import cos, sin, sqrt, floor, pi
import sys
import os
import networkx as nx
from itertools import product,islice
import numpy as np
import time
import json
from dataframes import df_from_consolidatedfile,readtxtfile
from pathlib import Path

def main(N):
	N=int(N)
	from ..common import make_graph
	from ..common import transforms
	
	consolidatedfile='../outputs/%d/approximate_angles_consolidated.txt' %N

	improvedanglesfile='../outputs/%d/angles_improved.txt' %N

	df=df_from_consolidatedfile(N,consolidatedfile,improvedanglesfile)

	localmax_angles=[]
	localmax_np_ids=[]
	localmax_hitcount=[]

	r=1000
	threshold=10

	flaggedfilepath='../outputs/%d/flagged.tsv' %N
	flaggedfilepath=readtxtfile(flaggedfilepath)
	flaggedlines=[l for l in flaggedfilepath.split('\n') if l!='']
	G=make_graph.main(N,r)
	spokes={e:G.edges[e] for e in G.edges if G.edges[e]['set']=='spokes'}
	spokes_by_index={spokes[e]['index']:e for e in spokes}
	fold_spoke_indices=[spokes[s_id]['index'] for s_id in spokes][1:-1]

	resultsfile='../outputs/%d/finalpositions.txt' %N

	results={}

	for line in flaggedlines:
		np_folding_id_str,optimized_folding_angle_str=line.split('\t')
		np_folding_id=int(np_folding_id_str)
		optimized_folding_angle=float(optimized_folding_angle_str)
		folding=islice(product([i for i in [-1,1]],repeat=len(fold_spoke_indices)),np_folding_id,np_folding_id+1).__next__()
		G=make_graph.main(N)
		G=transforms.folder(
			G=G,
			this_folding=folding,
			angle=optimized_folding_angle
		)
		print(np_folding_id,optimized_folding_angle)
		nodes={}
		for n in G.nodes:
			positions=[float(p) for p in G.nodes[n]['pos']]
			nodes[n]={'x':positions[0],'y':positions[1],'z':positions[2]}
		
		edges=[]
		for e in G.edges:
			edges.append(e)
		
		if np_folding_id_str not in results:
			results[np_folding_id_str]={optimized_folding_angle_str:{'nodes':nodes,'edges':edges}}
		else:
			results[np_folding_id_str][optimized_folding_angle_str]={'nodes':nodes,'edges':edges}
	
	d=open(resultsfile,'w')
	d.write(json.dumps(results,indent=1))
	d.close()

import importlib
from pathlib import Path

#https://gist.github.com/vaultah/d63cb4c86be2774377aa674b009f759a
def import_parents(level=1):
    global __package__
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[level]
    
    sys.path.append(str(top))
    try:
        sys.path.remove(str(parent))
    except ValueError: # already removed
        pass

    __package__ = '.'.join(parent.parts[len(top.parts):])
    importlib.import_module(__package__) # won't be needed after that

if __name__=="__main__" and __package__ is None:
	N=int(sys.argv[1])
	import_parents(level=2)
	main(N)
	
