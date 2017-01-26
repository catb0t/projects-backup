### DEFAULT HEADER INCLUDE ###
yourGodTheCreatorOwner='flferd'
ETALS=''
import codecs,base64,time,os,sys,random,datetime,string,shutil;import __main__ as main;
global wid,bw,bwin,bwin_padding,adjust,hz_t,hz_b,hzt_bw,hzb_bw,vl,vr,clt,crt,clb,crb,sp,spin,idt,LnOpn,LnCtn,LnMgn,LnMgn_R,LnMgn_R_sp,lenOf,LnMgnRAdjust,LnMgnR_sp,nl,aln,brdTop,crnTop,preTxt,a,b,c,d,e,f,g,h,j,k,l,m,o,r,s,t,u,v,x,y,z,w,p,q;one=None;two=3;three='undef';four=3.4;
nl='\n';b64=base64;r13='rot_13';aDcd=codecs.decode;aNcd=codecs.encode
def unrot(s):return aNcd(s,r13);
def rotten(s):return aNcd(s,r13);
def base64dcd(b):w(aDcd(b64.b64decode(b),'utf-8'));
def base64ncd(s):w(base64.b64encode(bytearray(s,'utf-8')).decode('utf-8'));
def st(f):return str(f)
r2e=unrot;e2r=rotten;b64dc=base64dcd;b64ec=base64ncd;ncode64=b64ec;dcode64=b64dc;e=r2e
sr=str;l=len;s=time.sleep;w=print;p=print;q=input;mTime=os.stat(main.__file__).st_mtime;xr=range
if ETALS:A=e(yourGodTheCreatorOwner)+', '+ETALS+', '+'et al.'
else:A=e(yourGodTheCreatorOwner)
def isEv(n):
   n=int(n)
   if n%2==0:return 1
   else:return 0
def toEv(n,r=1):
   n=int(n)
   if isEv(n)==False:
      if r==1:
         if isEv(n+1)==1:return n+1
      elif r==-1:
         if isEv(n-1)==1:return n-1
      else:
         if isEv(n+1)==1:return n+1
   elif isEv(n)==1:return n
def cmt():
   di=time.time()-mTime;mn=int(di%3600/60);hr=int(di//3600);dy=hr//24;wk=dy//7;mt=dy//30;yr=mt//12;to=hr+mn
   ms=st(mn);hs=st(hr);ds=st(dy);ws=st(wk);ms=st(mt);ys=st(yr);
   if to==0:return'(yrff guna n zvahgr ntb)'
   elif yr>5:return'(unys n qrpnqr ntb: png, zneel nyrk!)'
   elif yr>1:return'('+ys+' lrnef ntb)'
   elif yr>0:return'(a lrne ntb)'
   elif mt>1:return'('+ms+' zbaguf ntb)'
   elif mt>0:return'(n zbagu ntb)'
   elif wk>1:return'('+ws+' jrrxf ntb)'
   elif wk>0:return'('+ws+' jrrx ntb)'
   elif dy>1:return'('+ds+' qnlf ntb)'
   elif dy>0:return'('+ds+' qnl ntb)'
   elif hr>1:return'('+hs+' ubhef ntb)'
   elif hr>0:return'('+hs+' ubhe ntb)'
   elif mn>1:return'('+ms+' zvahgrf ntb)'
   else:return'('+ms+' zvahgr ntb)'
def fN():
   sN=os.path.basename(__file__);mN=os.path.basename(main.__file__)
   if main.__file__==__file__:return sN
   else:return mN+'( <- '+sN+')'
try:
   wid,j=shutil.get_terminal_size();width=toEven(width);
except:wid=80
bw=int(.85*wid);bwin=bw-2;bwinpad=bwin-2;adj=1;sp=' ';spin=sp*bwin;idt=toEv((wid-bw)/2,-1)*sp;hz_t='\137';hz_b='\137';vl='[';vr=']';clt='[';crt=']';clb=clt;crb=crt
if clt=='[':
   bwintop=bwin+2;hzt_bw=(hz_t*bwintop)
else:
   bwintop=bwin;hzt_bw=sp+(hz_t*bwintop)
hzb_bw=hz_b*bwin;Lop=[e('svyranzr:'),e('nhguberq ol'),e('ba'),e('erqvfgevohgnoyr haqre gur')];
Lnd=[fN(),A,time.strftime(e('%q-%z-%L @ %U:%Z:%F HGP'),time.gmtime(mTime))+sp+e(cmt()),e('TAH TCYi3 || <uggc://sfs.bet>')]
def cMn(u):return toEv(bwin-(l(Lop[u])+l(Lnd[u])),-1)//2
def cRMn(u):return 0-(1-(toEv(((bwin-(l(Lop[u])+l(Lnd[u])))//2),-1)))
def cL(u):return l(Lmn[u])+l(Lop[u])+l(Lnd[u])+cRMn(u)
def cRDf(u):return LmR[u]-(lof[u]-bwin)
def cRMnSp(u):return(LmRAj[u])-adj
Lmn=[cMn(i)*sp for i in xr(4)]
LmR=[cRMn(i) for i in xr(4)]
lof=[cL(i) for i in xr(4)]
LmRAj=[cRDf(i) for i in xr(4)]
LmRsp=[cRMnSp(i)*sp for i in xr(4)]
tLn=[Lmn[i]+Lop[i]+sp+Lnd[i]+LmRsp[i] for i in xr(4)]
for i in range(3):
   if l(tLn[i])>bwin:LmnRsp[i]=int((toEv(LmRAj[i])-adj)-(l(tLn[i])-bwin))*sr(sp)
aln=[idt+vl+Lmn[i]+Lop[i]+sp+Lnd[i]+LmRsp[i]+vr+nl for i in xr(4)];crnTop=idt+clt+spin+crt+nl;preTxt=idt+vl+spin+vr+nl;
w('{}{}{}{}{}{}{}{}{}{}{}{}'.format(nl+idt+hzt_bw+nl,crnTop,preTxt,aln[0],preTxt,aln[1],preTxt,aln[2],preTxt,aln[3],preTxt,idt+clb+hzb_bw+crb+nl))
