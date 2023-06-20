function setup() {
  var canvas=createCanvas(800, 800, WEBGL);
  canvas.parent('processinganimationdiv');
  fill(204);
}

var sketchname='p_10_31_2_034443043'

function draw() {
  background(220);
  
	if(sketchname == 'p_10_255_1_107149611') {p_10_255_1_107149611();}
if(sketchname == 'p_10_256_1_107149611') {p_10_256_1_107149611();}
if(sketchname == 'p_10_127_1_107149611') {p_10_127_1_107149611();}
if(sketchname == 'p_10_128_1_107149611') {p_10_128_1_107149611();}
if(sketchname == 'p_10_191_1_107149611') {p_10_191_1_107149611();}
if(sketchname == 'p_10_192_1_107149611') {p_10_192_1_107149611();}
if(sketchname == 'p_10_63_1_107149611') {p_10_63_1_107149611();}
if(sketchname == 'p_10_64_1_107149611') {p_10_64_1_107149611();}
if(sketchname == 'p_10_0_1_107149611') {p_10_0_1_107149611();}
if(sketchname == 'p_10_31_1_107149611') {p_10_31_1_107149611();}
if(sketchname == 'p_10_255_2_034443043') {p_10_255_2_034443043();}
if(sketchname == 'p_10_256_2_034443043') {p_10_256_2_034443043();}
if(sketchname == 'p_10_224_2_034443043') {p_10_224_2_034443043();}
if(sketchname == 'p_10_225_2_034443043') {p_10_225_2_034443043();}
if(sketchname == 'p_10_240_2_034443043') {p_10_240_2_034443043();}
if(sketchname == 'p_10_127_2_034443043') {p_10_127_2_034443043();}
if(sketchname == 'p_10_112_2_034443043') {p_10_112_2_034443043();}
if(sketchname == 'p_10_120_2_034443043') {p_10_120_2_034443043();}
if(sketchname == 'p_10_158_2_034443043') {p_10_158_2_034443043();}
if(sketchname == 'p_10_159_2_034443043') {p_10_159_2_034443043();}
if(sketchname == 'p_10_191_2_034443043') {p_10_191_2_034443043();}
if(sketchname == 'p_10_192_2_034443043') {p_10_192_2_034443043();}
if(sketchname == 'p_10_195_2_034443043') {p_10_195_2_034443043();}
if(sketchname == 'p_10_96_2_034443043') {p_10_96_2_034443043();}
if(sketchname == 'p_10_97_2_034443043') {p_10_97_2_034443043();}
if(sketchname == 'p_10_60_2_034443043') {p_10_60_2_034443043();}
if(sketchname == 'p_10_63_2_034443043') {p_10_63_2_034443043();}
if(sketchname == 'p_10_0_2_034443043') {p_10_0_2_034443043();}
if(sketchname == 'p_10_31_2_034443043') {p_10_31_2_034443043();}

  
}

function polygon( x, y,  radius,  npoints) {
  var angle = 3 / npoints;
  beginShape();
  for (var a = 0; a < TWO_PI; a += angle) {
    var sx = x + cos(a) * radius;
    var sy = y + sin(a) * radius;
    vertex(sx, sy);
  }
  endShape(CLOSE);
}