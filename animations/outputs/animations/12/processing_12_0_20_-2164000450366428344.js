

function setup() {
  createCanvas(1000, 800, WEBGL);
  fill(204);
  
  
  
}

function draw() {

  background(0);

let A_x=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let A_y=[1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0];
let A_z=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let B_x=[499.99999999999994, 499.99999999999994, 499.99999999999994, 499.99999999999994, 499.99999999999994, 499.99999999999994, 499.99999999999994, 499.99999999999994, 499.99999999999994, 499.99999999999994, 499.99999999999994, 499.99999999999994, 499.99999999999994, 499.99999999999994, 499.99999999999994, 499.99999999999994, 499.99999999999994, 499.99999999999994, 499.99999999999994, 499.99999999999994];
let B_y=[866.0254037844387, 866.0254037844387, 866.0254037844387, 866.0254037844387, 866.0254037844387, 866.0254037844387, 866.0254037844387, 866.0254037844387, 866.0254037844387, 866.0254037844387, 866.0254037844387, 866.0254037844387, 866.0254037844387, 866.0254037844387, 866.0254037844387, 866.0254037844387, 866.0254037844387, 866.0254037844387, 866.0254037844387, 866.0254037844387];
let B_z=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let C_x=[866.025403784439, 865.864241868985, 865.380963907927, 864.576192989279, 863.450966700425, 862.006735790356, 860.245362299231, 858.169117157655, 855.78067725878, 853.083122006998, 850.079929347681, 846.77497128308, 843.172508880172, 839.277186776889, 835.0940271938, 830.628423458995, 825.886133054486, 820.873270193116, 815.596297935528, 810.062019857378];
let C_y=[500.0, 499.956816794903, 499.827322855518, 499.611685137775, 499.310181662374, 498.923201156337, 498.45124255182, 497.894914342846, 497.254933800772, 496.532126049519, 495.727423001739, 494.841862157311, 493.876585265689, 492.832836853854, 491.711962621755, 490.515407707297, 489.244714823135, 487.901522267663, 486.487561812761, 485.004656471031];
let C_z=[0.0, 9.29185515604656, 18.5717303666926, 27.827661132225, 37.0477138243921, 46.220001072374, 55.3326970891151, 64.3740529182552, 73.3324115820045, 82.1962231104304, 90.9540594327798, 99.5946291116372, 108.106791900922, 116.479573108956, 124.702177748082, 132.76400445259, 140.654659147011, 148.363968447147, 155.881992776568, 163.199039181664];
let D_x=[1000.0, 999.35544231186, 997.423679144893, 994.210432166896, 989.725210781323, 983.981272199357, 976.995565812849, 968.788662138519, 959.384666678694, 948.8111191169907, 937.0988783384107, 924.2819938317738, 910.3975640981992, 895.485582751808, 879.5887730579241, 862.7524117093047, 845.0241426921348, 826.4537821404573, 807.0931151199964, 786.9956853199669];
let D_y=[0.0, 0.086390518567, 0.345739774322, 0.778579147948, 1.385788552213, 2.168587884024, 3.128525126297, 4.267461168247, 5.587551431604, 7.091224408833, 8.781157237329, 10.660248450863, 12.731588066121, 14.998425177811, 17.464133250697, 20.132173310607, 23.006055249227, 26.089297469084, 29.385385105436, 32.897727070953];
let D_z=[0.0, 25.38063291436356, 50.6974513185129, 75.8868832701782, 100.8858408238476, 125.6319591870474, 150.0638324821161, 174.1212450085682, 197.7453969237735, 220.8791232877224, 243.4671054510358, 265.4560738038242, 286.795000946408, 307.43528439107, 327.330917956498, 346.438651073394, 364.718135280354, 382.132057253372, 398.646257779788, 414.229836157979];
let E_x=[866.025403784439, 864.630216338832, 860.452633950369, 853.516536281884, 843.861522707772, 831.542614116335, 816.629839208887, 799.207709025378, 779.37458442666, 757.2419422159767, 732.9335464770797, 706.5845325347648, 678.3404116972221, 648.356005610968, 616.7943196418571, 583.8253651840497, 549.6249411882299, 514.3733854876264, 478.2543066825713, 441.4533074207579];
let E_y=[-500.0, -499.366929716395, -497.468613346416, -494.307737606079, -489.888791184025, -484.218080694981, -477.303752439762, -469.155819406748, -459.786192801898, -449.208717256683, -437.439208737574, -424.495494068832, -410.397450883892, -395.167046741204, -378.828376079028, -361.407693641618, -342.933442987055, -323.436278685349, -302.949080834559, -281.50696056249];
let E_z=[0.0, 43.94637620442216, 87.6973842430976, 131.0589690994559, 173.839690877749, 215.8520045294695, 256.9135064853441, 296.8481376685372, 335.4873327923785, 372.6711063719384, 408.2490664974458, 442.0813481223492, 474.039458402198, 504.007027474265, 531.880458982684, 557.569475620402, 580.997555967015, 602.102259940117, 620.835441236042, 637.163346203016];
let F_x=[500.0, 497.863294017256, 491.474884146556, 480.899634505945, 466.2447885616, 447.658686753608, 425.328996407791, 399.480478688745, 370.372323745084, 338.2950911019987, 303.5672976771247, 266.5317004518048, 227.5513247509311, 187.005292213276, 145.2845048265691, 102.7872428278217, 59.9147348144598, 17.06675807573031, -25.36267404939767, -66.9894830224831];
let F_y=[-866.02540378444, -864.296194671232, -859.115459248323, -850.503847377017, -838.495689085873, -823.138864579199, -804.494621510482, -782.63733883742, -757.654236456743, -729.645029753738, -698.721528202056, -665.007177221946, -628.636542654505, -589.754737440102, -548.516790401601, -505.086957426633, -459.637975814713, -412.3502630985695, -363.4110622580596, -313.0135359077247];
let F_z=[0.0, 60.00404419836636, 119.5748281500055, 178.2836271296762, 235.7107281985463, 291.4497888554691, 345.1120215013238, 396.3301497811036, 444.7620863163065, 490.0942855396714, 532.0447302253788, 570.3655157883032, 604.845002414635, 635.309511483651, 661.624549440279, 683.695549171085, 701.468125908241, 714.927851625238, 724.099558681955, 729.0461900174224];
let G_x=[0.0, -2.465664909907, -9.818572327915, -21.927258859573, -38.575264494149, -59.465044893524, -84.223337535456, -112.40787365244, -143.515301240077, -176.9901607530703, -212.2347349782443, -248.6195784011622, -285.4945194989029, -322.199922025658, -358.0779886306939, -392.4838920697123, -424.7965257417452, -454.4286760983297, -480.83643432397764, -503.5276831820401];
let G_y=[-1000.0, -996.715169340019, -986.884475321196, -970.579109701327, -947.9170531434, -919.0620720181881, -884.2223243511795, -843.648585375518, -797.6321061896093, -746.5021220782879, -690.6230301322753, -630.3912588770005, -566.2318556762444, -498.5948206787695, -427.951218989563, -354.789105526494, -279.609299619178, -202.9210487627975, -125.2376229990246, -47.0718830970877];
let G_z=[0.0, 69.24203302990583, 137.7170843155292, 204.6699705150987, 269.3688854818617, 331.1165445336277, 389.260688569093, 443.2037560475113, 492.4115485363274, 536.4207368407107, 574.8450791576971, 607.3802496710164, 633.8072048903035, 653.9940451698402, 667.8963595216768, 675.5560723672505, 677.0988405593835, 672.7300771952705, 662.7297048123806, 647.4457639589205];
let H_x=[-500.0, -502.014595670804, -507.987468512168, -517.707785468525, -530.830469318377, -546.885479325561, -565.29043766791, -585.366248562987, -606.355274781218, -627.4415671458643, -647.7725886808983, -666.4818378017612, -682.7117553306618, -695.636298572077, -704.4825820421889, -708.5510179850922, -707.2334392702383, -700.0287509090597, -686.5557320921166, -666.5626958321961];
let H_y=[-866.02540378444, -861.068369366786, -846.254824672514, -821.756651560578, -787.857685279927, -744.9498029464721, -693.5275273987515, -634.181225220942, -567.5889985183383, -494.5073895426899, -415.7610352085882, -332.2314246413335, -244.8449268815774, -154.5602674875485, -62.355641785836, 30.784341286843, 123.88168761164, 215.9778213870245, 306.1459696710534, 393.5029403763723];
let H_z=[0.0, 69.1798736559752, 137.22244898392097, 203.01533477826533, 265.4953194599569, 323.67139256101507, 376.6459346461528, 423.6335474906008, 463.9770635489499, 497.1603537021548, 522.8176424558031, 540.7391373730657, 550.8728815420848, 553.3228411762452, 548.3433418951267, 536.3300638085216, 517.8078943912865, 493.4160167557965, 463.8906771242297, 430.0461273386654];
let I_x=[-866.02540378444, -866.650876885904, -868.435736136517, -871.109029521965, -874.231454426193, -877.213288684321, -879.338524328992, -879.794280991673, -877.704376660894, -872.1657787860313, -862.2865544394313, -847.2238881848172, -826.2207419542299, -798.639791823286, -763.9933890590937, -721.9684520779392, -672.4453950322534, -615.5104291706369, -551.4608252701166, -480.8029890132651];
let I_y=[-500.0, -493.777974325489, -475.222050991254, -444.660450936145, -402.632791170495, -349.8791290865451, -287.3249628727815, -216.062517378075, -137.3287261581413, -52.4803926291429, 37.03292541884875, 129.6977146802175, 223.9663597820556, 318.2874014314335, 411.135543246374, 501.040760357247, 586.615887069691, 666.5820997041285, 739.7917633050854, 805.2481760352923];
let I_z=[0.0, 59.83425633303358, 118.22456351933296, 173.77138485322303, 225.1624939145441, 271.21289990992926, 310.9004536746868, 343.3959484292995, 368.0867336468441, 384.5930997256548, 392.7769559573421, 392.7426039673767, 384.8296923225508, 369.5987142710672, 347.8096689718418, 320.39473734113454, 288.4260183393065, 253.0795233055425, 215.5967298653667, 177.2450500746534];
let J_x=[-1000.0, -998.466941873084, -993.776886384661, -985.66326339079, -973.7017148482769, -957.3388852407878, -935.9305910629165, -908.787365821501, -875.2249872921241, -834.6173274142105, -786.4487354061117, -730.3631773673181, -666.2075092270959, -594.066545466474, -514.2879878540487, -427.4957749001542, -334.5909776179074, -236.73997108764698, -135.35022330990267, -32.0346320819631];
let J_y=[0.0, 6.535799703402, 25.967618149539, 57.773766325178, 101.101451283745, 154.7912733474079, 217.4104678956545, 287.293877784605, 362.5914089371957, 441.3205278334641, 521.4222116872587, 600.8186647267095, 677.4710702750245, 749.4356595821645, 814.916444107783, 872.313075920054, 920.26246702026, 957.6730070764964, 983.7504631485084, 998.0149161944593];
let J_z=[0.0, 43.714549158470774, 85.85630696851956, 124.92082437680413, 159.53724952078858, 188.52755589567178, 210.9570930102391, 226.1742230026785, 233.8373255075671, 233.9280500924288, 226.7503406700091, 212.9154171305617, 193.3135432801748, 169.0740055697662, 141.5152455384828, 112.08750625326452, 82.3106507607885, 53.7099765842365, 27.7528794519607, 5.7891136457244];
let K_x=[-866.02540378444, -862.069192031837, -850.14604703151, -830.100685913942, -801.7011877442369, -764.6772457224448, -718.7697160862105, -663.78778330183, -599.6694475422, -526.5407142115835, -444.7688481232077, -355.0053480327702, -258.2148812260759, -155.687254341963, -49.0305308336807, 59.8554298324308, 168.8245161708396, 275.547299590121, 377.5885692429163, 472.4957440744769];
let K_y=[500.0, 505.534965206702, 521.90195721663, 548.39683044009, 583.877500395688, 626.8098234155459, 675.3291724407305, 727.315188870742, 780.4766577442397, 832.4430500646741, 880.8590186376588, 923.4780328022475, 958.2513965597255, 983.4091105020095, 997.529400472736, 999.594228536118, 989.0287024364478, 965.7229815239251, 930.0360099068458, 882.7811591283703];
let K_z=[0.0, 25.149013982233978, 48.86298659947106, 69.79836181952074, 86.78907077435609, 98.92190048936958, 105.5967264664911, 106.5680242237245, 101.9652064917581, 92.2906064830228, 78.3952636865171, 61.4339840060157, 42.8023599767028, 24.0594759220172, 6.84082597141778, -7.23350558267148, -16.6501390058846, -20.0880087814145, -16.4935332674315, -5.1412659903151];
let L_x=[-500.0, -494.081442588022, -476.349627725051, -446.885121443596, -405.8511953557839, -353.5339578470888, -290.3921168967115, -217.110631275304, -134.65176995014804, -44.2969345177555, 52.3269731633173, 153.2418651941888, 256.1372123999851, 358.415118671201, 457.2615500505933, 549.7414113198688, 632.9131425329176, 703.956761534442, 760.3079459589953, 799.7899366556859];
let L_y=[866.02540378444, 869.234516885298, 878.588634152247, 893.283655082527, 912.030452967552, 933.1285265133549, 954.5634572526515, 974.122891856793, 989.5247702870387, 998.5508657347041, 999.1784253175997, 989.7028152499381, 968.8445725806857, 935.8351181990339, 890.476543677412, 833.172282008674, 764.9270308550508, 687.3159296806882, 602.4246088822558, 512.7632413891783];
let L_z=[0.0, 9.122635752058876, 17.239516811805657, 23.45074303667914, 27.05954980237759, 27.65310368005117, 25.16017302632, 19.8808161977041, 12.4853841835239, 3.9824927500596, -4.3420005509325, -11.0107595432652, -14.4593273490665, -13.1515137143024, -5.69740025672682, 9.03466232989292, 31.8202654374635, 63.002537201073, 102.4427565514305, 149.5016920960289];
let M_x=[0.0, 6.688845508981, 26.619457771325, 59.377305060028, 104.2503420997051, 160.2019101716652, 225.8415195633505, 299.401000483535, 378.724027178523, 461.2765620972585, 544.1843500790033, 624.3013356530538, 698.3099885585061, 762.851281709823, 814.6787918981832, 850.8284162542128, 868.7928238009036, 866.688245028799, 843.4007189260217, 798.6995465516376];
let M_y=[1000.0, 999.97840693847, 999.657472722109, 998.290688631521, 994.7054856909809, 987.4052480972493, 974.7017105725322, 954.8681965277045, 926.3026124711917, 887.688345088821, 838.1412635107957, 777.3319053892011, 705.5735592448337, 623.8692322430079, 533.913253004973, 438.046311357638, 339.1658700923768, 240.59688281121018, 145.9304128772478, 58.8398928047453];
let M_z=[0.0, -0.0613832011810128, -0.470022804068544, -1.47055000827206, -3.11416194893321, -5.19027976683353, -7.1891047332879, -8.3004434747378, -7.4505661257585, -3.37505219635211, 5.27806815734798, 19.8237076492957, 41.404811349254, 70.8596073197394, 108.60363826010818, 154.53818533831392, 207.9946176629005, 267.721246348202, 331.9157016353925, 398.3020077920309];
let first_x=[-211.32486540518747, -211.32486540518747, -211.32486540518747, -211.32486540518747, -211.32486540518747, -211.32486540518747, -211.32486540518747, -211.32486540518747, -211.32486540518747, -211.32486540518747, -211.32486540518747, -211.32486540518747, -211.32486540518747, -211.32486540518747, -211.32486540518747, -211.32486540518747, -211.32486540518747, -211.32486540518747, -211.32486540518747, -211.32486540518747];
let first_y=[788.6751345948124, 788.6751345948124, 788.6751345948124, 788.6751345948124, 788.6751345948124, 788.6751345948124, 788.6751345948124, 788.6751345948124, 788.6751345948124, 788.6751345948124, 788.6751345948124, 788.6751345948124, 788.6751345948124, 788.6751345948124, 788.6751345948124, 788.6751345948124, 788.6751345948124, 788.6751345948124, 788.6751345948124, 788.6751345948124];
let first_z=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let B_C_x=[577.3502691896259, 577.3502691896259, 577.3502691896259, 577.3502691896259, 577.3502691896259, 577.3502691896259, 577.3502691896259, 577.3502691896259, 577.3502691896259, 577.3502691896259, 577.3502691896259, 577.3502691896259, 577.3502691896259, 577.3502691896259, 577.3502691896259, 577.3502691896259, 577.3502691896259, 577.3502691896259, 577.3502691896259, 577.3502691896259];
let B_C_y=[577.3502691896257, 577.3502691896257, 577.3502691896257, 577.3502691896257, 577.3502691896257, 577.3502691896257, 577.3502691896257, 577.3502691896257, 577.3502691896257, 577.3502691896257, 577.3502691896257, 577.3502691896257, 577.3502691896257, 577.3502691896257, 577.3502691896257, 577.3502691896257, 577.3502691896257, 577.3502691896257, 577.3502691896257, 577.3502691896257];
let B_C_z=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let D_E_x=[788.675134594813, 787.9126501426412, 785.6278816131844, 781.8288712526326, 776.5289820823477, 769.7468370286435, 761.5062341297748, 751.836038242827, 740.770049790246, 728.346851200057, 714.609631804752, 699.605992070895, 683.387728134067, 666.010597711381, 647.534068555926, 628.021050703696, 607.537613843325, 586.15269121198, 563.937771486578, 540.966580197822];
let D_E_y=[-211.324865405191, -211.120482257291, -210.507140338763, -209.484264824129, -208.050906318771, -206.20575377665, -203.947152477263, -201.273126954721, -198.181408742144, -194.669468765726, -190.734554194755, -186.37372952691, -181.583921662359, -176.361968695652, -170.704672131411, -164.608852208283, -158.071405995892, -151.089367911476, -143.659972286841, -135.780717602085];
let D_E_z=[0.0, 25.37763792801356, 50.6735145912649, 75.8062269763449, 100.6950868071532, 125.2604735090561, 149.4241819127899, 173.1097629864622, 196.2428559195245, 218.7515099266504, 240.5664941918278, 261.6215944334022, 281.853894638911, 301.204042594142, 319.616497913303, 337.039761366325, 353.426584394494, 368.734157806445, 382.924278752452, 395.963495185479];
let F_G_x=[211.324865405187, 209.392746488852, 203.620728635157, 194.08150093175, 180.895124826375, 164.227420865476, 144.287744403339, 121.326183868916, 95.630223804998, 67.5209228192787, 37.3486636792067, 5.4885389271838, -27.6645595084109, -61.701074257294, -96.2020647685189, -130.7445610853693, -164.9069120052412, -198.2740514059567, -230.44260863945567, -261.0257921753521];
let F_G_y=[-788.67513459481, -786.741756568964, -780.95089007371, -771.330294455616, -757.9260905656, -740.802543470375, -720.041757882344, -695.74328601466, -668.023647584104, -637.015761773499, -602.868291136539, -565.744897691719, -525.823411814437, -483.2949150005446, -438.3627381414777, -391.2413776165444, -342.1553322672406, -291.3378651603916, -239.0296949609349, -185.4776227041376];
let F_G_z=[0.0, 50.70620486081823, 100.9554093189026, 150.2960540327006, 198.2873841801509, 244.5046589658091, 288.5441333153674, 330.027741571746, 368.607417806126, 403.9689931959748, 435.8356176975872, 463.9706608340564, 488.1800546984309, 508.31405109161324, 524.2683739223509, 535.9847574333221, 543.4508703207041, 546.6996352224485, 545.8079622033849, 540.8949236100476];
let H_I_x=[-577.35026918963, -578.570893920235, -582.166113862977, -587.938046173849, -595.563755013127, -604.605332594428, -614.523575488872, -624.694836111739, -634.430533051846, -642.9987243112453, -649.6470871009593, -653.6266084225342, -654.2152733743899, -650.741043327987, -642.6034434346589, -629.2931272299833, -610.4088535885002, -585.6713955216456, -554.9339983515334, -518.1891132664205];
let H_I_y=[-577.35026918962, -572.779240116473, -559.128672766967, -536.585150045845, -505.456403579845, -466.1665089808951, -419.2492685763705, -365.339889088382, -305.1650897735963, -239.5318025741079, -169.31464945366625, -95.4424028985505, -18.8836531661294, 59.3680800861645, 138.309543975358, 216.943002506855, 294.29128505687, 369.4123804336675, 441.4133310611824, 509.4631936999013];
let H_I_z=[0.0, 50.60815775561612, 100.1751961454401, 147.6861139077963, 192.1774137727835, 232.7610464976563, 268.646247819263, 299.1586678364063, 323.7562752570164, 342.0416172838937, 353.7701264106201, 358.8542844117874, 357.3635774400455, 349.5203003726752, 335.6913893866818, 316.3765753550055, 292.1932535029985, 263.8585537187565, 232.1691683540807, 197.9795482653784];
let J_K_x=[-788.67513459481, -786.4909995112846, -779.8730109474374, -768.630197803659, -752.46319706625, -730.991463891736, -703.789087185615, -670.4270862727, -630.519667563574, -583.7716644322503, -530.0242828340013, -469.2963347568642, -401.8183576583489, -328.057378118064, -248.7305616257597, -164.8065706146092, -77.4940973330764, 11.78228849662701, 101.41817166305933, 189.6757753429419];
let J_K_y=[211.32486540519, 216.390826027269, 231.422986767315, 255.929597801369, 289.108939355389, 329.8754861503389, 376.8952990157685, 428.629456319807, 483.3840698923357, 539.3652122436721, 594.7369216343938, 647.6803544781575, 696.4521240087176, 739.4399011408696, 775.213456642715, 802.569489402508, 820.568807756081, 828.5647015361255, 826.2216519303809, 813.5238631807745];
let J_K_z=[0.0, 25.181733304561575, 49.11911796182056, 70.63166919025603, 88.66341686265208, 102.33729685872727, 111.0005609714738, 114.2589476798525, 111.9979351899731, 104.3900606874548, 91.8880000944991, 75.2038228471347, 55.2755281938998, 33.2225971234962, 10.29282505174178, -12.19689167559748, -32.9228770310925, -50.6170544703095, -64.1263796611063, -72.4665192149396];
let last_x=[-211.324865405191, -206.04542386761, -190.265128332264, -164.165024028686, -128.0691050136119, -82.4744880860468, -28.0875657892455, 34.139239717194, 102.97609136417896, 176.8956912828225, 254.0699446853423, 332.3875438415538, 409.4950556809841, 482.862138345272, 549.8693884456363, 607.9152141568208, 654.5362223870056, 687.534068617891, 705.1006835502733, 705.933358115109];
let last_y=[788.67513459481, 790.072411771663, 794.042812648084, 799.936923491077, 806.721087429987, 813.0473749394629, 817.3455733308255, 817.9316530629121, 813.1261664853072, 801.3754200053158, 781.3680696113765, 752.1400328990395, 713.1612730569636, 664.3990515753555, 606.353604159079, 540.063787248388, 467.0819757613198, 389.4192633669202, 309.4637203346458, 229.8760010298893];
let last_z=[0.0, -0.0974787109377228, -0.762170620462044, -2.47475977316126, -5.55095912106541, -10.07855897328243, -15.8760582500669, -22.4771432352945, -29.1430866149679, -34.9027662808422, -38.6176459224549, -39.0669128917093, -35.0462097236601, -25.4721673961718, -9.48434946437722, 13.46370736049602, 43.5319284653449, 80.4458406022825, 123.4778091010715, 171.4595923508359];


let sec=floor(millis()/1000);
let steparray=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1];
let t=steparray[sec%38];

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
vertex(last_x[t],last_y[t],last_z[t]);
endShape(CLOSE);
beginShape();
vertex(L_x[t],L_y[t],L_z[t]);
vertex(M_x[t],M_y[t],M_z[t]);
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
