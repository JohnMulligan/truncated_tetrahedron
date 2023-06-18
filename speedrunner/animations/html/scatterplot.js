// THANKS, FOLKS! https://plotly.com/javascript/3d-scatter-plots/
// d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/3d-scatter.csv', function(err, rows){




d3.csv('https://raw.githubusercontent.com/JohnMulligan/truncated_tetrahedron/main/speedrunner/animations/html/12.csv', function(err, rows){


function unpack(rows, key) {
	return rows.map(function(row)
	{ return row[key]; });}

var trace1 = {
	x:unpack(rows, 'x1'), y: unpack(rows, 'y1'), z: unpack(rows, 'z1'),
	mode: 'markers',
	marker: {
		size: 12,
		line: {
		color: 'rgba(217, 217, 217, 0.14)',
		width: 0.5},
		opacity: 0.8},
	type: 'scatter3d'
};

var trace2 = {
	x:unpack(rows, 'x2'), y: unpack(rows, 'y2'), z: unpack(rows, 'z2'),
	mode: 'markers',
	marker: {
		color: 'rgb(127, 127, 127)',
		size: 12,
		symbol: 'circle',
		line: {
		color: 'rgb(204, 204, 204)',
		width: 1},
		opacity: 0.8},
	type: 'scatter3d'};

var data = [trace1, trace2];
var layout = {margin: {
	l: 0,
	r: 0,
	b: 0,
	t: 0
  }};




Plotly.newPlot('scatterplotdiv', data, layout);

var scatterplotdiv = document.getElementById('scatterplotdiv').on('plotly_click', function(data) {
	var p=data.points[0]
	var tracename=p.fullData.name
	console.log(tracename)
	var x=p.x
	var y=p.y
	var z=p.z
	x=x.replace("\.","_")
	
	var N='12'
	
	var xyz=['p',N,y,x]
// 	console.log(xyz)
	console.log(sketchname)
	var scriptname=xyz.join('_')
	
	sketchname=scriptname;
	
	console.log(sketchname)
	
// 	p_12_191_1_41547199
	
	
	
});



});

scatterplotdiv.on('plotly_click', function(data){
	console.log(data)
//     var pts = '';
// 
//     for(var i=0; i < data.points.length; i++){
// 
//         pts = 'x = '+data.points[i].x +'\ny = '+
// 
//             data.points[i].y.toPrecision(4) + '\n\n';
// 
//     }
// 
//     alert('Closest point clicked:\n\n'+pts);

});
