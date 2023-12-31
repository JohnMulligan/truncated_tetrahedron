import os
import sys
import re
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from common.dataframes import approx_angle_txtfiles_to_df

N=int(sys.argv[1])

basepath='outputs/%d' %N

approximate_angle_files=[f for f in os.listdir(basepath) if re.match('approximate_angles_consolidated.txt',f)]

df=approx_angle_txtfiles_to_df(basepath,approximate_angle_files)

#heatmap
fig = go.Figure(data=go.Heatmap(z=df['median_distance'],y=df['folding_id'],x=df['angle']))
fig.show()

#3d scatter
fig = px.scatter_3d(df, x='angle', y='folding_id', z='median_distance')
fig.show()

#2d scatter
fig=px.scatter(df,x='angle',y='median_distance')
fig.show()

#2d binned scatter (reduces the resolution of a 1000/th level sweep by 1/3)
df2=df
df2['anglebins']=pd.cut(df2['angle'],300)
df3=df2.groupby('anglebins').min('median_distance')

fig=px.scatter(df3,x='angle',y='median_distance')
fig.show()





