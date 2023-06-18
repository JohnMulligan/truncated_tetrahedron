

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
let D_x=[951.056516295154, 916.7913563896467, 818.8007968971859, 670.639961193562, 492.202610087155, 306.226334448045, 134.3911659391342, -6.23842518047408, -105.7538344054213, -162.459703072703];
let D_y=[-309.016994374943, -294.795312091901, -252.853879190099, -185.326719283224, -95.649684316156, 11.614365146149, 131.007722997453, 256.4555313384356, 381.5748755483186, 499.999553602047];
let D_z=[0.0, -210.8435161426382, -397.647174140869, -540.269123268268, -625.627724382891, -649.537582419547, -616.890808282712, -540.180656060578, -436.6892918456655, -324.9201313633336];
let E_x=[587.785252292473, 522.9850183721097, 347.8418978177439, 113.565091656699, -113.867541311407, -275.018661680436, -334.5978326060198, -289.3423618050801, -164.2649053086101, -0.000669815628];
let E_y=[-809.016994374943, -754.609693218417, -598.867212724859, -362.900630242515, -77.7288431474126, 221.120021379918, 499.639630251153, 730.8534241638256, 898.7602277641316, 999.999724110497];
let E_z=[0.0, -335.1548764302862, -598.74043520187, -740.521731558934, -745.30991305621, -634.4496491028113, -455.255888020358, -263.116021723054, -103.4299674670755, -0.000290087354600267];
let F_x=[0.0, -23.4770351099333, -107.2968162189291, -272.128105871229, -505.130229928149, -736.494587208561, -860.8398755236958, -795.7322093029311, -537.6672427767201, -173.061439569609];
let F_y=[-1000.000000000003, -991.455488769022, -945.946911065903, -815.869888484036, -556.0630759713216, -157.179558784802, 334.831137381722, 824.3450532010177, 1196.6717348784146, 1361.803217239019];
let F_z=[0.0, -170.0812429078632, -365.608615763488, -573.113190203003, -736.5989168296504, -795.3701544936954, -734.314097349609, -604.868342711785, -495.5848342637955, -470.2281216565496];
let G_x=[-587.785252292477, -498.3216537796853, -321.6438100036731, -243.7049437576971, -365.171072448104, -606.006016797734, -780.2093763198704, -759.2851653672722, -567.5966084439706, -335.520627334623];
let G_y=[-809.016994374943, -908.1289636271105, -1122.534172099498, -1259.15984889838, -1143.8231866984227, -736.197376265971, -155.426891978487, 395.4858986119507, 750.0467972737916, 861.803369747248];
let G_z=[0.0, 216.6296175269808, 186.513034551185, -143.401489057426, -606.5393238514584, -967.6406141830875, -1101.889665765267, -1048.396751907417, -921.7261364518525, -795.1483827500176];
let H_x=[-951.056516295157, -706.6681540792093, -189.2490274941821, 180.9465586560599, 192.824872108927, -17.07260466709, -194.4632704080524, -235.14236597023918, -201.2830486836716, -162.460002623546];
let H_y=[-309.016994374943, -538.8281049650946, -1041.3432827278675, -1413.787499180775, -1365.6872026909696, -923.46576486572, -352.421252253865, 93.1017197046857, 346.3520625213906, 499.999430220894];
let H_z=[0.0, 666.2679420218398, 784.715067561282, 278.175790354055, -460.3104090785235, -974.9889444361417, -1094.0965483564146, -922.682212426403, -630.5029431463955, -324.9208412683066];
let I_x=[-951.056516295157, -563.0091788671083, 224.4458174841619, 734.5734385183619, 717.605931079071, 427.692061662235, 157.1778091196826, -16.28525074201518, -84.5922252104926, -0.000660350711];
let I_y=[309.016994374947, -35.1174476748505, -742.5062696576096, -1182.438459323454, -1042.2335541380096, -527.366329093242, -7.542018003, 374.6728859264857, 697.3618017189226, 999.998954695592];
let I_z=[0.0, 994.2979464777447, 1133.310859428719, 426.300436855323, -416.16758821193855, -809.8961226182677, -720.7697796654996, -417.919641788915, -135.3853551375135, -0.000160357638600267];
let J_x=[-587.785252292477, -126.3037184905553, 714.9545726604749, 1068.7525226706969, 784.7813307433782, 273.19199738321, -169.0626115469824, -433.8251704569362, -423.2675343864306, -173.061140018766];
let J_y=[809.016994374947, 396.2754317931725, -373.7359499581925, -710.711452051559, -435.0394108425296, 46.800608316499, 443.967890146633, 814.2072649695647, 1184.1932805677657, 1361.803340619434];
let J_z=[0.0, 1066.0930415169546, 1059.9922147721256, 207.750713507243, -509.80918835686765, -641.2898671785387, -453.0535081838036, -297.769917137616, -309.3398244866395, -470.2274117515216];
let K_x=[0.0, 424.2202116417777, 1039.822565904512, 973.1693535987544, 340.0262829809383, -322.483892901868, -761.4640824188474, -856.0613614690811, -620.1736891353496, -335.5206367993];
let K_y=[999.999999999997, 578.3028510449615, -117.3126315966935, -295.486247326996, -35.1430598503226, 211.530941021918, 432.2959940904373, 746.7284323528369, 948.4896983095766, 861.804139162195];
let K_z=[0.0, 852.1878469977786, 600.9999708113287, -239.92986279881, -665.5071883538207, -641.692942789905, -628.8098036653906, -744.008886075037, -845.6585718587195, -795.1485124791446];
let first_x=[-224.51398828979276, -224.51398828979276, -224.51398828979276, -224.51398828979276, -224.51398828979276, -224.51398828979276, -224.51398828979276, -224.51398828979276, -224.51398828979276, -224.51398828979276];
let first_y=[690.9830056250522, 690.9830056250522, 690.9830056250522, 690.9830056250522, 690.9830056250522, 690.9830056250522, 690.9830056250522, 690.9830056250522, 690.9830056250522, 690.9830056250522];
let first_z=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let B_C_x=[587.785252292473, 587.785252292473, 587.785252292473, 587.785252292473, 587.785252292473, 587.785252292473, 587.785252292473, 587.785252292473, 587.785252292473, 587.785252292473];
let B_C_y=[427.05098312484176, 427.05098312484176, 427.05098312484176, 427.05098312484176, 427.05098312484176, 427.05098312484176, 427.05098312484176, 427.05098312484176, 427.05098312484176, 427.05098312484176];
let B_C_z=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let D_E_x=[587.785252292473, 553.203832371236, 455.449963230763, 311.339892044244, 145.280532791524, -15.403240861024, -145.6516874917458, -227.3378515036541, -252.5005927251173, -224.514188734604];
let D_E_y=[-427.050983124843, -407.397101586882, -349.435466853463, -256.11522702591, -132.184612711734, 16.050657874222, 181.048220393747, 354.4128277068039, 527.323508754767, 690.982388718257];
let D_E_z=[0.0, -178.8594086671015, -330.221642265648, -431.685140880553, -470.037541394593, -443.545423967688, -361.9987083405225, -244.516242378313, -115.565081311128, -0.000400890515];
let F_G_x=[-224.513988289796, -201.9881519788903, -173.5362699719881, -221.674997709714, -395.431204347151, -653.147284951082, -872.9003044947888, -927.151409187805, -768.5299316273911, -463.678290415383];
let F_G_y=[-690.983005625053, -734.7099409453101, -829.087813155716, -882.103346056858, -793.2262644917796, -506.746503983614, -46.71151511717, 483.6150813725926, 939.0270859469988, 1190.98251897343];
let F_G_z=[0.0, 49.2667422144448, -8.041391660902, -200.332226733692, -457.999240685355, -665.9320929310804, -747.647668793863, -716.806334250575, -657.5097783705115, -649.8392816629856];
let H_I_x=[-726.542528005357, -489.9159339557397, 9.4288195229809, 365.1789452523999, 375.700225446065, 160.738673503023, -63.4190949025504, -202.80387537961818, -262.2970425786186, -224.51438917897];
let H_I_y=[-3e-12, -224.3487063489305, -716.884763620952, -1095.793503146598, -1099.834793712914, -765.5450520100418, -318.951025425694, 65.7304237829857, 381.1346835985576, 690.98177181163];
let H_I_z=[0.0, 670.6516240217788, 818.653485819763, 382.273244528269, -255.91585060717247, -676.0872355802414, -736.877845413155, -543.073113567866, -255.0492235346405, -0.000801781564600267];
let last_x=[-224.513988289796, 113.5961692119797, 687.2952473972349, 827.0030812215999, 468.534344574281, -52.775164066556, -514.2722677598234, -779.8298527657291, -730.3348087093776, -463.678089970854];
let last_y=[690.983005625057, 371.8215905711965, -207.2567158385215, -443.882812508115, -260.7131254484256, 27.934140273782, 305.02032137974, 673.1519963964397, 1053.9192405742876, 1190.983135879594];
let last_z=[0.0, 769.8700051404508, 717.329610913424, 80.244955093119, -385.32535924653496, -443.0791212783907, -366.90305756683665, -377.0302778387028, -495.4483876801705, -649.8388807714636];


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
