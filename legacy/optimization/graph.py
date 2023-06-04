import pandas as pd
import plotly.express as px
df = pd.read_csv('output.csv')
df.head()
fig = px.scatter(df, x = 'ANGLE', y = 'DISTANCE',color="SEGMENT")
fig.write_html("output.html")
