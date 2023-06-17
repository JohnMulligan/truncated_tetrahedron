

function setup() {
  createCanvas(1000, 800, WEBGL);
  fill(204);
  
  
  
}

function draw() {

  background(0);

let A_x=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let A_y=[1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0];
let A_z=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let B_x=[258.81904510252076, 258.81904510252076, 258.81904510252076, 258.81904510252076, 258.81904510252076, 258.81904510252076, 258.81904510252076, 258.81904510252076, 258.81904510252076, 258.81904510252076];
let B_y=[965.9258262890684, 965.9258262890684, 965.9258262890684, 965.9258262890684, 965.9258262890684, 965.9258262890684, 965.9258262890684, 965.9258262890684, 965.9258262890684, 965.9258262890684];
let B_z=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let C_x=[500.0, 499.689171467531, 498.761383737247, 497.230659406883, 495.120133867032, 492.461705632506, 489.295554227695, 485.669532912641, 481.638445428132, 477.263217691151];
let C_y=[866.025403784439, 865.620324154322, 864.411207643605, 862.41632885745, 859.665838423887, 856.201307296774, 852.075098451769, 847.349575471526, 842.096159981573, 836.39425218278];
let C_z=[0.0, 8.29071096250897, 16.456115994609, 24.3728030416114, 31.921119176202, 38.986979034587, 45.463589104401, 51.2530618034613, 56.2678949541608, 60.4322942926978];
let D_x=[707.106781186547, 705.724360768303, 701.60522464055, 694.832887582378, 685.543711456834, 673.922796215773, 660.198489928509, 644.63576296472, 627.52873767054, 609.1926951668];
let D_y=[707.106781186548, 706.115335081792, 703.16540538735, 698.329281472021, 691.724372319545, 683.508762975983, 673.875316487788, 663.044621798462, 651.25714336116, 638.764963130377];
let D_z=[0.0, 24.29091885585237, 48.1186314378848, 71.0327186252756, 92.607793846085, 112.4546941358868, 130.2301609278288, 145.644635455257, 158.4678939103338, 168.5323613764288];
let E_x=[866.025403784439, 863.452458787711, 855.759997630571, 843.028734858545, 825.398194131917, 803.073164183006, 776.3308046072, 745.526806290772, 711.0989851330227, 673.5668999764108];
let E_y=[500.0, 498.188154744199, 492.820238397395, 484.097277332847, 472.348068419409, 458.019357152153, 441.661327125649, 423.907949170097, 405.451990551889, 387.014928451599];
let E_z=[0.0, 30.33096801971976, 59.9323569394625, 88.0910501520164, 114.1277470213124, 137.4158186499904, 157.4017647405216, 173.626711909272, 185.7477035382366, 193.5569336250782];
let F_x=[965.925826289068, 961.816056315282, 949.5188229973764, 929.1364153033214, 900.8582606705774, 864.9851862132391, 821.9558286903411, 772.369267696701, 716.9982562000392, 656.7886994765478];
let F_y=[258.819045102521, 256.415361112382, 249.349818404137, 238.053113655405, 223.223381185545, 205.795895266612, 186.899607469753, 167.80044643609, 149.832393765945, 134.318841715717];
let F_z=[0.0, 25.98742536834544, 51.00013011707792, 74.0880393846333, 94.3536227556717, 110.9852638986457, 123.2964748686201, 130.7690786231811, 133.0963240526804, 130.2203157944656];
let G_x=[1000.0, 993.5840122724208, 974.3978431654318, 942.6417463124351, 898.6960028804741, 843.1804600046864, 777.018852337749, 701.4922083138505, 618.2656437760057, 529.3756203373168];
let G_y=[0.0, -2.687944832952, -10.485989274756, -22.608673487183, -37.787742723342, -54.336913234012, -70.247824926934, -83.31882241699, -91.314385346955, -92.147471849176];
let G_z=[0.0, 28.13713334099473, 54.83872689178104, 78.71255880073421, 98.46035612087027, 112.9405844380664, 121.2437717870906, 122.77516307457763, 117.334040294809, 105.175086579078];
let H_x=[965.925826289068, 956.5292580948758, 928.50768623428, 882.3890159010564, 819.1251708534209, 740.1792473621014, 647.609122547087, 544.1171126506035, 433.0372384860598, 318.2398790697918];
let H_y=[-258.819045102521, -260.95752147855, -266.954636072483, -275.582081288716, -284.883036826727, -292.312064748873, -294.935852351253, -289.691845280176, -273.692346381505, -244.549751394053];
let H_z=[0.0, 36.629388283498, 71.15663510455855, 101.56886745108662, 126.04197580401348, 143.0557779041582, 151.5218098599068, 150.91058774089933, 141.3562097323648, 123.7113043918207];
let I_x=[866.025403784439, 853.7130920660738, 817.092400311669, 757.1507736846564, 675.6507218994109, 575.2638387591654, 459.682961170854, 333.6530330634385, 202.86681800948875, 73.6917684526888];
let I_y=[-500.0, -500.89872567936, -502.9795056405, -504.446981575907, -502.481209928698, -493.503571022696, -473.555097412764, -438.775296221994, -385.946791832542, -313.0440787891489];
let I_z=[0.0, 34.30517838083538, 65.9372069708536, 92.37171979865408, 111.39735283528947, 121.3018534199551, 121.0706918851033, 110.57024465022855, 90.672243471023, 63.2704561998802];
let J_x=[707.106781186548, 692.3433638685218, 648.613126916894, 577.6442199592504, 482.45582917067884, 367.4956982721704, 238.705562061091, 103.4213210477825, -29.96585312099024, -152.6152098110072];
let J_y=[-707.10678118654, -705.690660495517, -700.636308623457, -689.618374322454, -669.071584767772, -634.65705757474, -581.901512799002, -506.965802729984, -407.4578196657774, -283.16306825986];
let J_z=[0.0, 21.32744061321058, 39.5768182637274, 51.90815718000358, 55.97418208182457, 50.19320096021649, 34.0167386290956, 8.14094695475254, -25.407773576152, -63.3811297387378];
let K_x=[500.0, 482.8543633429018, 432.334600673626, 351.2473943808474, 244.41885193994986, 118.7991472014744, -16.598891148467, -151.0704825705315, -272.99492041096124, -371.0158300611342];
let K_y=[-866.025403784439, -861.333430898113, -846.265900801494, -818.002215849767, -772.354696536901, -704.5271268272484, -610.1262557920511, -486.3234543109098, -332.9887037959422, -153.554083438634];
let K_z=[0.0, 15.16026118979586, 26.7718040130481, 31.64947942018248, 27.35000146451737, 12.55616693712949, -12.5809810169332, -46.22965875003056, -84.9020645257413, -123.8048630712296];
let L_x=[258.819045102521, 239.9321586849958, 184.681526710749, 97.3340927099554, -14.92905362308614, -142.0806510125146, -271.635016182886, -389.5304151074185, -481.57862790258724, -535.3794688323972];
let L_y=[-965.925826289069, -956.9158179946377, -928.8088249501524, -878.6121227651317, -802.1204885423, -695.0379669058133, -554.4046936399845, -380.1164141055538, -176.2185984663282, 48.406839518314];
let L_z=[0.0, 16.23598556720944, 28.49460742384823, 33.32931279374083, 28.354455655263, 12.74096324445533, -12.408178743364495, -43.93344290936357, -76.88218510943815, -105.2380305436872];
let M_x=[0.0, -19.3601397137652, -75.446488223847, -162.2778331225246, -269.96667601231616, -385.0879179767606, -491.597641784839, -572.5002599639535, -612.2626651116602, -599.6700822072534];
let M_y=[-1000.0, -986.0081403672403, -942.9599683232168, -867.9858963653113, -757.4348069562482, -608.4503241308863, -420.8788891255495, -199.1207363934508, 46.6090912521138, 300.180286927964];
let M_z=[0.0, 7.90002779873936, 11.71639508506353, 8.08889481160913, -4.9223898848657, -27.23897851521637, -56.40420457443359, -87.64783349844816, -114.53654123645435, -130.2419429017052];
let N_x=[-258.819045102521, -276.8450410669142, -328.294704650122, -405.3722216699146, -495.4822595106131, -582.1350763766026, -646.680428804228, -671.0116415128651, -641.0418175108808, -550.3081937421141];
let N_y=[-965.925826289069, -946.5709027237008, -887.644659471966, -787.0328706900473, -642.7150568566911, -454.77228238122336, -227.6424406669055, 28.0077597040162, 294.5633793831878, 548.586619979288];
let N_z=[0.0, -9.26322609077264, -22.28865569573367, -41.91183830958467, -69.1909510822171, -102.76264548396077, -138.6073163114858, -170.45182728914926, -190.94844349300206, -193.5352686874348];
let O_x=[-500.0, -515.5511046042702, -558.888195675549, -620.2876496041886, -684.4191598311851, -732.0293947633465, -742.8006664271466, -699.3837380016365, -592.0550427792415, -422.8204609032561];
let O_y=[-866.025403784439, -841.2151457420408, -766.325213155651, -640.5855911916393, -464.6209483449452, -242.87747350229333, 13.9106550007485, 287.1773296932082, 550.9533085952178, 775.008630601215];
let O_z=[0.0, -17.50501735078342, -38.30680989879157, -64.55914687370468, -96.2775461529865, -130.70241476360366, -162.30012776466648, -183.66188233493668, -187.3640994943422, -168.4693854316068];
let P_x=[-707.10678118655, -718.7440219895922, -749.715143735466, -788.6328360585426, -818.1000111319971, -817.4455959577274, -766.9334492000429, -653.1245876588089, -474.30067048744246, -244.1348685713881];
let P_y=[-707.10678118655, -677.3267552108279, -588.214916364756, -441.1762109841383, -240.7579825874432, 2.74260518853966, 271.0484122842715, 537.3554118397642, 768.6828801356578, 931.621415621361];
let P_z=[0.0, -16.24756142842193, -35.12161083714138, -57.91499871299228, -83.5045285141516, -107.82891613981027, -124.27211181983189, -125.18654013930657, -104.44191365214641, -60.3387140977608];
let Q_x=[-866.025403784439, -872.0628196397622, -885.722003122189, -894.3539414887496, -879.3730576811237, -820.3013743207528, -700.5379339057301, -514.0168440863249, -270.8800827633074, 0.4352178630639];
let Q_y=[-500.0, -466.1236237574868, -365.649982101395, -202.8578685664513, 12.7144325337358, 263.71385297547664, 523.4414507201645, 757.0252941476742, 926.5481251906677, 1000.0296818170789];
let Q_z=[0.0, -22.15780450966914, -45.86086863105938, -71.17256092334438, -95.5749867117361, -113.67697396520263, -118.12905722467646, -101.89435460707188, -61.46545130874051, 0.1106809314783];
let R_x=[-965.925826289069, -964.7591990171783, -956.5800898016041, -928.4039348733212, -862.1811496856085, -740.2666496183436, -552.611136475857, -304.0844936499729, -19.15939525404544, 259.2316549604819];
let R_y=[-258.819045102521, -222.4119874321488, -115.532520255063, 53.9754624260427, 270.7392699368068, 509.87235669376764, 736.8889033104344, 911.4081327605322, 995.5509415062819, 965.7842212778717];
let R_z=[0.0, -34.82141346616834, -69.70901852876038, -103.19732421164528, -131.2956950536837, -147.57065052662745, -144.70338707006294, -117.47301963230287, -66.32901401934733, 0.11066613338300685];
let S_x=[-1000.0, -991.0696005241446, -959.6317893251673, -893.2029754930002, -775.8251549952424, -595.0565005361527, -350.4136806386611, -60.6575125005169, 233.89681887911655, 477.5886973540139];
let S_y=[0.0, 37.3036503657372, 145.490708717024, 312.6436428916227, 516.9986310139197, 726.0337037407377, 898.5731542505215, 991.8392204337822, 973.5625101355416, 836.0978408853847];
let S_z=[0.0, -36.79566715923621, -72.13975686634022, -103.08644049154434, -124.41698261669268, -129.22311477308685, -111.19608528717416, -68.25419796800487, -6.10104048287832, 60.52583144566831];
let T_x=[-965.925826289069, -949.1495533301623, -894.6453483806723, -791.7633679411422, -628.8417993779454, -401.45479259471966, -121.3446116977601, 177.7239550378401, 441.80492753029455, 609.3849261020899];
let T_y=[258.819045102521, 294.8161209607472, 397.59698065392, 551.0112719240177, 727.1485354677158, 887.2132563174597, 986.5849559782247, 985.5844481034453, 864.6218631090876, 638.3629243041247];
let T_z=[0.0, -27.94216202448376, -52.96848759935822, -70.84939858224674, -75.61884483038968, -60.75503509218464, -22.147605047159853, 37.96962788670913, 108.15525564303668, 168.5952733533773];
let U_x=[-866.025403784439, -841.3091295529734, -763.8809813204293, -626.2044308700292, -422.99496972450845, -160.41914290621168, 135.3019271307169, 414.9443727162861, 614.1273072350785, 673.5919405304269];
let U_y=[500.0, 532.5398093158582, 623.441945316974, 752.4009177554777, 885.9537807849258, 980.7990567163324, 992.5077916305027, 890.2577392127237, 674.1077519488176, 386.5660935810367];
let U_z=[0.0, -25.44447984806966, -46.40497744506622, -57.40334601560593, -52.03231894731558, -24.81256766429754, 25.242494626283346, 90.76772851914544, 154.60650238140678, 193.5785228992926];
let V_x=[-707.10678118655, -675.1084006706184, -577.2692448558843, -410.6937879861572, -178.63366370731245, 100.19075720903332, 384.7486924078739, 613.4462393457391, 719.2102397505315, 656.6479219819396];
let V_y=[707.10678118655, 733.8092757651582, 805.874399515211, 899.5787615961357, 977.7156672442239, 995.9741510368207, 915.5390791882805, 720.9515255917466, 437.0155150797726, 133.8919265553777];
let V_z=[0.0, -29.47771875296068, -52.94767495851702, -63.89892205324011, -55.98905205235056, -25.550060815592488, 24.55255287439671, 81.78093844643212, 124.72011865478828, 130.1986130288685];
let W_x=[-500.0, -462.1987432825514, -348.9818776161893, -163.6736553797232, 80.08577069522757, 350.2527603358643, 593.1940559461449, 741.8020995455302, 737.7511507754706, 562.1317895034975];
let W_y=[866.025403784439, 884.5146763426072, 931.03998924415, 979.9501326516811, 993.3630694018906, 930.9845520820518, 766.1085702546566, 504.4709127268287, 196.8963782702526, -66.2896877811513];
let W_z=[0.0, -39.75913157123888, -72.09971214606492, -89.78027100600072, -87.09790111513097, -62.88227266765019, -24.12393879356569, 12.43207524117231, 23.98590312660528, -8.157338793935493];
let X_x=[-258.819045102521, -217.5060281509454, -96.35556464674129, 93.7173419459318, 327.58761207256055, 560.8638796046343, 732.3923410862309, 779.6902397833636, 666.3442796968586, 410.0072598361456];
let X_y=[965.925826289069, 974.090922739116, 989.4333422447702, 986.6372908131134, 931.3491626086278, 793.3419709547868, 564.4650521700626, 275.0898090557767, -2.1424246176004, -171.6963481008763];
let X_z=[0.0, -55.56794762082848, -102.40663780126042, -132.83260930819583, -142.28359945198625, -132.4942236734598, -114.19100519625759, -106.29932553315969, -129.09238119090872, -192.2657602623785];
let Y_x=[0.0, 41.8157466984906, 161.4246516426227, 339.4530973966338, 539.4050546809625, 707.6809907553933, 783.4812920942221, 721.1120875671359, 518.1062802053386, 232.4061071016466];
let Y_y=[1000.0, 996.2583398404491, 976.6199285561775, 919.067985846382, 797.8043344304187, 598.9555888391687, 337.9325081384595, 69.1245703045927, -123.5396634241904, -160.0640381552349];
let Y_z=[0.0, -75.79590178987068, -141.56687198505173, -189.3717545197607, -216.09076235337776, -226.33993611259558, -233.4439842002906, -255.6153257842127, -306.3959438701487, -383.2392331180805];
let first_x=[-124.84444888695987, -124.84444888695987, -124.84444888695987, -124.84444888695987, -124.84444888695987, -124.84444888695987, -124.84444888695987, -124.84444888695987, -124.84444888695987, -124.84444888695987];
let first_y=[948.2877360840265, 948.2877360840265, 948.2877360840265, 948.2877360840265, 948.2877360840265, 948.2877360840265, 948.2877360840265, 948.2877360840265, 948.2877360840265, 948.2877360840265];
let first_z=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let B_C_x=[366.02540378443825, 366.02540378443825, 366.02540378443825, 366.02540378443825, 366.02540378443825, 366.02540378443825, 366.02540378443825, 366.02540378443825, 366.02540378443825, 366.02540378443825];
let B_C_y=[883.6634939894805, 883.6634939894805, 883.6634939894805, 883.6634939894805, 883.6634939894805, 883.6634939894805, 883.6634939894805, 883.6634939894805, 883.6634939894805, 883.6634939894805];
let B_C_z=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let D_E_x=[758.819045102521, 756.786690215786, 750.734057122002, 740.792942987838, 727.178090363748, 710.18005733753, 690.155719756118, 667.516856604238, 642.71735367882, 616.239614820704];
let D_E_y=[582.262332299589, 581.150244026086, 577.848660440208, 572.460024617798, 565.149828616044, 556.139050204373, 545.6941583709, 534.115239454078, 521.722895934533, 508.844631790682];
let D_E_z=[0.0, 30.34560184010487, 60.0503501768591, 88.4940514294093, 115.0968586663426, 139.337066457357, 160.766200980085, 179.0207433673403, 193.8300112758778, 205.0199357707248];
let F_G_x=[948.287736084027, 943.3406766407874, 928.5547456119745, 904.102657684688, 870.2938016891419, 827.6008797524001, 776.687021349283, 718.4256105193394, 653.9057664881955, 584.4184912855463];
let F_G_y=[124.84444888696, 122.609893786434, 116.088633682539, 105.818698717058, 92.666057296757, 77.77821888694, 62.519329624173, 48.388031530547, 36.921038464823, 29.587431774557];
let F_G_z=[0.0, 22.10774538519287, 43.1097078736831, 61.936284671485, 77.5937396005237, 89.2095246001619, 96.0829447378553, 97.7380072817671, 93.9726963677577, 84.8972599031012];
let H_I_x=[883.66349398948, 873.0635387404387, 841.5205995624128, 789.8288070553122, 719.3817133666271, 632.2513062509104, 531.251701968419, 419.9518641543205, 302.60611626648074, 183.9836230995358];
let H_I_y=[-366.025403784442, -367.217850486835, -370.323511214155, -373.964461630082, -375.968816787876, -373.559616461616, -363.618472078621, -343.013981748961, -308.972529097326, -259.45499351276];
let H_I_z=[0.0, 38.21394781254403, 74.05785234712764, 105.28499904204152, 129.90436297424586, 146.3252618675466, 153.507529092131, 151.09896360295303, 139.5325537113001, 120.0525959535123];
let J_K_x=[582.262332299589, 567.0136702905368, 521.986942073185, 449.3810801662844, 352.97301846916986, 238.2033471053064, 112.151386913353, -16.6999537698235, -138.97861691893925, -245.2246410558502];
let J_K_y=[-758.819045102521, -755.621210957013, -745.194555658785, -725.155983260377, -691.920035606977, -641.267856867243, -569.1056259974973, -472.3424238267316, -349.769816866943, -202.7834018593169];
let J_K_z=[0.0, 13.60068867823758, 24.0633856883766, 28.54279866297418, 24.79013673344237, 11.46233575348509, -11.5968634084777, -43.16593003769046, -80.621959429225, -120.1516954488568];
let L_M_x=[124.84444888696, 106.2933752913678, 52.29419638817, -32.1846598399346, -138.89985797984713, -256.5748793715056, -371.54387234371, -468.9572129141195, -534.5733604414482, -556.9526868657402];
let L_M_y=[-948.287736084019, -936.9004218955498, -901.7434410001231, -840.1072460864448, -748.3731066340874, -623.2709489087872, -463.4254779490001, -270.9127564016748, -52.4434803295982, 180.250730957267];
let L_M_z=[0.0, 15.640881147251386, 27.33081238066787, 31.728729436594826, 26.695159914522158, 11.812815897303594, -11.26913085489399, -38.81098339548138, -65.4116528385254, -84.9382962812678];
let N_O_x=[-366.025403784432, -382.0461730686052, -427.251529067335, -493.2315145805926, -566.6071822343921, -630.2896868530617, -665.670082360142, -655.7914828891938, -589.1551949915714, -463.3341399428604];
let N_O_y=[-883.663493989479, -862.1047242907593, -796.8337829974058, -686.5737231929284, -530.7984424220042, -331.8089443155823, -96.9379694734645, 159.8535783271902, 417.8205407586788, 651.372089353591];
let N_O_z=[0.0, -16.91052520219214, -37.16233286002007, -63.10143459148567, -95.1950168839065, -131.42351844380937, -167.17353631127258, -195.85500701649318, -210.33259243996105, -204.9788655183982];
let P_Q_x=[-758.819045102521, -767.4168762998733, -789.169238186443, -812.5108660674426, -820.1430059100821, -792.2879589641285, -711.4397262423865, -568.0575129856455, -365.82514076238147, -124.4434282964081];
let P_Q_y=[-582.26233229959, -551.2780226361788, -459.03416276322, -308.3787837711423, -106.2254324395142, 134.02807240142167, 390.7431939587535, 634.3351926003832, 830.7611057079068, 948.400056050721];
let P_Q_z=[0.0, -14.52566514250624, -31.12136244573136, -50.50030615643507, -70.9700249245137, -88.04220199125837, -95.0505340150947, -84.95210728164378, -53.06440867308321, 0.0991135224352];
let R_S_x=[-948.287736084029, -943.2225557858616, -923.5569473874023, -877.0892483481181, -787.5372548860287, -640.4960631717668, -430.8853905605221, -169.9049663334909, 111.58214100497057, 366.3835465870459];
let R_S_y=[-124.844448886962, -89.0605108995838, 15.332480535466, 178.7250122244407, 383.1381453893208, 600.8862528190816, 795.5623971382255, 927.1338976372272, 961.6301546426147, 883.4509555589619];
let R_S_z=[0.0, -38.54315527852984, -76.35117859830439, -111.23768671103008, -138.7170442143357, -152.32411761924905, -145.45075618915985, -114.49822125761487, -62.28852241735645, 0.099085456732184];
let T_U_x=[-883.663493989479, -863.7180224856367, -800.3052574685754, -684.7013767588982, -508.77222780533145, -273.31581252018066, 3.5613870251629, 282.2034780191881, 505.89556033766155, 616.3450413549199];
let T_U_y=[366.02540378444, 399.3313246083162, 493.471052270735, 630.8072108061338, 781.7032996548298, 906.5754388511007, 962.4834215562743, 915.2712498514882, 755.0159955701066, 508.4317627797507];
let T_U_z=[0.0, -21.75181459724541, -39.99141953621612, -50.097703730591235, -46.16769300136498, -22.46923707002384, 23.436407267887844, 86.96328141831013, 154.40716635579068, 205.0609382698203];
let V_W_x=[-582.26233229959, -548.5057966309414, -446.3820152712093, -275.9691774741722, -45.32256846614144, 220.95053184257432, 476.6560036614509, 658.6772494481982, 705.1932726899063, 584.2094313759004];
let V_W_y=[758.819045102521, 781.0540579723732, 839.46797023053, 909.9410994809107, 955.7366427933875, 935.3561505271372, 816.5064494139897, 594.1692378122677, 305.3526744828246, 29.2161351484007];
let V_W_z=[0.0, -29.40115657765513, -52.40013916204993, -62.41705392115649, -53.67193595828156, -23.86794849165316, 22.127880664038376, 69.91915579290003, 97.72538402810868, 84.85615578134761];
let last_x=[-124.844448886962, -84.4275948940984, 32.74285353090171, 212.1922748105488, 424.08335320654356, 620.3904148136234, 740.6560570259869, 730.5349669092724, 569.7647524579455, 295.6937796937356];
let last_y=[948.287736084029, 950.9421697768859, 950.2153712691597, 922.6237996284495, 838.1225882360065, 674.3066072352548, 434.0742988930505, 159.1306628109147, -72.1394370839694, -170.6955514171433];
let last_z=[0.0, -59.38376934132298, -109.87951099651542, -144.06906276459063, -158.33577783844575, -155.8922673390619, -148.6911083254557, -155.26390669184468, -192.59913533008873, -264.31936059525947];


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
vertex(T_U_x[t],T_U_y[t],T_U_z[t]);
endShape(CLOSE);
beginShape();
vertex(T_x[t],T_y[t],T_z[t]);
vertex(T_U_x[t],T_U_y[t],T_U_z[t]);
vertex(U_x[t],U_y[t],U_z[t]);
endShape(CLOSE);
beginShape();
vertex(T_U_x[t],T_U_y[t],T_U_z[t]);
vertex(U_x[t],U_y[t],U_z[t]);
vertex(V_x[t],V_y[t],V_z[t]);
vertex(V_W_x[t],V_W_y[t],V_W_z[t]);
endShape(CLOSE);
beginShape();
vertex(V_x[t],V_y[t],V_z[t]);
vertex(V_W_x[t],V_W_y[t],V_W_z[t]);
vertex(W_x[t],W_y[t],W_z[t]);
endShape(CLOSE);
beginShape();
vertex(V_W_x[t],V_W_y[t],V_W_z[t]);
vertex(W_x[t],W_y[t],W_z[t]);
vertex(X_x[t],X_y[t],X_z[t]);
vertex(last_x[t],last_y[t],last_z[t]);
endShape(CLOSE);
beginShape();
vertex(X_x[t],X_y[t],X_z[t]);
vertex(Y_x[t],Y_y[t],Y_z[t]);
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
