function setup() {
  var canvas=createCanvas(1000, 800, WEBGL);
  canvas.parent('processinganimationdiv');
  fill(204);
}

var sketchname='p_12_0_1_41547199'

function draw() {
  background(220);
  

  if(sketchname == 'p_12_0_1_41547199') {
    p_12_0_1_41547199();
  }
  
  if(sketchname == 'p_12_1023_1_41547199') {
    p_12_1023_1_41547199();
  }
  
  if(sketchname == 'p_12_1024_1_41547199') {
    p_12_1024_1_41547199();
  }
  
  if(sketchname == 'p_12_127_1_41547199') {
    p_12_127_1_41547199();
  }
  
  if(sketchname == 'p_12_0_1_41547199') {
    p_12_0_1_41547199();
  }
  
  if(sketchname == 'p_12_576_1_41547199') {
    p_12_576_1_41547199();
  }
  
  if(sketchname == 'p_12_768_1_41547199') {
    p_12_768_1_41547199();
  }
  
  if(sketchname == 'p_12_639_1_41547199') {
    p_12_639_1_41547199();
  }
  
  if(sketchname == 'p_12_63_1_41547199') {
    p_12_63_1_41547199();
  }
  
  if(sketchname == 'p_12_703_1_41547199') {
    p_12_703_1_41547199();
  }
  
  if(sketchname == 'p_12_896_1_41547199') {
    p_12_896_1_41547199();
  }
  
  if(sketchname == 'p_12_512_1_41547199') {
    p_12_512_1_41547199();
  }
  
  if(sketchname == 'p_12_480_1_41547199') {
    p_12_480_1_41547199();
  }
  
  if(sketchname == 'p_12_448_1_41547199') {
    p_12_448_1_41547199();
  }
  
  if(sketchname == 'p_12_320_1_41547199') {
    p_12_320_1_41547199();
  }
  
  if(sketchname == 'p_12_256_1_41547199') {
    p_12_256_1_41547199();
  }
  
  if(sketchname == 'p_12_191_1_41547199') {
    p_12_191_1_41547199();
  }
  
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