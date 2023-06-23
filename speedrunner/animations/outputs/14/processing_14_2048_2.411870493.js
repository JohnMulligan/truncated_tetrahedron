function p_14_2048_2_411870493(){


  background(0);

let A_x=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let A_y=[1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0];
let A_z=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let B_x=[433.8837391175581, 433.8837391175581, 433.8837391175581, 433.8837391175581, 433.8837391175581, 433.8837391175581, 433.8837391175581, 433.8837391175581, 433.8837391175581, 433.8837391175581, 433.8837391175581, 433.8837391175581, 433.8837391175581, 433.8837391175581, 433.8837391175581];
let B_y=[900.9688679024191, 900.9688679024191, 900.9688679024191, 900.9688679024191, 900.9688679024191, 900.9688679024191, 900.9688679024191, 900.9688679024191, 900.9688679024191, 900.9688679024191, 900.9688679024191, 900.9688679024191, 900.9688679024191, 900.9688679024191, 900.9688679024191];
let B_z=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let C_x=[781.83148246803, 779.256160460805, 771.606439031228, 759.108794669787, 742.133230736787, 721.182323199074, 696.876341442318, 669.934884669809, 641.155577557767, 611.390455900358, 581.52074136741, 552.430752189533, 524.9817221669346, 499.9863031123663, 478.1845056050173];
let C_y=[623.489801858734, 622.249592144798, 618.565680463366, 612.547132144013, 604.372131413935, 594.282706102789, 582.577562203537, 569.603240428196, 555.74385657617, 541.409729460243, 527.025233070149, 513.016232620698, 499.797476450928, 487.76031704779, 477.261124723869];
let C_z=[0.0, -33.1016629765276, -65.2233231478254, -95.4139915228319, -122.779847760247, -146.510702477768, -165.903983595854, -180.385536579977, -189.52662277255, -193.056612564483, -190.870997614276, -183.034484906103, -169.779081044669, -151.497223502914, -128.730162177812];
let D_x=[974.927912181824, 982.668332089844, 1004.345156531845, 1035.525410292372, 1069.464465665686, 1097.990023234075, 1112.586577604817, 1105.549226224488, 1071.06666974846, 1006.10085114081, 910.95401596506, 789.450322060618, 648.7042224072256, 498.4963959150576, 350.3243007993443];
let D_y=[222.520933956314, 230.718085090636, 254.43345250654, 291.139169988401, 336.94504225401, 387.043259167755, 436.256470264928, 479.6253004634506, 512.9668699889396, 533.3393897774648, 539.3590226086787, 531.3326206344865, 511.1916224706763, 482.2357692066297, 448.717630671255];
let D_z=[0.0, 25.1120090620683, 41.0907123062406, 40.0594031563291, 16.501446096945, -31.92434629364, -103.9572177498883, -194.7514666489618, -296.338824440172, -398.485037330127, -489.842333060756, -559.263800116145, -597.125755965552, -596.502306331028, -554.052747011349];
let E_x=[974.927912181824, 989.2844192783731, 1031.0077638007417, 1095.9689440682691, 1177.065045088955, 1264.140723805243, 1344.293026220884, 1402.787040343398, 1424.670182423121, 1396.970699585086, 1311.156207569126, 1165.372137841874, 965.9288260359966, 727.5857089725256, 472.3845745738633];
let E_y=[-222.520933956311, -208.016063664153, -165.037805929773, -95.281677655343, -1.817127425995, 110.689096202929, 235.897449677375, 366.0094641026836, 492.3471147103705, 606.2741752702718, 700.3287979919467, 769.3519797985155, 811.3603087060573, 827.9373447561798, 824.004203045054];
let E_z=[0.0, 99.481615097615, 187.3618062196986, 252.3982171450361, 284.315881661257, 274.807760775183, 218.8904998107047, 116.3809613957762, -26.891898847114, -198.576201013604, -380.347121094564, -549.6806232927655, -682.738692204498, -757.966765270373, -759.779610490999];
let F_x=[781.83148246803, 797.7275793665501, 845.2502404469348, 923.1117946400042, 1026.965522260946, 1147.429235470667, 1269.3389088709348, 1373.0727125584071, 1437.9453197465616, 1446.783637010494, 1390.2427689938795, 1269.441857648215, 1096.0804571174986, 890.0848101656416, 675.6538707728143];
let F_y=[-623.489801858726, -602.64996237672, -540.040368237536, -435.938525553905, -292.37401613317, -114.682758696462, 87.563116045036, 300.8366548937642, 509.2804903948356, 697.2908308266614, 852.3103161246717, 967.0003236479415, 1040.1904819739284, 1076.4288442174218, 1084.400523243892];
let F_z=[0.0, 174.5304476340274, 338.7866554856956, 480.7303919836171, 586.158708090469, 640.387054096207, 631.7355917680917, 555.6210186073941, 417.62952438481, 234.201922129822, 30.395131593472, -164.75609849839256, -323.907856121273, -426.442586661788, -461.555510450692];
let G_x=[433.883739117558, 447.8618016670621, 491.2711715544057, 566.5076460821642, 672.132116035794, 798.575627999998, 927.4021482815097, 1035.2578066827223, 1100.9800978291187, 1112.564392449707, 1070.7708426972445, 987.946769222213, 883.0159088657426, 775.2035715004556, 679.1737916063151];
let G_y=[-900.968867902426, -871.058214073801, -781.347255301081, -633.173846237646, -432.195652639835, -191.1309942874027, 69.776150117758, 325.4542450733531, 551.1235612049194, 727.8662731425807, 846.4807827704691, 908.3154174988628, 923.1540647808663, 905.3727617687377, 869.987339902645];
let G_z=[0.0, 234.6404485558162, 459.3356879863626, 659.5989853735241, 815.517440181529, 905.941364972333, 916.0332171466257, 844.3030717681622, 705.320088773833, 526.47731125379, 340.178877203778, 174.91854167580746, 48.876584975792, -31.975374012597, -71.585176755989];
let H_x=[0.0, 12.49600090991711, 53.2952695973657, 128.3857054352182, 237.776309413474, 369.183480122188, 499.4913513672157, 603.6611288239652, 665.3722041102957, 682.6549778349089, 665.5725765330735, 628.465004335806, 582.3492027108906, 531.9633157075965, 478.0791098304022];
let H_y=[-1000.000000000006, -957.3836450725265, -831.5426339058439, -630.4453630241014, -371.9426169383641, -85.4330041386947, 191.952310289532, 424.2441774013327, 586.63387490393, 671.6220554452389, 688.548572562815, 657.4198501235068, 600.6599120863733, 536.6591463320187, 477.126108406184];
let H_z=[0.0, 267.3024094450868, 520.32583036039, 737.7269873847273, 891.4573449575423, 956.0670311980375, 921.2867840320781, 799.2795098579616, 621.3734107811277, 426.094307730641, 245.6587932447092, 98.19475670193185, -11.6157077814083, -86.258999062574, -128.8847923192565];
let I_x=[-433.88373911756, -417.7679021565569, -364.4667997247403, -265.6557728764558, -122.829027175332, 45.856527336429, 212.1265831238917, 352.0991480302522, 456.3716393658407, 527.9524841505129, 571.4247558051223, 583.7875358880273, 554.790867462223, 475.88975508575766, 350.3224757092432];
let I_y=[-900.968867902426, -843.6614776060325, -678.6831669959229, -428.5352616407274, -132.8766386829241, 156.4773494422593, 389.416080208296, 534.5314781458437, 589.297381299724, 577.0819272024789, 533.163494977264, 488.4569124559308, 459.6049897833853, 448.5748906984173, 448.8288045866726];
let I_z=[0.0, 265.7192038696911, 507.2452720047256, 692.7171159733766, 787.1812045437013, 768.9806163310695, 644.7152494572251, 449.1144840361506, 228.4689263764008, 19.65665347745, -160.6095044491528, -311.09452166694217, -432.8119936714603, -518.877981429067, -554.2549478658495];
let J_x=[-781.831482468032, -753.3897186183009, -662.6139891088253, -502.6552654612758, -282.435646581837, -30.8949358035339, 217.42806685364317, 440.1695091894389, 630.0302906837896, 781.9238765872959, 880.5184700889284, 902.7316001435743, 833.402700376168, 679.7202336188096, 472.4888428040472];
let J_y=[-623.489801858726, -553.5578948843955, -359.1397752862899, -85.3259577614504, 200.6421143771939, 429.4715123884053, 557.637482320619, 586.3469357260119, 557.1253527549271, 525.8087883055667, 532.4811654665061, 586.0454730499202, 669.2132078476533, 755.3808823616573, 824.2079028392546];
let J_z=[0.0, 230.2203052651318, 423.2063615391764, 537.4725397705116, 539.4853575982833, 425.9854791959055, 232.7253001419721, 15.9620466238526, -180.0281942950932, -342.188425591676, -480.8014381574308, -605.7356942014982, -709.4021339068163, -768.648843812356, -759.7499004586045];
let K_x=[-974.927912181822, -924.5247772503839, -770.2060551686403, -514.6711336873853, -184.7225227642604, 172.2834726995951, 512.5893941935692, 811.9980210541929, 1056.6845838031647, 1225.459623123352, 1290.1840868805884, 1236.8001056882704, 1083.933454056057, 879.0505032611567, 675.7201129927192];
let K_y=[-222.520933956311, -147.4449834721595, 51.0563499608751, 300.79329788184464, 510.9235461396729, 614.9126376428183, 607.566361278837, 546.8174388215284, 514.1392830487606, 562.0376738945097, 687.1697322740262, 843.5545163391583, 978.0171120084713, 1059.0953861788173, 1084.4151954856227];
let K_z=[0.0, 168.1932217738162, 288.2050639589384, 316.4978726084106, 235.7752281452073, 76.1392450048295, -96.59090365625289, -225.3743178844444, -299.1104186998742, -347.26519512108234, -401.3798169645457, -463.7864423286251, -509.5603103793433, -511.574519986398, -461.3349546762125];
let L_x=[-974.927912181822, -895.558969198856, -661.6428660751303, -298.2587382099464, 135.8299235303416, 567.09519179586, 941.3631333531412, 1231.686736690931, 1417.7697930405986, 1475.9067449090378, 1399.2703179013283, 1220.9701050163114, 1005.820815505727, 815.3138843051261, 679.1104479575681];
let L_y=[222.520933956314, 290.1630165349545, 454.3043793658401, 619.1320786996226, 688.4774069923359, 632.212370577522, 512.7722250543253, 441.0215568953014, 492.4350533782693, 654.5127244376135, 845.7556147199941, 979.6144776324413, 1015.5439585665916, 965.7468745341314, 869.7927046498806];
let L_z=[0.0, 92.54611681362739, 134.3631810075674, 93.1408491989696, -16.7777759272627, -128.5231352701115, -168.9056085213685, -121.7843689038874, -39.8640835675752, 8.80624210952768, -0.1155944307177, -40.34888850061315, -73.0372116992493, -81.125959792574, -71.4786269714335];
let M_x=[-781.831482468032, -672.520231984103, -362.7556197442403, 84.5420718193926, 566.1070687190056, 981.9643275935351, 1276.77240979843, 1432.9739165860028, 1443.678855994238, 1317.196214940253, 1100.9581373072003, 872.5383902079014, 692.7766942295979, 571.18806523643, 477.9737337723721];
let M_y=[623.489801858734, 668.1975708916535, 754.6566925263871, 778.4308711252926, 670.6495560349416, 473.8526538533151, 323.4355646598293, 336.0790253738894, 508.21829458470324, 723.4526509723767, 852.9489167563628, 845.5582206503203, 736.7727046548335, 596.4249077584244, 476.9911900998386];
let M_z=[0.0, 19.02155214879439, -1.7146134888456, -68.5678356876864, -129.0542661364617, -99.0602013246317, 54.06190144426151, 261.0116609644196, 404.1425311906288, 418.83126378694766, 330.0667241603153, 201.90412828222784, 76.4694113048407, -35.6712183884956, -129.039521414898];
let N_x=[-433.88373911756, -301.824103890996, 55.3393535189777, 523.9921825344456, 954.2752959413236, 1236.5985043103292, 1341.264024011033, 1288.1575933911508, 1115.066570551631, 886.2528640601608, 687.3597230539364, 572.2219975932545, 520.3608320102579, 463.34749083832605, 350.3207178098311];
let N_y=[900.968867902429, 907.9876937869375, 880.6483655529421, 733.0228221565973, 463.7309783267496, 208.6528984430461, 139.7841680547243, 298.5681913769885, 549.7043276284022, 709.380695523306, 701.7058390976028, 587.8635161393682, 476.1458554022916, 430.2055181252634, 448.9400870287274];
let N_z=[0.0, -37.07962229350341, -87.6503793559126, -122.2704750692547, -61.4347883991857, 151.7241482135093, 454.2809170050015, 680.1577382028206, 701.3884548189428, 529.0677033032827, 265.8471992270803, -1.72732227172815, -240.4038758290163, -434.1731496493486, -554.457089607987];
let O_x=[0.0, 139.385594502938, 493.1617962513447, 894.1125874263956, 1163.3601306092467, 1220.339693391339, 1100.6985134009299, 889.1131134933889, 677.293839571266, 554.8657943141969, 563.4774231714894, 648.1643255997294, 695.4209295180169, 631.6804947287401, 472.5931328281021];
let O_y=[999.999999999999, 959.631795171682, 802.3013196059796, 495.9252476551323, 140.7378598314936, -48.1373149200649, 59.036255941932, 352.2869306598662, 585.9172852805582, 624.4372001324846, 540.1260829615518, 488.1027928943205, 546.338032545594, 682.7047069454204, 824.4115716701074];
let O_z=[0.0, -64.08245604202511, -102.9968195428642, -52.5719080589328, 162.2195017714903, 514.8449291990933, 819.8903725576275, 869.7363876023315, 629.9327209465669, 244.41093315519169, -129.8893575603947, -428.74351036632817, -643.5034723602123, -759.7041368710896, -759.720054952326];
let first_x=[-193.09642971379355, -193.09642971379355, -193.09642971379355, -193.09642971379355, -193.09642971379355, -193.09642971379355, -193.09642971379355, -193.09642971379355, -193.09642971379355, -193.09642971379355, -193.09642971379355, -193.09642971379355, -193.09642971379355, -193.09642971379355, -193.09642971379355];
let first_y=[846.010735815048, 846.010735815048, 846.010735815048, 846.010735815048, 846.010735815048, 846.010735815048, 846.010735815048, 846.010735815048, 846.010735815048, 846.010735815048, 846.010735815048, 846.010735815048, 846.010735815048, 846.010735815048, 846.010735815048];
let first_z=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let B_C_x=[541.0441730642652, 541.0441730642652, 541.0441730642652, 541.0441730642652, 541.0441730642652, 541.0441730642652, 541.0441730642652, 541.0441730642652, 541.0441730642652, 541.0441730642652, 541.0441730642652, 541.0441730642652, 541.0441730642652, 541.0441730642652, 541.0441730642652];
let B_C_y=[678.4479339461052, 678.4479339461052, 678.4479339461052, 678.4479339461052, 678.4479339461052, 678.4479339461052, 678.4479339461052, 678.4479339461052, 678.4479339461052, 678.4479339461052, 678.4479339461052, 678.4479339461052, 678.4479339461052, 678.4479339461052, 678.4479339461052];
let B_C_z=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let D_E_x=[867.767478235117, 885.221935051507, 934.843080354961, 1008.747021813, 1094.895650899159, 1178.61089219904, 1244.434818627631, 1278.112992324788, 1268.462971942861, 1208.90263688671, 1098.4523471529, 942.08637448267, 750.3852999945956, 538.523218095682, 324.7019611660443];
let D_E_y=[0.0, 15.968217190773, 62.328385730651, 134.618760825937, 225.955556991976, 327.794339963282, 430.869504633617, 526.2033275527132, 606.0683541488788, 664.792745919495, 699.316970671864, 709.439655748143, 697.727073662407, 669.100280377813, 630.151729133736];
let D_E_z=[0.0, 98.4987830317364, 179.8856307239226, 229.2238926317571, 235.666939802789, 193.882575019399, 104.815257909414, -24.307462136659, -180.72853865369876, -347.589305586617, -505.865918977369, -636.588079592077, -723.079749795861, -752.958155129698, -719.65494590756];
let F_G_x=[541.044173064266, 561.1036488830921, 620.5373623234877, 716.2690134556042, 840.924035392735, 981.132547951033, 1117.610842684438, 1227.835711697528, 1290.92478933296, 1293.187196575465, 1232.2685072009676, 1118.1745749415195, 970.6046543521603, 813.4751864350212, 668.6379748578053];
let F_G_y=[-678.447933946096, -651.760812863983, -572.184001610394, -441.779940276245, -265.672937430587, -53.539677627589, 179.8846271477604, 415.9295350047751, 634.7199893941785, 818.7948813968708, 956.4729626433787, 1043.8648973735014, 1084.9126401884773, 1089.5532329837877, 1070.747894043636];
let F_G_z=[0.0, 225.483019104116, 436.0997270203376, 615.5668351226311, 746.391483178528, 812.450588901928, 803.3580179584117, 718.8961458654272, 571.411254054282, 384.680571223829, 189.118791876499, 14.71248131701045, -115.930270460065, -192.01212655944, -215.053365281796];
let H_I_x=[-193.096429713796, -175.54463401143389, -120.5272678443833, -25.0427173112858, 105.984684260549, 254.591813992416, 393.5765863631147, 497.5648656762912, 553.8668799491556, 565.7712361912879, 546.6643405838925, 509.923710094233, 461.8701317338626, 401.90745086871357, 328.3814554623442];
let H_I_y=[-846.010735815046, -797.8252956615722, -657.115659986257, -437.163288093965, -163.723507292809, 125.3035912121733, 386.609313479718, 583.084221684581, 694.8042026372224, 723.6284573979234, 689.2482719100161, 619.3442102375968, 539.2456093542573, 465.6818787824797, 406.018254980599];
let H_I_z=[0.0, 280.7477582342982, 539.2963574749688, 747.761092061147, 874.8834326130954, 897.2642924355861, 812.2471659312367, 642.7153123841222, 429.371672418607, 214.830373875955, 29.188780317483, -115.10581024351455, -218.284528673374, -283.86118570191, -312.005545131009];
let J_K_x=[-781.831482468032, -743.4239538122218, -624.9987139884113, -426.0509475302338, -164.0731427895489, 124.7266903806044, 402.5468106653597, 646.5818077718621, 847.7010467134377, 995.4962853741209, 1069.6575418979853, 1049.5839149044682, 933.287335274469, 746.7929971192617, 535.0895716977852];
let J_K_y=[-376.510198141266, -306.9638046997325, -116.4413800960429, 143.55422333298262, 400.5973840762149, 587.2155765467463, 671.243537841506, 670.7570884725696, 640.3684395535147, 636.8732054664873, 688.0937557271011, 784.4661501748518, 893.9072149491172, 984.8042043014603, 1041.1677492251165];
let J_K_z=[0.0, 220.6828595761586, 397.1007165148636, 485.0839357717906, 455.7767411478363, 316.9091557381765, 115.1513255940231, -90.1879122063814, -261.8142268566392, -397.41926931269, -512.5828465596688, -613.6450004226332, -686.2809847927953, -706.478847841971, -659.7074172295485];
let L_M_x=[-781.831482468032, -694.4131846459109, -441.3074670135263, -59.8765276554924, 378.3084791244726, 792.7565963426601, 1128.0411837944732, 1356.704126030094, 1458.6649738312196, 1419.258192943481, 1254.2337870442839, 1022.7992138716133, 801.119073641629, 638.9492693165937, 540.8260912543312];
let L_M_y=[376.510198141264, 433.4783274694105, 565.8629440496611, 682.1902757292326, 701.0223290097299, 616.4870961257251, 510.8498239650274, 491.7481846433292, 603.6444169258384, 793.3429765754807, 956.4244739230861, 1014.6825261122503, 957.4034450880259, 826.8565182539343, 678.0218864363006];
let L_M_z=[0.0, 92.68633371686549, 136.7969473251504, 107.1590563236266, 28.4516355325393, -29.3839861219645, -7.20670775233219, 85.0885057137726, 176.8361386286258, 205.0612479156927, 166.3648337645393, 102.82043254890785, 52.3254710364267, 21.849358438253, -0.0621399022155];
let last_x=[-193.096429713796, -67.18737646221899, 266.1182049284447, 683.6824953845936, 1035.0974541892176, 1223.6030907583352, 1237.1623797822938, 1111.671797741904, 902.645931020907, 690.0927901981379, 554.4163894955944, 514.6574292851425, 509.3877327168919, 456.48070192207206, 324.8344473273691];
let last_y=[846.010735815039, 839.2083640930475, 779.0435600572152, 605.3588818893716, 350.9116526483006, 167.7634157005331, 200.1077176143433, 428.2790481018058, 673.8396756085123, 769.5329258078623, 700.5179390890498, 578.6575529543373, 516.4172200694006, 545.609741993393, 630.5588177370676];
let last_z=[0.0, -2.23805802316231, -8.60821370293033, 16.2930374068177, 142.8652437644143, 394.9485180453483, 669.9724599310945, 794.2926681506736, 679.7826237622448, 391.5836705333551, 57.7040186796473, -241.72835408756615, -483.8309345800543, -652.4244657411626, -719.877799693572];


let sec=floor(millis()/1000);
let steparray=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1];
let t=steparray[sec%28];

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
vertex(last_x[t],last_y[t],last_z[t]);
endShape(CLOSE);
beginShape();
vertex(N_x[t],N_y[t],N_z[t]);
vertex(O_x[t],O_y[t],O_z[t]);
vertex(last_x[t],last_y[t],last_z[t]);
endShape(CLOSE);
}