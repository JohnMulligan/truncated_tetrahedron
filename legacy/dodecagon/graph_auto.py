import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output
from math import pi as pi
from math import cos as cos
from math import sin as sin
from math import sqrt as sqrt
import plotly.graph_objects as go
import random
import json
app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server

magical_angle=1.415471989998
r=1000
pointstr='ABCDEFGHIJKLMNOPQRST'
triangles=[
	['L','S','T'],
	['A','R','M'],['A','M','B'],
	['B','M','C'],
	['C','M','N'],['C','N','D'],
	['D','N','E'],
	['N','E','O'],['E','O','F'],
	['F','O','G'],
	['G','H','O'],['P','O','H'],
	['H','I','P'],
	['J','I','P'],['J','P','Q'],
	['J','Q','K'],
	['K','Q','S'],['K','L','S']	
	]
	
def make_points():
	X=[eval(eval(i+"x")) for i in pointstr]
	Y=[eval(eval(i+"y")) for i in pointstr]
	Z=[eval(eval(i+"z")) for i in pointstr]
	I=[pointstr.index(i[0]) for i in triangles]
	J=[pointstr.index(i[1]) for i in triangles]
	K=[pointstr.index(i[2]) for i in triangles]
	return {"X":X,"Y":Y,"Z":Z,"I":I,"J":J,"K":K}

points_dict={}
from formal_expressions.zero import *
points_dict[0]=make_points()
from formal_expressions.one import *
points_dict[1]=make_points()
from formal_expressions.two import *
points_dict[2]=make_points()
from formal_expressions.three import *
points_dict[3]=make_points()
from formal_expressions.four import *
points_dict[4]=make_points()
from formal_expressions.five import *
points_dict[5]=make_points()
from formal_expressions.six import *
points_dict[6]=make_points()
from formal_expressions.seven import *
points_dict[7]=make_points()
from formal_expressions.eight import *
points_dict[8]=make_points()
from formal_expressions.nine import *
points_dict[9]=make_points()
from formal_expressions.ten import *
points_dict[10]=make_points()
from formal_expressions.eleven import *
points_dict[11]=make_points()



#FROM https://dash.plotly.com/live-updates

app.layout = html.Div(
	children=[
		dcc.Graph(
			id='3dmesh'
		),
		dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )
        ,dcc.Store(id='intermediate-value',data=json.dumps({"value":0}))
    ]
    )


@app.callback(
	[Output('3dmesh', 'figure'),Output('intermediate-value', 'data')],
	[Input('interval-component','n_intervals'),Input('intermediate-value', 'data')]
	)

def update_figure(n,data):
	step=random.choice([-1,1])
	value=json.loads(data)['value']
	
	p=value+step
	if p>11:
		p=10
	if p<0:
		p=1
	
	X=points_dict[p]["X"]
	Y=points_dict[p]["Y"]
	Z=points_dict[p]["Z"]
	I=points_dict[p]["I"]
	J=points_dict[p]["J"]
	K=points_dict[p]["K"]
	fig = go.Figure(data=[
		go.Mesh3d(
			x=X,
			y=Y,
			z=Z,
			i=I,
			j=J,
			k=K,
			showscale=False
		)
	])
	
	fig.update_layout(
    scene = dict(
		xaxis = dict(nticks=0, range=[-1000,1000],showticklabels=False),
		yaxis = dict(nticks=0, range=[-1000,1000],showticklabels=False),
		zaxis = dict(nticks=0, range=[-1000,1000],showticklabels=False),
		xaxis_title='',
		yaxis_title='',
		zaxis_title=''
		),
	width=800,
	height=800
	)
	
	return(fig,json.dumps({"value":p}))

if __name__ == '__main__':
    app.run_server(host='0.0.0.0',debug=False,port=3000)