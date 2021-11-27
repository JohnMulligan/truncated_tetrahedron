

function setup() {
  createCanvas(650, 650, WEBGL);
  fill(204);
  
  
  
};

function draw() {

  background(0);
  
  
let ax = [0,109.807620968859,46.4101614245640,299.999999845480,16.9872977352831,-4.87463570874826e-7,-5.62876170874826e-7,-109.807621228527,-46.4101618022789,-300.000000261803,-16.9872976767090,1.08040700000000e-6];
let bx = [150.000000000000,150.000000000000,133.012701917973,340.192378665543,-6.21778265600687,-69.6152423686251,-150.000000435959,-150.000000007968,-133.012702116934,-340.192378516856,6.21778275195500,69.6152422257710];
let cx = [259.807621135332,259.807621135332,259.807621135332,340.192378742802,103.589838652698,10.7695156490509,-196.410161482971,-113.397459429330,-136.047190328587,-233.012701173469,26.2395691901730,96.4101592654100];
let dx = [300.000000000000,300.000000000000,300.000000000000,300.000000000000,236.602540474557,160.769515637098,-92.8203227084081,-36.6025400306309,-52.4791382289529,-85.6406454560840,23.0562752219470,53.5898351894220];
let ex = [259.807621135332,259.807621135332,259.807621135332,259.807621135332,259.807621135332,230.384757773943,57.1796772281331,3.58983887466007,34.1234021750801,-45.4482669185260,-0.148805188029000,-16.0254059737270];
let fx = [150.000000000000,150.000000000000,150.000000000000,150.000000000000,150.000000000000,150.000000000000,103.589838556584,-33.0127015741429,37.1578905755911,-152.627944053750,-20.1705916555340,-42.8203231381490];
let gx = [3.67394039744206e-14,3.67394039744206e-14,3.67394039744206e-14,3.67394039744206e-14,3.67394039744206e-14,3.67394039744206e-14,3.67394039744206e-14,-109.807620968859,-46.4101614245629,-299.999999845480,-16.9872977352820,8.30841000000000e-7];
let hx = [-150.000000000000,-150.000000000000,-150.000000000000,-150.000000000000,-150.000000000000,-150.000000000000,-150.000000000000,-150.000000000000,-133.012701917973,-340.192378665542,6.21778265600700,69.6152420117760];
let ix = [-259.807621135331,-259.807621135331,-259.807621135331,-259.807621135331,-259.807621135331,-259.807621135331,-259.807621135331,-259.807621135331,-259.807621135331,-340.192378742802,-103.589838652697,-10.7695170495020];
let jx = [-300.000000000000,-300.000000000000,-300.000000000000,-300.000000000000,-300.000000000000,-300.000000000000,-300.000000000000,-300.000000000000,-300.000000000000,-300.000000000000,-236.602540474557,-160.769517380927];
let kx = [-259.807621135332,-259.807621135332,-259.807621135332,-259.807621135332,-259.807621135332,-259.807621135332,-259.807621135332,-259.807621135332,-259.807621135332,-259.807621135332,-259.807621135332,-230.384758817546];
let lx = [-150.000000000000,-150.000000000000,-150.000000000000,-150.000000000000,-150.000000000000,-150.000000000000,-150.000000000000,-150.000000000000,-150.000000000000,-150.000000000000,-150.000000000000,-150.000000000000];
let mx = [173.205080756888,173.205080756888,173.205080756888,299.999999807774,26.7949193540941,-46.4101614245631,-173.205080919376,-173.205080628738,-173.205080767512,-299.999999432524,-26.7949192839960,46.4101602156250];
let nx = [236.602540378444,236.602540378444,236.602540378444,236.602540378444,236.602540378444,190.192378935028,-9.80762084300987,-52.0725938428019,-41.3889912925009,-67.5426476756750,-31.8160888816860,-21.1324894924210];
let ox = [63.3974596215559,63.3974596215559,63.3974596215559,63.3974596215559,63.3974596215559,63.3974596215559,63.3974596215559,-109.807620872747,-36.6025401971029,-236.602540256578,-63.3974591558610,-63.3974592946350];
let px = [-173.205080756888,-173.205080756888,-173.205080756888,-173.205080756888,-173.205080756888,-173.205080756888,-173.205080756888,-173.205080756888,-173.205080756888,-299.999999807774,-26.7949193540940,46.4101601218130];
let qx = [-236.602540378444,-236.602540378444,-236.602540378444,-236.602540378444,-236.602540378444,-236.602540378444,-236.602540378444,-236.602540378444,-236.602540378444,-236.602540378444,-236.602540378444,-190.192380779404];
let rx = [-63.3974596215565,109.807620872746,36.6025401971030,236.602540256578,63.3974591558631,63.3974590963883,63.3974592588750,-109.807621141614,-36.6025404896839,-236.602540772545,-63.3974591447150,-63.3974591447149];
let sx = [-63.3974596215565,-63.3974596215565,-63.3974596215565,-63.3974596215565,-63.3974596215565,-63.3974596215565,-63.3974596215565,-63.3974596215565,-63.3974596215565,-63.3974596215565,-63.3974596215565,-63.3974596215565];
let tx = [0,0,0,0,0,0,0,0,0,0,0,0];
let ay = [300.000000000000,329.422863361389,92.8203232712827,-160.769515149633,-236.602540127810,-300.000000178425,-300.000000103012,-329.422863383157,-92.8203237336108,160.769514725913,236.602539831339,299.999999313246];
let by = [259.807621135332,259.807621135332,196.410161609888,-10.7695151376815,-103.589838113726,-340.192378832015,-259.807620764682,-259.807620650002,-196.410161837355,10.7695145625661,103.589837524479,340.192377086712];
let cy = [150.000000000000,150.000000000000,150.000000000000,69.6152423925295,6.21778284823354,-340.192378576330,-133.012701444308,-110.769514967510,-195.299461461298,-98.3339506164155,-28.8675141365420,233.012699573633];
let dy = [1.83697019872103e-14,1.83697019872103e-14,1.83697019872103e-14,1.83697019872103e-14,-16.9872980820273,-299.999999667055,-46.4101613215501,-31.3466518527716,-90.5989229802659,-57.4374157531349,-28.3121636377060,85.6406441681410];
let ey = [-150.000000000000,-150.000000000000,-150.000000000000,-150.000000000000,-150.000000000000,-259.807620968860,-86.6025404230501,-100.961894332378,12.9909152409084,92.5625843345147,104.700538522766,45.4482661121690];
let fy = [-259.807621135332,-259.807621135332,-259.807621135332,-259.807621135332,-259.807621135332,-259.807621135332,-213.397459691916,-250.000000003984,11.8802150960164,201.666049725357,237.157890332024,152.627943417086];
let gy = [-300.000000000000,-300.000000000000,-300.000000000000,-300.000000000000,-300.000000000000,-300.000000000000,-300.000000000000,-329.422863361389,-92.8203232712831,160.769515149633,236.602540127810,299.999998896923];
let hy = [-259.807621135332,-259.807621135332,-259.807621135332,-259.807621135332,-259.807621135332,-259.807621135332,-259.807621135332,-259.807621135332,-196.410161609888,10.7695151376812,103.589838113726,340.192377235400];
let iy = [-150.000000000000,-150.000000000000,-150.000000000000,-150.000000000000,-150.000000000000,-150.000000000000,-150.000000000000,-150.000000000000,-150.000000000000,-69.6152423925293,-6.21778284823300,340.192377946101];
let jy = [-5.51091059616309e-14,-5.51091059616309e-14,-5.51091059616309e-14,-5.51091059616309e-14,-5.51091059616309e-14,-5.51091059616309e-14,-5.51091059616309e-14,-5.51091059616309e-14,-5.51091059616309e-14,-5.51091059616309e-14,16.9872980820270,300.000000318327];
let ky = [150.000000000000,150.000000000000,150.000000000000,150.000000000000,150.000000000000,150.000000000000,150.000000000000,150.000000000000,150.000000000000,150.000000000000,150.000000000000,259.807621935245];
let ly = [259.807621135331,259.807621135331,259.807621135331,259.807621135331,259.807621135331,259.807621135331,259.807621135331,259.807621135331,259.807621135331,259.807621135331,259.807621135331,259.807621135331];
let my = [173.205080756888,173.205080756888,173.205080756888,46.4101617060011,-26.7949189696425,-299.999999807774,-173.205080312961,-173.205080235085,-173.205080752999,-46.4101620879873,26.7949185058910,299.999998195603];
let ny = [-63.3974596215559,-63.3974596215559,-63.3974596215559,-63.3974596215559,-63.3974596215559,-236.602540115859,-36.6025403378211,-47.9274057212386,-8.05565819564364,18.0979981875305,27.6709007647230,67.5426469307180];
let oy = [-236.602540378444,-236.602540378444,-236.602540378444,-236.602540378444,-236.602540378444,-236.602540378444,-236.602540378444,-283.012701821860,-9.80762136817964,190.192378691295,236.602540297199,236.602539779287];
let py = [-173.205080756888,-173.205080756888,-173.205080756888,-173.205080756888,-173.205080756888,-173.205080756888,-173.205080756888,-173.205080756888,-173.205080756888,-46.4101617060013,26.7949189696420,299.999998570854];
let qy = [63.3974596215558,63.3974596215558,63.3974596215558,63.3974596215558,63.3974596215558,63.3974596215558,63.3974596215558,63.3974596215558,63.3974596215558,63.3974596215558,63.3974596215558,236.602540900314];
let ry = [236.602540378444,283.012701821860,9.80762136817800,-190.192378691296,-236.602540297200,-236.602540519163,-236.602540681650,-283.012702099929,-9.80762173474964,190.192378548111,236.602540295255,236.602540295255];
let sy = [236.602540378444,236.602540378444,236.602540378444,236.602540378444,236.602540378444,236.602540378444,236.602540378444,236.602540378444,236.602540378444,236.602540378444,236.602540378444,236.602540378444];
let ty = [300.000000000000,300.000000000000,300.000000000000,300.000000000000,300.000000000000,300.000000000000,300.000000000000,300.000000000000,300.000000000000,300.000000000000,300.000000000000,300.000000000000];
let az = [0,-132.867294833701,-153.421936962604,-265.734590109775,-76.7109687792743,-2.94917905208081e-7,1.70269029728323e-7,132.867294296550,153.421936966678,265.734590169516,76.7109692941588,1.73609634579464e-6];
let bz = [0,0,-76.7109684387351,-265.734589814859,-153.421937132874,-132.867295423534,-1.70270382682247e-7,-3.47599008665047e-7,76.7109679238492,265.734589755120,153.421937128799,132.867297516469];
let cz = [0,0,0,-132.867294833700,-153.421936962604,-265.734590109777,-76.7109687792752,-23.7344562411902,-78.5468355668910,238.820319018062,74.8751015619085,242.000136148259];
let dz = [0,0,0,0,-76.7109684387342,-265.734589814860,-153.421937132874,85.3983824830246,-157.093670187107,211.906048665532,-80.3827019267921,218.265679120794];
let ez = [0,0,0,0,0,-132.867294833701,-153.421936962604,218.265677221949,-80.3827014037578,211.906049020188,-157.093670020913,85.3983834351979];
let fz = [0,0,0,0,0,0,-76.7109684387348,242.000133384117,74.8751020849441,238.820319727375,-78.5468347114652,-23.7344553703918];
let gz = [0,0,0,0,0,0,0,132.867294833701,153.421936962604,265.734590109776,76.7109687792742,1.38849825503939e-6];
let hz = [0,0,0,0,0,0,0,0,76.7109684387349,265.734589814860,153.421937132874,132.867296979317];
let iz = [0,0,0,0,0,0,0,0,0,132.867294833701,153.421936962603,265.734591034179];
let jz = [0,0,0,0,0,0,0,0,0,0,76.7109684387342,265.734589645682];
let kz = [0,0,0,0,0,0,0,0,0,0,0,132.867294202320];
let lz = [0,0,0,0,0,0,0,0,0,0,0,0];
let mz = [0,0,0,-209.578263272435,-121.000066850922,-209.578263737622,-2.68575263362436e-7,-8.30973349893790e-8,-5.43578653912479e-7,209.578263178204,121.000066575919,209.578265577820];
let nz = [0,0,0,0,0,-209.578263272436,-121.000066850923,172.140712455971,-123.895871275772,167.125031592597,-123.895871550776,172.140713396479];
let oz = [0,0,0,0,0,0,0,209.578263272435,121.000066850922,209.578263737622,2.68575277573291e-7,7.29054604174639e-7];
let pz = [0,0,0,0,0,0,0,0,0,209.578263272435,121.000066850922,209.578265195731];
let qz = [0,0,0,0,0,0,0,0,0,0,0,209.578263005583];
let rz = [0,-209.578263272436,-121.000066850923,-209.578263737620,-2.68574737560812e-7,-6.72704013229894e-13,2.68573615412507e-7,209.578262890347,121.000067125924,209.578263831853,8.12151753848411e-7,8.12151738315459e-7];
let sz = [0,0,0,0,0,0,0,0,0,0,0,0];
let tz = [0,0,0,0,0,0,0,0,0,0,0,0];



 
background(0);
let steparray=[0,1,2,3,4,5,6,7,8,9,10,11,10,9,8,7,6,5,4,3,2,1];



let sec=floor(millis()/1000);

let t=steparray[sec % 22];



let angle=((sec*5)%360);



//let cam_x=350 * cos(angle);
//let cam_y=350*sin(angle);
let cam_x=350*cos(angle);
let cam_y=350*sin(angle);
console.log(angle,cam_x,cam_y);

camera(cam_x,cam_y,-900,0,0,0,0,1,0);


fill(127);





beginShape();
vertex(lx[t],ly[t],lz[t]);
vertex(sx[t],sy[t],sz[t]);
vertex(tx[t],ty[t],tz[t]);
endShape(CLOSE);
beginShape();
vertex(ax[t],ay[t],az[t]);
vertex(rx[t],ry[t],rz[t]);
vertex(mx[t],my[t],mz[t]);
endShape(CLOSE);
beginShape();
vertex(ax[t],ay[t],az[t]);
vertex(mx[t],my[t],mz[t]);
vertex(bx[t],by[t],bz[t]);
endShape(CLOSE);
beginShape();
vertex(bx[t],by[t],bz[t]);
vertex(mx[t],my[t],mz[t]);
vertex(cx[t],cy[t],cz[t]);
endShape(CLOSE);
beginShape();
vertex(cx[t],cy[t],cz[t]);
vertex(mx[t],my[t],mz[t]);
vertex(nx[t],ny[t],nz[t]);
endShape(CLOSE);
beginShape();
vertex(cx[t],cy[t],cz[t]);
vertex(nx[t],ny[t],nz[t]);
vertex(dx[t],dy[t],dz[t]);
endShape(CLOSE);
beginShape();
vertex(dx[t],dy[t],dz[t]);
vertex(nx[t],ny[t],nz[t]);
vertex(ex[t],ey[t],ez[t]);
endShape(CLOSE);
beginShape();
vertex(nx[t],ny[t],nz[t]);
vertex(ex[t],ey[t],ez[t]);
vertex(ox[t],oy[t],oz[t]);
endShape(CLOSE);
beginShape();
vertex(ex[t],ey[t],ez[t]);
vertex(ox[t],oy[t],oz[t]);
vertex(fx[t],fy[t],fz[t]);
endShape(CLOSE);
beginShape();
vertex(fx[t],fy[t],fz[t]);
vertex(ox[t],oy[t],oz[t]);
vertex(gx[t],gy[t],gz[t]);
endShape(CLOSE);
beginShape();
vertex(gx[t],gy[t],gz[t]);
vertex(hx[t],hy[t],hz[t]);
vertex(ox[t],oy[t],oz[t]);
endShape(CLOSE);
beginShape();
vertex(px[t],py[t],pz[t]);
vertex(ox[t],oy[t],oz[t]);
vertex(hx[t],hy[t],hz[t]);
endShape(CLOSE);
beginShape();
vertex(hx[t],hy[t],hz[t]);
vertex(ix[t],iy[t],iz[t]);
vertex(px[t],py[t],pz[t]);
endShape(CLOSE);
beginShape();
vertex(jx[t],jy[t],jz[t]);
vertex(ix[t],iy[t],iz[t]);
vertex(px[t],py[t],pz[t]);
endShape(CLOSE);
beginShape();
vertex(jx[t],jy[t],jz[t]);
vertex(px[t],py[t],pz[t]);
vertex(qx[t],qy[t],qz[t]);
endShape(CLOSE);
beginShape();
vertex(jx[t],jy[t],jz[t]);
vertex(qx[t],qy[t],qz[t]);
vertex(kx[t],ky[t],kz[t]);
endShape(CLOSE);
beginShape();
vertex(kx[t],ky[t],kz[t]);
vertex(qx[t],qy[t],qz[t]);
vertex(sx[t],sy[t],sz[t]);
endShape(CLOSE);
beginShape();
vertex(kx[t],ky[t],kz[t]);
vertex(lx[t],ly[t],lz[t]);
vertex(sx[t],sy[t],sz[t]);
endShape(CLOSE);


};

function polygon( x, y,  radius,  npoints) {
  var angle = 3 / npoints;
  beginShape();
  for (var a = 0; a < TWO_PI; a += angle) {
    var sx = x + cos(a) * radius;
    var sy = y + sin(a) * radius;
    vertex(sx, sy);
  }
  endShape(CLOSE);
};
