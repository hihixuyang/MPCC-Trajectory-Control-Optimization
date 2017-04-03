/* This function was automatically generated by CasADi */#ifdef __cplusplus
extern "C" {
#endif

#ifdef CODEGEN_PREFIX
  #define NAMESPACE_CONCAT(NS, ID) _NAMESPACE_CONCAT(NS, ID)
  #define _NAMESPACE_CONCAT(NS, ID) NS ## ID
  #define CASADI_PREFIX(ID) NAMESPACE_CONCAT(CODEGEN_PREFIX, ID)
#else /* CODEGEN_PREFIX */
  #define CASADI_PREFIX(ID) FORCESNLPsolver_model_11_ ## ID
#endif /* CODEGEN_PREFIX */

#include <math.h>

#include "FORCESNLPsolver/include/FORCESNLPsolver.h"

#define PRINTF printf
FORCESNLPsolver_FLOAT CASADI_PREFIX(sq)(FORCESNLPsolver_FLOAT x) { return x*x;}
#define sq(x) CASADI_PREFIX(sq)(x)

FORCESNLPsolver_FLOAT CASADI_PREFIX(sign)(FORCESNLPsolver_FLOAT x) { return x<0 ? -1 : x>0 ? 1 : x;}
#define sign(x) CASADI_PREFIX(sign)(x)

static const int CASADI_PREFIX(s0)[] = {20, 1, 0, 20, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19};
#define s0 CASADI_PREFIX(s0)
static const int CASADI_PREFIX(s1)[] = {18, 1, 0, 18, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17};
#define s1 CASADI_PREFIX(s1)
static const int CASADI_PREFIX(s2)[] = {1, 1, 0, 1, 0};
#define s2 CASADI_PREFIX(s2)
static const int CASADI_PREFIX(s3)[] = {1, 20, 0, 0, 0, 0, 0, 0, 1, 2, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
#define s3 CASADI_PREFIX(s3)
/* evaluate_stages */
int FORCESNLPsolver_model_11(const FORCESNLPsolver_FLOAT** arg, FORCESNLPsolver_FLOAT** res) {
     FORCESNLPsolver_FLOAT a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37,a38,a39,a40,a41,a42,a43,a44,a45,a46,a47,a48,a49,a50,a51,a52,a53,a54,a55,a56,a57,a58,a59,a60,a61,a62,a63,a64,a65,a66,a67,a68,a69,a70,a71,a72,a73,a74,a75,a76,a77,a78,a79,a80,a81,a82,a83,a84,a85,a86,a87,a88,a89,a90,a91,a92,a93,a94,a95,a96,a97,a98,a99,a100,a101,a102,a103,a104,a105,a106,a107,a108,a109,a110,a111,a112,a113,a114,a115,a116,a117,a118,a119,a120,a121,a122,a123,a124,a125,a126,a127,a128,a129,a130,a131,a132,a133,a134,a135;
         a0=arg[1] ? arg[1][0] : 0;
         a1=arg[0] ? arg[0][17] : 0;
         a2=(a0*a1);
         a3=arg[1] ? arg[1][1] : 0;
  a2=(a2+a3);
         a4=(a2*a1);
         a5=arg[1] ? arg[1][2] : 0;
  a4=(a4+a5);
         a6=arg[0] ? arg[0][5] : 0;
  a4=(a6-a4);
         a7=arg[1] ? arg[1][9] : 0;
         a8=(a7*a1);
         a9=arg[1] ? arg[1][10] : 0;
  a8=(a8+a9);
         a10=(a7*a1);
  a10=(a10+a9);
         a11=sq(a10);
         a12=arg[1] ? arg[1][11] : 0;
         a13=(a12*a1);
         a14=arg[1] ? arg[1][12] : 0;
  a13=(a13+a14);
         a15=sq(a13);
  a11=(a11+a15);
  a15=arg[1] ? arg[1][13] : 0;
         a16=(a15*a1);
         a17=arg[1] ? arg[1][14] : 0;
  a16=(a16+a17);
         a18=sq(a16);
  a11=(a11+a18);
  a11=sqrt(a11);
  a8=(a8/a11);
  a18=(a4*a8);
         a19=arg[1] ? arg[1][3] : 0;
         a20=(a19*a1);
         a21=arg[1] ? arg[1][4] : 0;
  a20=(a20+a21);
         a22=(a20*a1);
         a23=arg[1] ? arg[1][5] : 0;
  a22=(a22+a23);
         a24=arg[0] ? arg[0][6] : 0;
  a22=(a24-a22);
         a25=(a12*a1);
  a25=(a25+a14);
         a26=(a7*a1);
  a26=(a26+a9);
         a27=sq(a26);
         a28=(a12*a1);
  a28=(a28+a14);
         a29=sq(a28);
  a27=(a27+a29);
  a29=(a15*a1);
  a29=(a29+a17);
         a30=sq(a29);
  a27=(a27+a30);
  a27=sqrt(a27);
  a25=(a25/a27);
  a30=(a22*a25);
  a18=(a18+a30);
  a30=arg[1] ? arg[1][6] : 0;
         a31=(a30*a1);
         a32=arg[1] ? arg[1][7] : 0;
  a31=(a31+a32);
         a33=(a31*a1);
         a34=arg[1] ? arg[1][8] : 0;
  a33=(a33+a34);
         a35=arg[0] ? arg[0][7] : 0;
  a33=(a35-a33);
         a36=(a15*a1);
  a36=(a36+a17);
         a37=(a7*a1);
  a37=(a37+a9);
         a38=sq(a37);
         a39=(a12*a1);
  a39=(a39+a14);
         a40=sq(a39);
  a38=(a38+a40);
  a40=(a15*a1);
  a40=(a40+a17);
         a41=sq(a40);
  a38=(a38+a41);
  a38=sqrt(a38);
  a36=(a36/a38);
  a41=(a33*a36);
  a18=(a18+a41);
  a41=10000.;
  a18=(a41*a18);
         a42=(a0*a1);
  a42=(a42+a3);
         a43=(a42*a1);
  a43=(a43+a5);
  a43=(a6-a43);
         a44=(a18*a43);
         a45=(a7*a1);
  a45=(a45+a9);
         a46=(a7*a1);
  a46=(a46+a9);
         a47=sq(a46);
         a48=(a12*a1);
  a48=(a48+a14);
         a49=sq(a48);
  a47=(a47+a49);
  a49=(a15*a1);
  a49=(a49+a17);
         a50=sq(a49);
  a47=(a47+a50);
  a47=sqrt(a47);
  a45=(a45/a47);
  a50=(a44*a45);
         a51=(a19*a1);
  a51=(a51+a21);
         a52=(a51*a1);
  a52=(a52+a23);
  a52=(a24-a52);
         a53=(a18*a52);
         a54=(a12*a1);
  a54=(a54+a14);
         a55=(a7*a1);
  a55=(a55+a9);
         a56=sq(a55);
         a57=(a12*a1);
  a57=(a57+a14);
         a58=sq(a57);
  a56=(a56+a58);
  a58=(a15*a1);
  a58=(a58+a17);
         a59=sq(a58);
  a56=(a56+a59);
  a56=sqrt(a56);
  a54=(a54/a56);
  a59=(a53*a54);
  a50=(a50+a59);
  a59=(a30*a1);
  a59=(a59+a32);
         a60=(a59*a1);
  a60=(a60+a34);
  a60=(a35-a60);
         a61=(a18*a60);
         a62=(a15*a1);
  a62=(a62+a17);
         a63=(a7*a1);
  a63=(a63+a9);
         a64=sq(a63);
         a65=(a12*a1);
  a65=(a65+a14);
         a66=sq(a65);
  a64=(a64+a66);
  a66=(a15*a1);
  a66=(a66+a17);
         a67=sq(a66);
  a64=(a64+a67);
  a64=sqrt(a64);
  a62=(a62/a64);
  a67=(a61*a62);
  a50=(a50+a67);
  a67=(a0*a1);
  a67=(a67+a3);
         a68=(a67*a1);
  a68=(a68+a5);
  a68=(a6-a68);
         a69=sq(a68);
         a70=(a19*a1);
  a70=(a70+a21);
         a71=(a70*a1);
  a71=(a71+a23);
  a71=(a24-a71);
         a72=sq(a71);
  a69=(a69+a72);
  a72=(a30*a1);
  a72=(a72+a32);
         a73=(a72*a1);
  a73=(a73+a34);
  a73=(a35-a73);
         a74=sq(a73);
  a69=(a69+a74);
  a74=(a0*a1);
  a74=(a74+a3);
         a75=(a74*a1);
  a75=(a75+a5);
  a75=(a6-a75);
         a76=(a7*a1);
  a76=(a76+a9);
         a77=(a7*a1);
  a77=(a77+a9);
         a78=sq(a77);
         a79=(a12*a1);
  a79=(a79+a14);
         a80=sq(a79);
  a78=(a78+a80);
  a80=(a15*a1);
  a80=(a80+a17);
         a81=sq(a80);
  a78=(a78+a81);
  a78=sqrt(a78);
  a76=(a76/a78);
  a81=(a75*a76);
         a82=(a19*a1);
  a82=(a82+a21);
         a83=(a82*a1);
  a83=(a83+a23);
  a83=(a24-a83);
         a84=(a12*a1);
  a84=(a84+a14);
         a85=(a7*a1);
  a85=(a85+a9);
         a86=sq(a85);
         a87=(a12*a1);
  a87=(a87+a14);
         a88=sq(a87);
  a86=(a86+a88);
  a88=(a15*a1);
  a88=(a88+a17);
         a89=sq(a88);
  a86=(a86+a89);
  a86=sqrt(a86);
  a84=(a84/a86);
  a89=(a83*a84);
  a81=(a81+a89);
  a89=(a30*a1);
  a89=(a89+a32);
         a90=(a89*a1);
  a90=(a90+a34);
  a90=(a35-a90);
         a91=(a15*a1);
  a91=(a91+a17);
         a92=(a7*a1);
  a92=(a92+a9);
         a93=sq(a92);
         a94=(a12*a1);
  a94=(a94+a14);
         a95=sq(a94);
  a93=(a93+a95);
  a95=(a15*a1);
  a95=(a95+a17);
         a96=sq(a95);
  a93=(a93+a96);
  a93=sqrt(a93);
  a91=(a91/a93);
  a96=(a90*a91);
  a81=(a81+a96);
  a96=sq(a81);
  a69=(a69-a96);
  a69=sqrt(a69);
  a96=(a41*a69);
         a97=(a0*a1);
  a97=(a97+a3);
         a98=(a97*a1);
  a98=(a98+a5);
  a98=(a6-a98);
         a99=sq(a98);
         a100=(a19*a1);
  a100=(a100+a21);
         a101=(a100*a1);
  a101=(a101+a23);
  a101=(a24-a101);
         a102=sq(a101);
  a99=(a99+a102);
  a102=(a30*a1);
  a102=(a102+a32);
         a103=(a102*a1);
  a103=(a103+a34);
  a103=(a35-a103);
         a104=sq(a103);
  a99=(a99+a104);
  a104=(a0*a1);
  a104=(a104+a3);
  a3=(a104*a1);
  a3=(a3+a5);
  a6=(a6-a3);
  a3=(a7*a1);
  a3=(a3+a9);
  a5=(a7*a1);
  a5=(a5+a9);
         a105=sq(a5);
         a106=(a12*a1);
  a106=(a106+a14);
         a107=sq(a106);
  a105=(a105+a107);
  a107=(a15*a1);
  a107=(a107+a17);
         a108=sq(a107);
  a105=(a105+a108);
  a105=sqrt(a105);
  a3=(a3/a105);
  a108=(a6*a3);
         a109=(a19*a1);
  a109=(a109+a21);
  a21=(a109*a1);
  a21=(a21+a23);
  a24=(a24-a21);
  a21=(a12*a1);
  a21=(a21+a14);
  a23=(a7*a1);
  a23=(a23+a9);
         a110=sq(a23);
         a111=(a12*a1);
  a111=(a111+a14);
         a112=sq(a111);
  a110=(a110+a112);
  a112=(a15*a1);
  a112=(a112+a17);
         a113=sq(a112);
  a110=(a110+a113);
  a110=sqrt(a110);
  a21=(a21/a110);
  a113=(a24*a21);
  a108=(a108+a113);
  a113=(a30*a1);
  a113=(a113+a32);
  a32=(a113*a1);
  a32=(a32+a34);
  a35=(a35-a32);
  a32=(a15*a1);
  a32=(a32+a17);
  a34=(a7*a1);
  a34=(a34+a9);
  a9=sq(a34);
         a114=(a12*a1);
  a114=(a114+a14);
  a14=sq(a114);
  a9=(a9+a14);
  a14=(a15*a1);
  a14=(a14+a17);
  a17=sq(a14);
  a9=(a9+a17);
  a9=sqrt(a9);
  a32=(a32/a9);
  a17=(a35*a32);
  a108=(a108+a17);
  a17=sq(a108);
  a99=(a99-a17);
  a99=sqrt(a99);
  a17=(a96*a99);
  a50=(a50+a17);
  a17=arg[1] ? arg[1][15] : 0;
         a115=(a17*a1);
         a116=arg[1] ? arg[1][16] : 0;
  a115=(a115+a116);
         a117=(a115*a1);
         a118=arg[1] ? arg[1][17] : 0;
  a117=(a117+a118);
         a119=arg[0] ? arg[0][18] : 0;
  a117=(a119-a117);
         a120=(a17*a1);
  a120=(a120+a116);
  a120=(a120*a1);
  a120=(a120+a118);
         a121=0.;
  a121=(a121<a120);
  a120=101.;
  a120=(a120*a121);
  a121=1.;
  a120=(a120-a121);
  a117=(a117*a120);
  a121=(a17*a1);
  a121=(a121+a116);
  a116=(a121*a1);
  a116=(a116+a118);
  a119=(a119-a116);
  a116=(a117*a119);
  a50=(a50+a116);
  a116=2.;
  a118=arg[0] ? arg[0][13] : 0;
         a122=(a116*a118);
         a123=(a122*a118);
         a124=arg[0] ? arg[0][14] : 0;
         a125=(a116*a124);
         a126=(a125*a124);
  a123=(a123+a126);
  a126=arg[0] ? arg[0][15] : 0;
         a127=(a116*a126);
         a128=(a127*a126);
  a123=(a123+a128);
  a128=arg[0] ? arg[0][16] : 0;
         a129=(a116*a128);
         a130=(a129*a128);
  a123=(a123+a130);
  a50=(a50+a123);
  a123=arg[0] ? arg[0][19] : 0;
  a130=(a116*a123);
         a131=(a130*a123);
  a50=(a50+a131);
  if (res[0]!=0) res[0][0]=a50;
  a98=(a98+a98);
  a50=(a99+a99);
  a96=(a96/a50);
  a98=(a98*a96);
  a108=(a108+a108);
  a108=(a108*a96);
  a50=(a3*a108);
  a131=(a98-a50);
  a81=(a81+a81);
  a99=(a41*a99);
  a69=(a69+a69);
  a99=(a99/a69);
  a81=(a81*a99);
  a69=(a76*a81);
  a131=(a131-a69);
  a68=(a68+a68);
  a68=(a68*a99);
  a131=(a131+a68);
         a132=(a18*a45);
  a131=(a131+a132);
  a60=(a60*a62);
  a52=(a52*a54);
  a60=(a60+a52);
  a43=(a43*a45);
  a60=(a60+a43);
  a41=(a41*a60);
  a60=(a8*a41);
  a131=(a131+a60);
  if (res[1]!=0) res[1][0]=a131;
  a101=(a101+a101);
  a101=(a101*a96);
  a131=(a21*a108);
  a43=(a101-a131);
  a52=(a84*a81);
  a43=(a43-a52);
  a71=(a71+a71);
  a71=(a71*a99);
  a43=(a43+a71);
         a133=(a18*a54);
  a43=(a43+a133);
         a134=(a25*a41);
  a43=(a43+a134);
  if (res[1]!=0) res[1][1]=a43;
  a103=(a103+a103);
  a103=(a103*a96);
  a96=(a32*a108);
  a43=(a103-a96);
         a135=(a91*a81);
  a43=(a43-a135);
  a73=(a73+a73);
  a73=(a73*a99);
  a43=(a43+a73);
  a18=(a18*a62);
  a43=(a43+a18);
  a99=(a36*a41);
  a43=(a43+a99);
  if (res[1]!=0) res[1][2]=a43;
  a118=(a116*a118);
  a122=(a122+a118);
  if (res[1]!=0) res[1][3]=a122;
  a124=(a116*a124);
  a125=(a125+a124);
  if (res[1]!=0) res[1][4]=a125;
  a126=(a116*a126);
  a127=(a127+a126);
  if (res[1]!=0) res[1][5]=a127;
  a128=(a116*a128);
  a129=(a129+a128);
  if (res[1]!=0) res[1][6]=a129;
  a14=(a14+a14);
  a32=(a32/a9);
  a35=(a35*a108);
  a32=(a32*a35);
  a129=(a9+a9);
  a32=(a32/a129);
  a14=(a14*a32);
  a14=(a15*a14);
  a121=(a121*a117);
  a129=(a1*a117);
  a129=(a17*a129);
  a121=(a121+a129);
  a120=(a120*a119);
  a115=(a115*a120);
  a121=(a121+a115);
  a115=(a1*a120);
  a17=(a17*a115);
  a121=(a121+a17);
  a14=(a14-a121);
  a114=(a114+a114);
  a114=(a114*a32);
  a114=(a12*a114);
  a14=(a14+a114);
  a34=(a34+a34);
  a34=(a34*a32);
  a34=(a7*a34);
  a14=(a14+a34);
  a35=(a35/a9);
  a35=(a15*a35);
  a14=(a14-a35);
  a113=(a113*a96);
  a14=(a14+a113);
  a96=(a1*a96);
  a96=(a30*a96);
  a14=(a14+a96);
  a112=(a112+a112);
  a21=(a21/a110);
  a24=(a24*a108);
  a21=(a21*a24);
  a96=(a110+a110);
  a21=(a21/a96);
  a112=(a112*a21);
  a112=(a15*a112);
  a14=(a14+a112);
  a111=(a111+a111);
  a111=(a111*a21);
  a111=(a12*a111);
  a14=(a14+a111);
  a23=(a23+a23);
  a23=(a23*a21);
  a23=(a7*a23);
  a14=(a14+a23);
  a24=(a24/a110);
  a24=(a12*a24);
  a14=(a14-a24);
  a109=(a109*a131);
  a14=(a14+a109);
  a131=(a1*a131);
  a131=(a19*a131);
  a14=(a14+a131);
  a107=(a107+a107);
  a3=(a3/a105);
  a6=(a6*a108);
  a3=(a3*a6);
  a108=(a105+a105);
  a3=(a3/a108);
  a107=(a107*a3);
  a107=(a15*a107);
  a14=(a14+a107);
  a106=(a106+a106);
  a106=(a106*a3);
  a106=(a12*a106);
  a14=(a14+a106);
  a5=(a5+a5);
  a5=(a5*a3);
  a5=(a7*a5);
  a14=(a14+a5);
  a6=(a6/a105);
  a6=(a7*a6);
  a14=(a14-a6);
  a104=(a104*a50);
  a14=(a14+a104);
  a50=(a1*a50);
  a50=(a0*a50);
  a14=(a14+a50);
  a102=(a102*a103);
  a14=(a14-a102);
  a103=(a1*a103);
  a103=(a30*a103);
  a14=(a14-a103);
  a100=(a100*a101);
  a14=(a14-a100);
  a101=(a1*a101);
  a101=(a19*a101);
  a14=(a14-a101);
  a97=(a97*a98);
  a14=(a14-a97);
  a98=(a1*a98);
  a98=(a0*a98);
  a14=(a14-a98);
  a95=(a95+a95);
  a91=(a91/a93);
  a90=(a90*a81);
  a91=(a91*a90);
  a98=(a93+a93);
  a91=(a91/a98);
  a95=(a95*a91);
  a95=(a15*a95);
  a14=(a14+a95);
  a94=(a94+a94);
  a94=(a94*a91);
  a94=(a12*a94);
  a14=(a14+a94);
  a92=(a92+a92);
  a92=(a92*a91);
  a92=(a7*a92);
  a14=(a14+a92);
  a90=(a90/a93);
  a90=(a15*a90);
  a14=(a14-a90);
  a89=(a89*a135);
  a14=(a14+a89);
  a135=(a1*a135);
  a135=(a30*a135);
  a14=(a14+a135);
  a88=(a88+a88);
  a84=(a84/a86);
  a83=(a83*a81);
  a84=(a84*a83);
  a135=(a86+a86);
  a84=(a84/a135);
  a88=(a88*a84);
  a88=(a15*a88);
  a14=(a14+a88);
  a87=(a87+a87);
  a87=(a87*a84);
  a87=(a12*a87);
  a14=(a14+a87);
  a85=(a85+a85);
  a85=(a85*a84);
  a85=(a7*a85);
  a14=(a14+a85);
  a83=(a83/a86);
  a83=(a12*a83);
  a14=(a14-a83);
  a82=(a82*a52);
  a14=(a14+a82);
  a52=(a1*a52);
  a52=(a19*a52);
  a14=(a14+a52);
  a80=(a80+a80);
  a76=(a76/a78);
  a75=(a75*a81);
  a76=(a76*a75);
  a81=(a78+a78);
  a76=(a76/a81);
  a80=(a80*a76);
  a80=(a15*a80);
  a14=(a14+a80);
  a79=(a79+a79);
  a79=(a79*a76);
  a79=(a12*a79);
  a14=(a14+a79);
  a77=(a77+a77);
  a77=(a77*a76);
  a77=(a7*a77);
  a14=(a14+a77);
  a75=(a75/a78);
  a75=(a7*a75);
  a14=(a14-a75);
  a74=(a74*a69);
  a14=(a14+a74);
  a69=(a1*a69);
  a69=(a0*a69);
  a14=(a14+a69);
  a72=(a72*a73);
  a14=(a14-a72);
  a73=(a1*a73);
  a73=(a30*a73);
  a14=(a14-a73);
  a70=(a70*a71);
  a14=(a14-a70);
  a71=(a1*a71);
  a71=(a19*a71);
  a14=(a14-a71);
  a67=(a67*a68);
  a14=(a14-a67);
  a68=(a1*a68);
  a68=(a0*a68);
  a14=(a14-a68);
  a66=(a66+a66);
  a62=(a62/a64);
  a62=(a62*a61);
  a68=(a64+a64);
  a62=(a62/a68);
  a66=(a66*a62);
  a66=(a15*a66);
  a14=(a14-a66);
  a65=(a65+a65);
  a65=(a65*a62);
  a65=(a12*a65);
  a14=(a14-a65);
  a63=(a63+a63);
  a63=(a63*a62);
  a63=(a7*a63);
  a14=(a14-a63);
  a61=(a61/a64);
  a61=(a15*a61);
  a14=(a14+a61);
  a59=(a59*a18);
  a14=(a14-a59);
  a18=(a1*a18);
  a18=(a30*a18);
  a14=(a14-a18);
  a58=(a58+a58);
  a54=(a54/a56);
  a54=(a54*a53);
  a18=(a56+a56);
  a54=(a54/a18);
  a58=(a58*a54);
  a58=(a15*a58);
  a14=(a14-a58);
  a57=(a57+a57);
  a57=(a57*a54);
  a57=(a12*a57);
  a14=(a14-a57);
  a55=(a55+a55);
  a55=(a55*a54);
  a55=(a7*a55);
  a14=(a14-a55);
  a53=(a53/a56);
  a53=(a12*a53);
  a14=(a14+a53);
  a51=(a51*a133);
  a14=(a14-a51);
  a133=(a1*a133);
  a133=(a19*a133);
  a14=(a14-a133);
  a49=(a49+a49);
  a45=(a45/a47);
  a45=(a45*a44);
  a133=(a47+a47);
  a45=(a45/a133);
  a49=(a49*a45);
  a49=(a15*a49);
  a14=(a14-a49);
  a48=(a48+a48);
  a48=(a48*a45);
  a48=(a12*a48);
  a14=(a14-a48);
  a46=(a46+a46);
  a46=(a46*a45);
  a46=(a7*a46);
  a14=(a14-a46);
  a44=(a44/a47);
  a44=(a7*a44);
  a14=(a14+a44);
  a42=(a42*a132);
  a14=(a14-a42);
  a132=(a1*a132);
  a132=(a0*a132);
  a14=(a14-a132);
  a40=(a40+a40);
  a36=(a36/a38);
  a33=(a33*a41);
  a36=(a36*a33);
  a132=(a38+a38);
  a36=(a36/a132);
  a40=(a40*a36);
  a40=(a15*a40);
  a14=(a14-a40);
  a39=(a39+a39);
  a39=(a39*a36);
  a39=(a12*a39);
  a14=(a14-a39);
  a37=(a37+a37);
  a37=(a37*a36);
  a37=(a7*a37);
  a14=(a14-a37);
  a33=(a33/a38);
  a33=(a15*a33);
  a14=(a14+a33);
  a31=(a31*a99);
  a14=(a14-a31);
  a99=(a1*a99);
  a30=(a30*a99);
  a14=(a14-a30);
  a29=(a29+a29);
  a25=(a25/a27);
  a22=(a22*a41);
  a25=(a25*a22);
  a30=(a27+a27);
  a25=(a25/a30);
  a29=(a29*a25);
  a29=(a15*a29);
  a14=(a14-a29);
  a28=(a28+a28);
  a28=(a28*a25);
  a28=(a12*a28);
  a14=(a14-a28);
  a26=(a26+a26);
  a26=(a26*a25);
  a26=(a7*a26);
  a14=(a14-a26);
  a22=(a22/a27);
  a22=(a12*a22);
  a14=(a14+a22);
  a20=(a20*a134);
  a14=(a14-a20);
  a134=(a1*a134);
  a19=(a19*a134);
  a14=(a14-a19);
  a16=(a16+a16);
  a8=(a8/a11);
  a4=(a4*a41);
  a8=(a8*a4);
  a41=(a11+a11);
  a8=(a8/a41);
  a16=(a16*a8);
  a15=(a15*a16);
  a14=(a14-a15);
  a13=(a13+a13);
  a13=(a13*a8);
  a12=(a12*a13);
  a14=(a14-a12);
  a10=(a10+a10);
  a10=(a10*a8);
  a10=(a7*a10);
  a14=(a14-a10);
  a4=(a4/a11);
  a7=(a7*a4);
  a14=(a14+a7);
  a2=(a2*a60);
  a14=(a14-a2);
  a1=(a1*a60);
  a0=(a0*a1);
  a14=(a14-a0);
  if (res[1]!=0) res[1][7]=a14;
  a117=(a117+a120);
  if (res[1]!=0) res[1][8]=a117;
  a116=(a116*a123);
  a130=(a130+a116);
  if (res[1]!=0) res[1][9]=a130;
  return 0;
}

int FORCESNLPsolver_model_11_init(int *f_type, int *n_in, int *n_out, int *sz_arg, int* sz_res) {
  *f_type = 1;
  *n_in = 2;
  *n_out = 2;
  *sz_arg = 2;
  *sz_res = 2;
  return 0;
}

int FORCESNLPsolver_model_11_sparsity(int i, int *nrow, int *ncol, const int **colind, const int **row) {
  const int* s;
  switch (i) {
    case 0:
      s = s0; break;
    case 1:
      s = s1; break;
    case 2:
      s = s2; break;
    case 3:
      s = s3; break;
    default:
      return 1;
  }

  *nrow = s[0];
  *ncol = s[1];
  *colind = s + 2;
  *row = s + 2 + (*ncol + 1);
  return 0;
}

int FORCESNLPsolver_model_11_work(int *sz_iw, int *sz_w) {
  if (sz_iw) *sz_iw = 0;
  if (sz_w) *sz_w = 136;
  return 0;
}


#ifdef __cplusplus
} /* extern "C" */
#endif
