import json
import os
import sys
import re
#import plotly.express as px
#import plotly.graph_objects as go
import pandas as pd
from common.dataframes import approx_angle_txtfiles_to_df

'''
	this script runs through a finished sweep's files
	outputs/{{N}}/approximate_angles_worker_{{task_id}}.txt
	pulls out all the hits and finds the local minima
	and then writes out to that N's "approximate_angles_consolidated.txt"
	for the sake of efficient memory use, we should run this before committing anything to git
	--in other words, only the consolidated file should come off the cluster
	however, i've saved the raw outputs from 10 and 12 as examples (tarballs)
'''

N=int(sys.argv[1])

basepath='outputs/%d' %N

approximate_angle_files=[f for f in os.listdir(basepath) if re.match('approximate_angles.txt',f)]

df=approx_angle_txtfiles_to_df(basepath,approximate_angle_files)

#we are going to walk over all the angles, looking for continuities in the folding id's
#and identifying local minima on the distances
df=df.sort_values(by=['angle'])

#but first we're going to eliminate the noise at the beginning and end of the graph
def find_limit_folding_angle(folding_ids_dict,angles,keepers):
	keepers=[]
	for angle in angles[1:]:
		this_angle_df=df[df['angle']==angle]
		this_angle_folding_ids=set(list(this_angle_df.folding_id.values))
		for ifid in list(folding_ids_dict.keys()):
			if ifid not in this_angle_folding_ids:
				del(folding_ids_dict[ifid])
		initial_folding_ids=set(list(folding_ids_dict.keys()))
		if len(this_angle_folding_ids.intersection(initial_folding_ids))==0:
			last_initial_angle=prev_angle
			break
		else:
			#identities hiding under the initial curve
			##this happens occasionally as N grows -- edge case but i don't want to lose them
			for row in this_angle_df.itertuples():
				folding_id=row.folding_id
				median_distance=row.median_distance
				if row.folding_id not in folding_ids_dict:
					keepers.append({
						'angle':angle,
						'folding_id':folding_id,
						'median_distance':median_distance
					})
		prev_angle=angle
	return(prev_angle,keepers)

keepers=[]

angles=list(df.angle.unique())
angles.sort()
initial_folding_ids_dict={row.folding_id:row.median_distance for row in df[df['angle']==angles[0]].itertuples()}
initial_limit_angle,keepers=find_limit_folding_angle(initial_folding_ids_dict,angles,keepers)
print("initial cutoff",initial_limit_angle)

angles.reverse()
final_folding_ids_dict={row.folding_id:row.median_distance for row in df[df['angle']==angles[0]].itertuples()}
final_limit_angle,keepers=find_limit_folding_angle(final_folding_ids_dict,angles,keepers)
print("final cutoff",final_limit_angle)

print("hits under the beginning and ending curves",json.dumps(keepers,indent=2))

df=df[df['angle']>initial_limit_angle]
df=df[df['angle']<final_limit_angle]

df=df.sort_values(by=['angle'])

## we now, as far as I've seen, have local distance minima on angles at specific folding ids
for folding_id in df.folding_id.unique():
	fid_df=df[df['folding_id']==folding_id]
	prev_dist=10000
	angles=fid_df.angle.unique()
	angles.sort()
	for angle in angles:
		median_distance=fid_df[fid_df['angle']==angle].median_distance.values[0]
		close_neighborings=fid_df[fid_df['angle']==angle].close_neighborings.values[0]
		if median_distance>prev_dist:
			local_min={
				'angle':float(prev_angle),
				'folding_id':int(folding_id),
				'median_distance':float(prev_dist),
				'close_neighborings':json.dumps(close_neighborings)
			}
			keepers.append(local_min)
			prev_dist=10000
			break
		else:
			prev_dist=median_distance
			prev_angle=angle

d=open('outputs/%d/approximate_angles_consolidated.txt' %N,'w')

lines=[]
for k in keepers:
	linearray=[str(k['angle']),str(k['folding_id']),k['median_distance'],k['close_neighborings']]
	line='\t'.join(linearray)
	lines.append(line)

d.write('\n'.join(lines))
d.close()


# optimized_df=pd.DataFrame.from_records(keepers)

#heatmap
# fig = go.Figure(
# 	data=go.Heatmap(
# 		z=optimized_df['median_distance'],
# 		y=optimized_df['folding_id'],
# 		x=optimized_df['angle']
# 	)
# )

# fig.show()
