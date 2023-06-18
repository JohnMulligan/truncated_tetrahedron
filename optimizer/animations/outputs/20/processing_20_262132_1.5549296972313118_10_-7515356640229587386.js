

function setup() {
  createCanvas(1000, 800, WEBGL);
  fill(204);
  
  
  
}

function draw() {

  background(0);

let A_x=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let A_y=[1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0];
let A_z=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let B_x=[309.0169943749474, 309.0169943749474, 309.0169943749474, 309.0169943749474, 309.0169943749474, 309.0169943749474, 309.0169943749474, 309.0169943749474, 309.0169943749474, 309.0169943749474];
let B_y=[951.0565162951535, 951.0565162951535, 951.0565162951535, 951.0565162951535, 951.0565162951535, 951.0565162951535, 951.0565162951535, 951.0565162951535, 951.0565162951535, 951.0565162951535];
let B_z=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let C_x=[587.785252292473, 586.767467990588, 583.744419903526, 578.806120152423, 572.099608024317, 563.824571835336, 554.227403153988, 543.593860421766, 532.240560413843, 520.505550884069];
let C_y=[809.016994374947, 807.999210073062, 804.976161986, 800.037862234897, 793.331350106791, 785.05631391781, 775.459145236463, 764.825602504241, 753.472302496318, 741.737292966544];
let C_z=[0.0, -16.6207386255499, -32.7465900063543, -47.8974023068774, -61.6220557589798, -73.5118948819986, -83.2128963165259, -90.436209971157, -94.9667596165492, -96.669646841645];
let D_x=[809.016994374947, 812.247244439938, 821.226968849383, 833.916944785205, 847.219929212368, 857.394352346892, 860.561207238564, 853.24229079871, 832.863795668678, 798.162969270416];
let D_y=[587.785252292473, 593.291337242909, 609.030802674277, 632.763152546835, 661.062353984369, 689.7403205537269, 714.3670970084255, 730.8255049594688, 735.8337604161011, 727.3732130430221];
let D_z=[0.0, 14.1423426049611, 22.880943824211, 21.5619819665895, 6.9395147003035, -22.3395118115607, -65.483555435711, -119.5705598306181, -179.8285276154155, -240.151348227823];
let E_x=[951.056516295153, 962.165340544745, 993.118974325671, 1037.205371897069, 1084.516090903545, 1123.612052382514, 1143.407466294287, 1134.939452600118, 1092.730447810924, 1015.545565361185];
let E_y=[309.016994374947, 329.111194825702, 386.608270045839, 473.587558936841, 578.221508874633, 686.5744670591355, 784.654303180476, 860.3683635734048, 905.0735013244552, 914.5056007068761];
let E_z=[0.0, 89.1115644391686, 160.242957649665, 198.2648772767205, 193.2588465953905, 141.9927156092553, 48.291089351268, -77.7097879211786, -221.231433447573, -365.104314634208];
let F_x=[1000.0, 1021.035933543093, 1078.9035876234175, 1159.072638128272, 1240.98134749942, 1302.523297655389, 1324.642618279793, 1294.962152735887, 1209.703136487196, 1073.6584825287061];
let F_y=[0.0, 42.747328827468, 164.256683303552, 345.687023069886, 559.8226065110937, 776.2717291878132, 966.907083223735, 1110.3540978423018, 1194.673933812216, 1217.9153803728582];
let F_z=[0.0, 200.5429645930796, 362.944066191864, 456.4833695579125, 463.5680607925705, 382.4758436894203, 226.685907832598, 21.2186484001862, -202.9025759698638, -414.6256420701012];
let G_x=[951.056516295154, 982.7779725628825, 1068.3416476617404, 1181.7748884757366, 1288.25847047402, 1353.8358320090908, 1354.2086009548948, 1280.0693918018544, 1137.8071900888108, 946.0374131114231];
let G_y=[-309.016994374943, -236.220242131713, -31.484306375958, 267.6838430693541, 609.2002010964001, 938.6315596979922, 1210.786300900534, 1397.610193379338, 1490.8111821351522, 1499.4313820503191];
let G_z=[0.0, 336.9262120410806, 606.790078653059, 758.6208865078195, 768.8772388496735, 644.9511314111403, 420.427352194669, 144.3003637695772, -132.0458863993573, -366.1635862942979];
let H_x=[809.016994374947, 851.3433221112325, 962.6938164689074, 1102.0066788209099, 1217.7791155865316, 1265.993658641624, 1223.9391409188297, 1095.2161260344903, 905.3004230087458, 690.8003007572191];
let H_y=[-587.785252292477, -478.975501357124, -177.25126065086, 250.9352698075281, 717.4052660914791, 1137.0892145991402, 1448.931287357134, 1626.563949571696, 1677.092155762323, 1630.852743638879];
let H_z=[0.0, 484.1735691947866, 862.675791844247, 1060.6862526652985, 1053.8531884555084, 870.3070259400173, 576.003059222437, 250.5849584681652, -36.5107120593231, -241.7875049724179];
let I_x=[587.785252292473, 640.3085533596895, 774.5701078905824, 931.3822480791418, 1042.3167203168755, 1058.779543836126, 969.8153194742048, 801.9047085638763, 603.5667504520778, 424.1807437299221];
let I_y=[-809.016994374943, -660.442990871609, -255.6455894044132, 297.8798929455849, 864.8270852102521, 1326.9504285571552, 1615.565197298158, 1721.0403813286696, 1680.3014170871486, 1552.3308890232738];
let I_z=[0.0, 627.0750878605496, 1100.05895657947, 1318.6987977133256, 1266.8478421528296, 1007.7915613229324, 650.44223467352, 304.7105867189619, 46.1540258699014, -98.1375917528539];
let J_x=[309.016994374947, 371.4725492343325, 526.4247696201214, 694.7444868205678, 793.6714896986025, 778.859778357262, 662.0274166589928, 497.7225003677853, 351.1988684237978, 267.5958439351061];
let J_y=[-951.056516295153, -761.877986371141, -257.3102281342808, 401.6825826583039, 1024.747431637257, 1465.4569241071372, 1664.6629051132243, 1649.6063254639423, 1499.1776055545536, 1299.6242454170726];
let J_z=[0.0, 750.8697241886736, 1290.605768366572, 1495.0919352347014, 1369.2587766234376, 1026.4421107627522, 623.1844031819993, 288.6691625503764, 83.457972392444, -0.6312389175986];
let K_x=[0.0, 72.6047840019455, 247.8761678463654, 426.5478162681938, 516.9070358072375, 489.274552198202, 385.5880022043618, 283.8736728018093, 247.3868582336928, 292.353516468128];
let K_y=[-1000.0, -772.8027376509383, -182.04648731513382, 547.2296834731839, 1168.1828881702231, 1521.4159207756531, 1582.6633764955898, 1436.0285383346113, 1204.9091998595106, 987.8140493246657];
let K_z=[0.0, 842.770083949487, 1411.572760465606, 1564.182851849641, 1342.5253840012533, 922.0584200253822, 501.7583151607053, 207.7978128442582, 60.7392717324659, 6.32768867573668];
let L_x=[-309.016994374943, -225.4231306915775, -27.8284297357586, 165.8416299282078, 262.1832026721525, 255.240795092591, 216.8510353881248, 231.5076646103485, 332.9327492403957, 487.179251377795];
let L_y=[-951.056516295153, -692.0887701210065, -38.83776777111181, 713.3295601558979, 1269.137702728901, 1482.2250009528493, 1392.2152944531767, 1151.3662810807944, 913.1547650032745, 758.8969748695067];
let L_z=[0.0, 893.2832992371815, 1448.5214401217797, 1515.911920848257, 1191.4927330277644, 718.1485385871222, 319.7024679991473, 89.0031669592332, -13.0727712095861, -80.42986690008922];
let M_x=[-587.785252292477, -491.8263357467365, -267.7812127758546, -49.4152920290982, 75.6652675208255, 129.464797671663, 202.4225167271085, 358.0471202591895, 574.2137847901137, 763.350464420474];
let M_y=[-809.016994374943, -528.0734508374135, 155.2226885837762, 875.7980965033919, 1309.315169645122, 1356.7102760332184, 1145.9213789327448, 890.3292608626763, 738.5847807763265, 717.120617640374];
let M_z=[0.0, 897.191596351279, 1397.0416518516981, 1357.307382274294, 943.5334653470054, 460.6346171948702, 127.3016040807043, -28.1907221708508, -108.967243942671, -221.3949848296502];
let N_x=[-809.016994374943, -699.0866534126214, -443.3416698476516, -187.8815752565802, -8.8428963373795, 140.2723295016987, 346.2876757822255, 621.3912185705435, 876.3974317476757, 995.100281285635];
let N_y=[-587.785252292477, -297.6987783358075, 376.9720300951292, 1010.9798989004099, 1281.4336620853637, 1173.1386749074113, 911.8092505003617, 739.7668548380464, 749.8118249384012, 881.509704403329];
let N_z=[0.0, 854.0912668804573, 1263.2779689563831, 1111.4620322683231, 643.5868714553594, 207.5108689499932, -22.3021884534027, -104.7923878599857, -189.2540074874938, -352.3729140616192];
let O_x=[-951.056516295153, -825.7950835195585, -533.5550897239337, -229.3965504589715, 23.9746819844357, 285.2294472033777, 608.7102306717464, 933.9229966422985, 1120.7141372234078, 1076.8910908368457];
let O_y=[-309.016994374943, -24.7613551603765, 599.9424889426832, 1099.192517949635, 1190.5463292197285, 972.8520034765793, 754.5418587430997, 749.7725370118463, 942.4232463456382, 1177.202335595571];
let O_z=[0.0, 768.4343688517828, 1063.196283724505, 814.1709155424601, 346.0142472317034, 15.7828045345872, -87.787588237041, -115.3157632323737, -222.3773403310385, -413.7170151737249];
let P_x=[-1000.0, -858.8632508675274, -527.6536936357634, -167.9156437057337, 168.1702567158207, 531.6906381415157, 917.2077493620606, 1191.6603057169355, 1211.138235483932, 971.4758014917987];
let P_y=[0.0, 262.5456874378055, 797.5205460272322, 1127.5922100416506, 1053.1252807310166, 800.9564363565294, 717.5572497502347, 917.0173264444772, 1240.715503021795, 1469.541688835092];
let P_z=[0.0, 649.0688504160707, 820.6781353467051, 508.7195724392131, 104.7466384031554, -71.3708687989391, -51.0671978625732, -56.2596261398207, -195.3185253069371, -377.49151684043034];
let Q_x=[-951.056516295153, -794.8753718259386, -426.3418660039004, -12.3904654549057, 397.6103145513507, 824.1508533028547, 1186.5716626415215, 1308.8516123730276, 1112.1296507210964, 726.8599649494518];
let Q_y=[309.016994374947, 534.5449052039995, 946.1234925765682, 1092.0439844263265, 894.0762379342975, 696.1642423707704, 811.0707588946709, 1185.8573693140772, 1527.4485049997882, 1625.398006353734];
let Q_z=[0.0, 508.32459909464075, 564.6702345536971, 239.5816709921351, -36.4894379214506, -34.3224405308833, 77.7166258108968, 52.7275125684013, -118.7126957008358, -260.1933147574013];
let R_x=[-809.016994374943, -674.8492628205756, -346.9956818505214, 56.7100350943699, 518.7009709035807, 1048.6190388109187, 1490.7894530858005, 1562.2969724429965, 1159.5228030376268, 533.0787314857557];
let R_y=[587.785252292473, 745.3714127325275, 997.6722413762216, 975.1237750679114, 666.3887790943865, 481.13507460155034, 762.1922619053524, 1366.8893386917823, 1832.186679054366, 1860.316270522362];
let R_z=[0.0, 310.75718201873474, 266.4523997966591, -42.2724630508509, -213.6403381192846, -69.8675965001079, 132.0249669654763, 82.3896590167526, -171.3957270968841, -331.9513117122767];
let S_x=[-587.785252292477, -488.5795989967526, -235.81419043449242, 111.02309649261, 573.6167961832253, 1170.2257430881837, 1717.3068127478296, 1849.6403949623225, 1371.2242621638798, 538.6916235830442];
let S_y=[809.016994374947, 881.7763871276575, 946.4384344950383, 758.0176740042454, 370.0879454990945, 196.53536572002733, 588.9729466776424, 1395.6475315371245, 2061.3767112775413, 2164.65227367];
let S_z=[0.0, 99.60732360313872, -21.4724869510089, -260.9091471918599, -297.7654565695947, -24.0223940349628, 260.7569443971713, 202.7794064575286, -148.1279652136715, -404.3050264760623];
let T_x=[-309.016994374943, -300.7053087391106, -214.6771965831468, 53.925190339719, 584.4357211135194, 1350.3009082041497, 2021.8650698026486, 2090.2076809868504, 1404.2376329775916, 391.1321410639413];
let T_y=[951.056516295157, 924.0876159917044, 835.5325897823104, 573.7064969443044, 127.7749644241255, -45.22535234206466, 527.4652362152397, 1587.1189424132745, 2370.301336678327, 2431.98428028073];
let T_z=[0.0, -146.96919267911326, -313.2602325970299, -507.1939143485499, -495.3871595164287, -107.7580347159148, 297.472568089295, 260.6849081096629, -111.2137324816141, -336.13784397694315];
let U_x=[0.0, -130.6329082457366, -286.10758961763173, -106.270237111788, 549.1969607040274, 1548.2901538614876, 2320.3436989525903, 2203.9599190307144, 1245.5874175311747, 157.59807289002728];
let U_y=[1000.0, 867.9345516186102, 678.1923120388653, 449.0259225927884, -16.6341873274655, -189.70061499354367, 594.6578700912899, 1877.5993014652295, 2637.5415439869653, 2540.570742768264];
let U_z=[0.0, -403.50219126141627, -574.0833591794699, -745.2677407400658, -770.6891647123387, -302.2165765584458, 232.0307977643982, 236.8404799399692, -75.1617124810271, -158.4927298412711];
let first_x=[-146.55714625849524, -146.55714625849524, -146.55714625849524, -146.55714625849524, -146.55714625849524, -146.55714625849524, -146.55714625849524, -146.55714625849524, -146.55714625849524, -146.55714625849524];
let first_y=[925.3254041760194, 925.3254041760194, 925.3254041760194, 925.3254041760194, 925.3254041760194, 925.3254041760194, 925.3254041760194, 925.3254041760194, 925.3254041760194, 925.3254041760194];
let first_z=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let B_C_x=[425.32540417601933, 425.32540417601933, 425.32540417601933, 425.32540417601933, 425.32540417601933, 425.32540417601933, 425.32540417601933, 425.32540417601933, 425.32540417601933, 425.32540417601933];
let B_C_y=[834.7481064940806, 834.7481064940806, 834.7481064940806, 834.7481064940806, 834.7481064940806, 834.7481064940806, 834.7481064940806, 834.7481064940806, 834.7481064940806, 834.7481064940806];
let B_C_z=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let D_E_x=[834.748106494081, 842.609734729045, 864.822675352174, 897.446458002034, 934.477048976759, 968.620555787462, 992.242306330696, 998.376522158051, 981.674037509785, 939.172329957653];
let D_E_y=[425.325404176019, 437.398808081409, 472.121668891008, 525.181029793015, 589.964381900207, 658.351486325962, 721.6880580569812, 771.8257984888, 802.1053243351759, 808.1652103723816];
let D_E_z=[0.0, 56.9317211466449, 102.9471404501667, 128.5450656533266, 126.8835257923582, 94.7022120946064, 32.8108190326291, -53.9175081182227, -157.0494995452852, -265.534526654057];
let F_G_x=[925.32540417602, 951.5586452496021, 1023.5800392958145, 1122.9802127644625, 1224.039602574924, 1299.722796474975, 1327.645286854476, 1294.522661518989, 1198.149638363637, 1046.7190470894213];
let F_G_y=[-146.557146258497, -92.560712011035, 60.626525148038, 288.481799702178, 555.9144383683345, 824.3497969913656, 1058.974312768445, 1234.4620996900128, 1338.054598817752, 1369.670764373146];
let F_G_z=[0.0, 263.1523319172796, 478.07611082764, 606.4173271249575, 627.1314915513755, 539.7525074711883, 362.957334060919, 129.1644825289154, -123.1291846379916, -357.18121130395815];
let H_I_x=[662.459848116453, 708.3190031457885, 828.0627950981594, 975.3571110859567, 1093.6069274802599, 1137.1576073250687, 1086.562005335148, 952.4238158001064, 767.8608019195938, 574.3642787896681];
let H_I_y=[-662.459848116457, -541.815928728248, -209.13720661182, 257.4860390564439, 756.1642293692661, 1191.6256164578272, 1499.697524459337, 1658.1755536626429, 1682.7956332414951, 1612.8858134317402];
let H_I_z=[0.0, 535.6557724614876, 951.63121279065, 1165.4348411794435, 1154.5224630502914, 956.8075758479523, 650.873642031803, 325.8601536232282, 53.6730629804477, -127.0045158659599];
let J_K_x=[146.557146258495, 210.7974347970645, 368.8324242391404, 537.4232469261718, 633.4514304436755, 619.123867067884, 516.9540741892168, 389.4887663156933, 300.8159770418648, 284.5803074086731];
let J_K_y=[-925.325404176013, -729.5366851446479, -212.2178716228736, 449.5885706823989, 1052.1209477563511, 1447.9527744094262, 1590.5602371154966, 1525.9760604327225, 1347.5987050168944, 1145.2140591660068];
let J_K_z=[0.0, 764.7564162517806, 1304.266824053358, 1491.8769437211165, 1344.0493417124128, 991.3232302449705, 600.4289141480855, 296.17307901851706, 122.7096417671104, 53.4456948280651];
let L_M_x=[-425.325404176017, -340.7481664419745, -141.4005121425896, 54.9471324337098, 162.0465627456835, 186.009105298715, 204.6808701518608, 292.5775709259964, 459.1315493846248, 645.134711207019];
let L_M_y=[-834.748106494073, -580.1633158900423, 52.81146096433119, 756.9814417324409, 1238.9530569264289, 1375.4240669592903, 1238.1073401346137, 999.1656239386343, 807.6631243099046, 721.5684902799677];
let L_M_z=[0.0, 858.2387389564003, 1372.6459279265873, 1402.5443062434742, 1064.5406441007833, 613.9572433302882, 263.5071134333313, 76.3256715835082, -13.8906751696996, -107.11224552897932];
let N_O_x=[-834.748106494083, -724.3146408696675, -466.3016139371506, -201.3056065507262, 5.6514609891328, 206.0100728162607, 470.9250430509095, 779.9355393406455, 1018.3679598974157, 1074.022697123969];
let N_O_y=[-425.325404176017, -153.8202420010835, 463.1920590838392, 1007.1557536129719, 1187.354122422874, 1035.6971349453343, 804.8475404061877, 720.5271855217513, 828.4404626638539, 1025.795286582101];
let N_O_z=[0.0, 778.475079380986, 1125.096060048239, 947.5704105253451, 509.4442376527594, 145.5135740277802, -13.3572661524677, -65.4372629452165, -162.4734390238964, -349.5066561383942];
let P_Q_x=[-925.325404176023, -785.5122715029112, -455.3801904961688, -87.5259167696285, 272.5071179265737, 662.1236750533167, 1041.8462253897535, 1256.9172987220904, 1185.7113904377634, 878.9358066849367];
let P_Q_y=[146.557146258497, 377.8847686284725, 828.8400501399892, 1059.7136667400266, 933.0357479526315, 717.5784647024743, 736.401943876947, 1030.0388902779102, 1380.4752686067332, 1566.813346967922];
let P_Q_z=[0.0, 557.5711861985748, 676.2796527128111, 382.2866354991281, 62.9421423451084, -15.7774419777377, 54.599353977045, 43.8550249032963, -112.3970211264865, -282.46590836491595];
let R_S_x=[-662.459848116457, -563.3858558487796, -308.5381106530704, 40.3549804294129, 496.603638988747, 1077.5359040131648, 1604.8471251904964, 1725.9561592086495, 1273.4195660827104, 520.3144103318477];
let R_S_y=[662.459848116453, 768.0510152081835, 924.2387837755844, 843.3351867781975, 511.6657681989285, 319.6345615510733, 645.944913912613, 1365.0658507443263, 1944.4392167565572, 2001.565022448233];
let R_S_z=[0.0, 191.94288608302472, 124.3825757546901, -139.3269455048779, -264.9023143062946, -81.5591136051975, 155.105129435031, 98.7493002054052, -209.8949157660241, -415.26490343517435];
let last_x=[-146.557146258496, -215.6961487148986, -269.4209158959312, -65.313305747658, 516.6256911564843, 1410.7921538991527, 2168.4781097992595, 2171.1622015529906, 1334.5157874655852, 247.2333347278613];
let last_y=[925.325404176017, 846.3543251077957, 718.9907926070244, 502.2395579639174, 63.2290538983325, -127.78010675831466, 532.1156198254826, 1719.4125720585594, 2516.150824474349, 2496.303216580769];
let last_z=[0.0, -264.3841430953453, -415.6146515923269, -595.1140489282029, -630.6310786127457, -236.5245447192908, 223.0529281000054, 205.91216364597204, -141.5795611207095, -289.1112520401043];


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
vertex(J_K_x[t],J_K_y[t],J_K_z[t]);
endShape(CLOSE);
beginShape();
vertex(J_x[t],J_y[t],J_z[t]);
vertex(J_K_x[t],J_K_y[t],J_K_z[t]);
vertex(K_x[t],K_y[t],K_z[t]);
endShape(CLOSE);
beginShape();
vertex(J_K_x[t],J_K_y[t],J_K_z[t]);
vertex(K_x[t],K_y[t],K_z[t]);
vertex(L_x[t],L_y[t],L_z[t]);
vertex(L_M_x[t],L_M_y[t],L_M_z[t]);
endShape(CLOSE);
beginShape();
vertex(L_x[t],L_y[t],L_z[t]);
vertex(L_M_x[t],L_M_y[t],L_M_z[t]);
vertex(M_x[t],M_y[t],M_z[t]);
endShape(CLOSE);
beginShape();
vertex(L_M_x[t],L_M_y[t],L_M_z[t]);
vertex(M_x[t],M_y[t],M_z[t]);
vertex(N_x[t],N_y[t],N_z[t]);
vertex(N_O_x[t],N_O_y[t],N_O_z[t]);
endShape(CLOSE);
beginShape();
vertex(N_x[t],N_y[t],N_z[t]);
vertex(N_O_x[t],N_O_y[t],N_O_z[t]);
vertex(O_x[t],O_y[t],O_z[t]);
endShape(CLOSE);
beginShape();
vertex(N_O_x[t],N_O_y[t],N_O_z[t]);
vertex(O_x[t],O_y[t],O_z[t]);
vertex(P_x[t],P_y[t],P_z[t]);
vertex(P_Q_x[t],P_Q_y[t],P_Q_z[t]);
endShape(CLOSE);
beginShape();
vertex(P_x[t],P_y[t],P_z[t]);
vertex(P_Q_x[t],P_Q_y[t],P_Q_z[t]);
vertex(Q_x[t],Q_y[t],Q_z[t]);
endShape(CLOSE);
beginShape();
vertex(P_Q_x[t],P_Q_y[t],P_Q_z[t]);
vertex(Q_x[t],Q_y[t],Q_z[t]);
vertex(R_x[t],R_y[t],R_z[t]);
vertex(R_S_x[t],R_S_y[t],R_S_z[t]);
endShape(CLOSE);
beginShape();
vertex(R_x[t],R_y[t],R_z[t]);
vertex(R_S_x[t],R_S_y[t],R_S_z[t]);
vertex(S_x[t],S_y[t],S_z[t]);
endShape(CLOSE);
beginShape();
vertex(R_S_x[t],R_S_y[t],R_S_z[t]);
vertex(S_x[t],S_y[t],S_z[t]);
vertex(T_x[t],T_y[t],T_z[t]);
vertex(last_x[t],last_y[t],last_z[t]);
endShape(CLOSE);
beginShape();
vertex(T_x[t],T_y[t],T_z[t]);
vertex(U_x[t],U_y[t],U_z[t]);
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