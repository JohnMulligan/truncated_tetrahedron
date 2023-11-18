import os
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import json
import sys

def readtxtfile(filepath):
	d=open(filepath)
	t=d.read()
	d.close()
	return(t)

def df_from_consolidatedfile(consolidatedfile):
	consolidated=readtxtfile(consolidatedfile)
	consolidatedlines=[c for c in consolidated.split('\n\n') if c!='']
		
	records=[]
	
	for line in consolidatedlines:
		record=json.loads(line)
		n,np_id=[int(i) for i in record['this_folding_np_id'].split('_')]
		record['n']=n
		record['np_id']=np_id
		records.append(record)
	df=pd.DataFrame.from_records(records)
	df=df.sort_values(by=['np_id'])
	print(df, df['this_folding_np_id'])
	return df

def main(N):
	N=int(N)
	
	consolidatedfile='../optimizer/outputs/%d/consolidated.txt' %N
	df=df_from_consolidatedfile(consolidatedfile)

	localmax_angles=[]
	localmax_np_ids=[]
	localmax_hitcount=[]

	for angle in df['angle'].unique():
		print(angle)
		df2=df[['angle','np_id','n','close_neighborings_count']]
		df2=df2[df2['angle']==angle]
		hitsarray=list(df2['close_neighborings_count'].values)
		np_ids=list(df2['np_id'].values)
		angles=list(df2['angle'].values)
		
		for idx in range(len(hitsarray)):
			this_val=hitsarray[idx]
			if idx not in (0,len(hitsarray)-1):
				prev_val=hitsarray[idx-1]
				next_val=hitsarray[idx+1]
				if prev_val < this_val and next_val < this_val:
					#basic peak
					localmax_angles.append(angles[idx])
					localmax_np_ids.append(np_ids[idx])
					localmax_hitcount.append(hitsarray[idx])
				elif next_val==this_val and prev_val < this_val:
					#beginning of plateau
					localmax_angles.append(angles[idx])
					localmax_np_ids.append(np_ids[idx])
					localmax_hitcount.append(hitsarray[idx])
				elif prev_val==this_val and next_val < this_val:
					#end of plateau
					localmax_angles.append(angles[idx])
					localmax_np_ids.append(np_ids[idx])
					localmax_hitcount.append(hitsarray[idx])
			if len(hitsarray)==1:
				localmax_angles.append(angles[idx])
				localmax_np_ids.append(np_ids[idx])
				localmax_hitcount.append(hitsarray[idx])
			else:
				if idx==len(hitsarray)-1:
					prev_val=hitsarray[idx-1]
					if prev_val < this_val:
						#last if max
						localmax_angles.append(angles[idx])
						localmax_np_ids.append(np_ids[idx])
						localmax_hitcount.append(hitsarray[idx])
				if idx==0:
					next_val=hitsarray[idx+1]
					if next_val < this_val:
						#first if max
						localmax_angles.append(angles[idx])
						localmax_np_ids.append(np_ids[idx])
						localmax_hitcount.append(hitsarray[idx])
	
	d=open("../optimizer/outputs/%s/flagged.tsv" %str(N),"w")
	lines=[]
	for idx in range(len(localmax_angles)):
		angle=localmax_angles[idx]
		np_id=localmax_np_ids[idx]
		lines.append("\t".join([str(i) for i in [np_id,angle]]))
	d.write('\n'.join(lines))
	d.close()
		
	
	fig = px.line_3d(
		df,
		x="angle",
		y="np_id",
		z="close_neighborings_count",
		color='angle'
	)
	
	fig.add_trace(
		go.Scatter3d(
			x=localmax_angles,
			y=localmax_np_ids,
			z=localmax_hitcount,
			mode='markers'
		)
	)
	
	fig.update_layout(scene = dict(
		xaxis_title="angle",
		yaxis_title="np_id",
		zaxis_title="hit count"
	))

	fig.show()

if __name__=="__main__":
	N=int(sys.argv[1])
	main(N)
