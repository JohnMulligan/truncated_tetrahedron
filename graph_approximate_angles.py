import os
import sys
import re
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

N=int(sys.argv[1])

basepath='outputs/%d' %N

approximate_angle_files=[f for f in os.listdir(basepath) if re.match('approximate_angles_worker_[0-9]+\.txt',f)]
approximate_angles={
	"angle":[],
	"folding_id":[],
	"average_distance":[]
}

for aaf in approximate_angle_files:
	d=open(os.path.join(basepath,aaf),'r')
	t=d.read()
	d.close()
	goodlines=[line for line in t.split("\n") if line!='']
	for line in goodlines:
		linevals=line.split('\t')
		if len(linevals)==4:
			angle_str,folding_id_str,folding_pattern_str,average_distance_str=linevals
			angle=float(angle_str)
			folding_id=int(folding_id_str)
			average_distance=float(average_distance_str)
			approximate_angles['angle'].append(angle)
			approximate_angles['folding_id'].append(folding_id)
			approximate_angles['average_distance'].append(average_distance)

df=pd.DataFrame.from_dict(approximate_angles)

#heatmap
fig = go.Figure(data=go.Heatmap(z=df['average_distance'],y=df['folding_id'],x=df['angle']))
fig.show()

#3d scatter
fig = px.scatter_3d(df, x='angle', y='folding_id', z='average_distance')
fig.show()

#2d scatter
fig=px.scatter(df,x='angle',y='average_distance')
fig.show()

#2d binned scatter (reduces the resolution of a 1000/th level sweep by 1/3)
df2=df
df2['anglebins']=pd.cut(df2['angle'],300)
df3=df2.groupby('anglebins').min('average_distance')

fig=px.scatter(df3,x='angle',y='average_distance')
fig.show()





