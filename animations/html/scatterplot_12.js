// THANKS, FOLKS! https://plotly.com/javascript/3d-scatter-plots/
// d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/3d-scatter.csv', function(err, rows){

d3.csv('https://raw.githubusercontent.com/JohnMulligan/dihedral_public/main/12.csv', function(err, rows){

function unpack(rows, key) {
	return rows.map(function(row)
	{ return row[key]; });}

var trace1 = {
	x:unpack(rows, 'x1'), y: unpack(rows, 'y1'), z: unpack(rows, 'z1'),
	mode: 'markers',
	marker: {
		size: 12,
		color: 'rgb(136, 8, 8)',
		symbol: 'circle'},
	type: 'scatter3d'
};

var trace2 = {
	x:unpack(rows, 'x2'), y: unpack(rows, 'y2'), z: unpack(rows, 'z2'),
	mode: 'markers',
	marker: {
		color: 'rgb(0, 20, 217)',
		size: 12,
		symbol: 'circle',
		opacity: 0.2},
	type: 'scatter3d'};

var data = [trace1, trace2];
var layout = {
	scene: {
		xaxis:{title: 'Folding angle'},
		yaxis:{title: 'Folding iteration'},
		zaxis:{title: 'Intersections'},
	},
	margin: {
	l: 0,
	r: 0,
	b: 0,
	t: 0
  }};

Plotly.newPlot('scatterplotdiv', data, layout);

var scatterplotdiv = document.getElementById('scatterplotdiv').on('plotly_click',
	function(data) {
		var p=data.points[0]
		var tracename=p.fullData.name
		var x=p.x
		var y=p.y
		var z=p.z
		x=x.replace("\.","_")
	
		var N='12'
	
		var xyz=['p',N,y,x]
		var scriptname=xyz.join('_')
		if (tracename=='trace 0') {
			sketchname=scriptname;
		}

	}
);



});
