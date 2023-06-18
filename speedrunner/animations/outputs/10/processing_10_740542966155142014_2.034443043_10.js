

function setup() {
  createCanvas(1000, 800, WEBGL);
  fill(204);
  
  
  
}

function draw() {

  background(0);

let A_x=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let A_y=[1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0];
let A_z=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let B_x=[587.7852522924732, 587.7852522924732, 587.7852522924732, 587.7852522924732, 587.7852522924732, 587.7852522924732, 587.7852522924732, 587.7852522924732, 587.7852522924732, 587.7852522924732];
let B_y=[809.0169943749474, 809.0169943749474, 809.0169943749474, 809.0169943749474, 809.0169943749474, 809.0169943749474, 809.0169943749474, 809.0169943749474, 809.0169943749474, 809.0169943749474];
let B_z=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let C_x=[951.056516295153, 941.814706920499, 914.559511644446, 870.67770307562, 812.402033154485, 742.697628418478, 665.1111212879322, 583.5901937294599, 502.2827151023877, 425.325694262993];
let C_y=[309.016994374947, 309.016994374947, 309.016994374947, 309.016994374947, 309.016994374947, 309.016994374947, 309.016994374947, 309.016994374947, 309.016994374947, 309.016994374947];
let C_z=[0.0, -81.4196321895832, -158.696549033287, -227.898820839445, -285.505364232078, -328.585098525633, -354.946082150799, -363.24704091535, -353.065613426404, -324.919841276231];
let D_x=[951.056516295154, 975.8447504020533, 1043.148463311335, 1133.309329241757, 1218.333873677532, 1268.020900528612, 1256.697372281904, 1169.175309516927, 1004.6921412213857, 777.997540230119];
let D_y=[-309.016994374943, -294.795312091902, -252.853879190098, -185.326719283223, -95.649684316156, 11.614365146148, 131.007722997453, 256.4555313384356, 381.5748755483187, 499.999553602047];
let D_z=[0.0, 45.9328940905318, 64.310209157048, 34.045701825333, -54.355561600143, -196.09680788303, -372.3936661855586, -553.755245520137, -705.607999071747, -795.147703469983];
let E_x=[587.785252292473, 675.9091338328712, 909.99158612617, 1210.3938199395245, 1477.30343813838, 1626.229203908635, 1615.9530188817862, 1458.602399841107, 1209.1904760391626, 940.457413123589];
let E_y=[-809.016994374943, -754.609693218417, -598.867212724859, -362.900630242516, -77.7288431474125, 221.120021379916, 499.639630251153, 730.8534241638246, 898.7602277641327, 999.999724110492];
let E_z=[0.0, 329.7909080211098, 558.789764168742, 620.979683368907, 506.518416566851, 261.899046514987, -30.3236315571126, -283.302643537069, -436.042137434427, -470.228282011263];
let F_x=[0.0, 165.1042463941552, 580.907291399904, 1053.4183160084285, 1379.8818762525327, 1450.793511110847, 1289.4918860176442, 1013.9940179121679, 755.2165314220757, 587.785712199971];
let F_y=[-1000.000000000003, -881.71401585515, -557.9912999661009, -111.94920824039, 348.2869223133745, 723.161756459133, 949.693555295331, 1014.4888526849996, 948.6978259922635, 809.017611281501];
let F_z=[0.0, 653.6564192844799, 1080.324708319909, 1163.518240718331, 943.53743000755, 576.76794809361, 239.5663544214324, 38.940031563932, -19.653010364429, -0.000129730772];
let G_x=[-587.785252292477, -346.9307968965028, 218.559392854646, 761.1748110767985, 1004.8540666258868, 921.224663324679, 689.3129658810172, 508.00310330926493, 443.1943548261057, 425.325524442349];
let G_y=[-809.016994374943, -623.943474285225, -150.4307874595979, 409.592132199272, 837.8783935654815, 1004.036043244934, 913.1944931935936, 678.2466393251626, 443.3402063464145, 309.017270263272];
let G_z=[0.0, 884.6119855546448, 1371.124364983003, 1320.216598360626, 903.2839266327821, 426.326990482004, 96.6709607258034, -74.551728244027, -190.597003614565, -324.919131371952];
let H_x=[-951.056516295157, -795.7581190911358, -360.730264887661, 205.3654064212855, 618.8334325532188, 653.300133552852, 366.3146744082422, 40.72576877806892, -121.6470419182613, -162.459743165129];
let H_y=[-309.016994374943, -219.931901524903, 62.6283516165031, 526.914713143081, 1042.8236255398656, 1382.096316322402, 1375.8751695628187, 1066.7533190150307, 692.3492395349995, 500.000228760518];
let H_z=[0.0, 753.1026886306438, 1339.575879455762, 1563.68595772085, 1340.2639412915821, 835.292621699647, 348.7913816962094, 38.055836865364, -160.3528444353854, -324.91916199912066];
let I_x=[-951.056516295157, -997.1747790385508, -870.623298354397, -264.2131603257215, 533.9951045300542, 921.167998207964, 728.1258444679293, 319.1110630689689, 56.5923092678867, -8.0182616e-05];
let I_y=[309.016994374947, 164.51056502672, -24.1273621893023, 166.181971695563, 797.3832797430495, 1470.500442496507, 1753.8254242616676, 1592.2328381279597, 1256.6847106707476, 1000.000740289417];
let I_z=[0.0, 313.1011769770808, 1001.273423369153, 1740.699714671206, 1901.091460234323, 1385.199458182518, 677.7477518172514, 206.397495896994, 17.7544854442006, -0.0001603594426551034];
let J_x=[-587.785252292477, -868.5174910507858, -1059.083537046974, -352.033232859105, 818.9478919928972, 1450.738162252852, 1318.1351909112611, 921.986794762717, 663.6497407050697, 587.785332467108];
let J_y=[809.016994374947, 371.605132634976, -367.8152526266363, -445.580181716799, 300.0451187840055, 1178.790779989543, 1570.0661980424777, 1459.6814189878817, 1141.3386742856555, 809.018228191825];
let J_z=[0.0, -254.8118036501302, 523.437276087701, 1739.8548699485566, 2132.2249148036303, 1513.367025857198, 668.3920509377689, 175.7872905925452, 29.69509167853, 0.0001603545789994636];
let K_x=[0.0, -462.5884123850898, -832.956547125852, -2.825550505134, 1243.2502958105692, 1700.139219131195, 1391.7418052454007, 937.255599960423, 629.1920932534746, 425.326194256991];
let K_y=[999.999999999997, 316.3582490728299, -798.5530619136213, -923.36133942874, -46.9931725664135, 805.453036382486, 1056.5044727379527, 869.6375699853296, 549.6834657220845, 309.017546153222];
let K_z=[0.0, -717.5594413538842, 142.258137978125, 1561.6831236740586, 1846.746534359112, 1088.650587187259, 332.53131807575994, -7.4642608120738, -145.584102642419, -324.918841285662];
let first_x=[-224.51398828979276, -224.51398828979276, -224.51398828979276, -224.51398828979276, -224.51398828979276, -224.51398828979276, -224.51398828979276, -224.51398828979276, -224.51398828979276, -224.51398828979276];
let first_y=[690.9830056250522, 690.9830056250522, 690.9830056250522, 690.9830056250522, 690.9830056250522, 690.9830056250522, 690.9830056250522, 690.9830056250522, 690.9830056250522, 690.9830056250522];
let first_z=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let B_C_x=[587.785252292473, 587.785252292473, 587.785252292473, 587.785252292473, 587.785252292473, 587.785252292473, 587.785252292473, 587.785252292473, 587.785252292473, 587.785252292473];
let B_C_y=[427.05098312484176, 427.05098312484176, 427.05098312484176, 427.05098312484176, 427.05098312484176, 427.05098312484176, 427.05098312484176, 427.05098312484176, 427.05098312484176, 427.05098312484176];
let B_C_z=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let D_E_x=[587.785252292473, 634.813615745343, 765.490812918396, 950.7332331334202, 1148.769258779525, 1313.764159267375, 1405.3373438890233, 1397.043979004716, 1282.0980029206057, 1075.165756543879];
let D_E_y=[-427.050983124843, -407.397101586882, -349.435466853463, -256.11522702591, -132.184612711734, 16.050657874222, 181.048220393747, 354.4128277068039, 527.323508754767, 690.982388718256];
let D_E_z=[0.0, 175.9968627659568, 308.187760098117, 361.998427155859, 319.441170744509, 183.094314556705, -24.111968114467, -263.2758636280978, -487.201594486893, -649.838923094567];
let F_G_x=[-224.513988289796, -71.1013770753898, 310.707502770479, 733.7984221017825, 1014.135971490377, 1071.317994660713, 954.1791542765671, 782.6103068620159, 654.7214414666547, 587.785452737679];
let F_G_y=[-690.983005625053, -583.050955353815, -292.946344742026, 90.691108655913, 456.5546954117755, 709.855271982719, 803.007448034494, 746.3873495094084, 596.3355721894967, 427.051600031851];
let F_G_z=[0.0, 623.5679915480678, 1028.931326594249, 1111.768273205424, 923.386593589607, 618.232434538008, 348.8668192846474, 182.052560735796, 88.234026577945, 0.000400890007];
let H_I_x=[-726.542528005357, -691.3654812687708, -489.851114898091, -34.3112838652835, 480.6685755607378, 701.055400935886, 507.8064937693382, 136.84891271234991, -125.8701705810983, -224.513809010652];
let H_I_y=[-3e-12, -24.720693647357, 1.4941438473511, 252.826927872416, 739.7820401681404, 1232.321719579703, 1442.4164168389707, 1283.2903759844505, 940.4575925503685, 690.983557403439];
let H_I_z=[0.0, 441.8266130357028, 985.332391889181, 1448.234652622082, 1527.2781214436382, 1183.409036650231, 697.2886718078134, 337.672388326601, 130.030426602404, 0.000358564315];
let last_x=[-224.513988289796, -513.5654821700468, -750.296759243328, -155.6756392119355, 874.4636426453592, 1432.903368218073, 1323.1793568739122, 970.0026829206449, 713.0625665418847, 587.785653179879];
let last_y=[690.983005625057, 261.4769599017827, -473.4708392152803, -592.607575112641, 52.4776056251165, 829.188880841837, 1188.4674119504366, 1100.1088199898936, 781.0532907337625, 427.052216941403];
let last_z=[0.0, -343.0098235388552, 324.979077399523, 1447.067105930605, 1846.696699721246, 1360.532258921238, 684.3594111809385, 295.3701249984709, 146.5319385719496, 0.0008017801935598396];


let sec=floor(millis()/1000);
let steparray=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1];
let t=steparray[sec%18];

background(0)

let angle=((sec*5)%360);




//adapted from
//from https://discourse.processing.org/t/how-to-rotate-around-a-sphere/25072/24
//and math.fandom.com/wiki/Ellipsoid
//and Simon Greenwold.

  let latitude = (frameCount%360)*3.141/180;
  let longitude = (((frameCount-(latitude/2))/5)%360)*3.141/180;
  let radius=5000;
  
  let cam_x = radius * cos(latitude)*cos(longitude);
  let cam_y = radius * cos(latitude)*sin(longitude);
  let cam_z = radius * sin(latitude);
  camera(cam_x, cam_y, cam_z, 0, 0, 0, 0, 1, 0);

/**
 * Points and Lines. 
 * 
 * Points and lines can be used to draw basic geometry.
 * Change the value of the variable 'd' to scale the form.
 * The four variables set the positions based on the value of 'd'. 
 */




//let cam_x=350 * cos(angle);
//let cam_y=350*sin(angle);
//let cam_x=350*cos(angle);
//let cam_y=350*sin(angle);
//console.log(angle,cam_x,cam_y);

//camera(cam_x,cam_y,-900,0,0,0,0,1,0);


fill(127);

beginShape();
vertex(A_x[t],A_y[t],A_z[t]);
vertex(B_x[t],B_y[t],B_z[t]);
vertex(B_C_x[t],B_C_y[t],B_C_z[t]);
vertex(first_x[t],first_y[t],first_z[t]);
endShape(CLOSE);
beginShape();
vertex(B_x[t],B_y[t],B_z[t]);
vertex(B_C_x[t],B_C_y[t],B_C_z[t]);
vertex(C_x[t],C_y[t],C_z[t]);
endShape(CLOSE);
beginShape();
vertex(B_C_x[t],B_C_y[t],B_C_z[t]);
vertex(C_x[t],C_y[t],C_z[t]);
vertex(D_x[t],D_y[t],D_z[t]);
vertex(D_E_x[t],D_E_y[t],D_E_z[t]);
endShape(CLOSE);
beginShape();
vertex(D_x[t],D_y[t],D_z[t]);
vertex(D_E_x[t],D_E_y[t],D_E_z[t]);
vertex(E_x[t],E_y[t],E_z[t]);
endShape(CLOSE);
beginShape();
vertex(D_E_x[t],D_E_y[t],D_E_z[t]);
vertex(E_x[t],E_y[t],E_z[t]);
vertex(F_x[t],F_y[t],F_z[t]);
vertex(F_G_x[t],F_G_y[t],F_G_z[t]);
endShape(CLOSE);
beginShape();
vertex(F_x[t],F_y[t],F_z[t]);
vertex(F_G_x[t],F_G_y[t],F_G_z[t]);
vertex(G_x[t],G_y[t],G_z[t]);
endShape(CLOSE);
beginShape();
vertex(F_G_x[t],F_G_y[t],F_G_z[t]);
vertex(G_x[t],G_y[t],G_z[t]);
vertex(H_x[t],H_y[t],H_z[t]);
vertex(H_I_x[t],H_I_y[t],H_I_z[t]);
endShape(CLOSE);
beginShape();
vertex(H_x[t],H_y[t],H_z[t]);
vertex(H_I_x[t],H_I_y[t],H_I_z[t]);
vertex(I_x[t],I_y[t],I_z[t]);
endShape(CLOSE);
beginShape();
vertex(H_I_x[t],H_I_y[t],H_I_z[t]);
vertex(I_x[t],I_y[t],I_z[t]);
vertex(J_x[t],J_y[t],J_z[t]);
vertex(last_x[t],last_y[t],last_z[t]);
endShape(CLOSE);
beginShape();
vertex(J_x[t],J_y[t],J_z[t]);
vertex(K_x[t],K_y[t],K_z[t]);
vertex(last_x[t],last_y[t],last_z[t]);
endShape(CLOSE);

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
