### DEFAULT HEADER INCLUDE ###
yourGodTheCreatorOwner='catb0t <thebinaryminer@gmail.com>'
ETALS=''
import time,os,sys,random,datetime,string,shutil;import __main__ as main
global a,b,c,d,e,f,g,h,j,k,l,m,o,q,r,s,t,u,v,x,y,z #in my code, <4 char vars (except i (and n,w,p) which are Reserved) are typically global and extremely volatile. stuff that gets set a few times and not read often, gets longer names
global one,two,three,four,five,six,seven,eight,nine,ten
one=None;two=3;three='undef';four=3.4;#etc#underhandedness to trick the Unsuspecting Richardi.
global w,p,fibnum
w=print;p=print; #for a programmer, I'm a very lazy person
global width,bw,bwinner,bwinner_padding,adjust,hz_t,hz_b,hzt_bw,hzb_bw,vl,vr,clt,crt,clb,crb,spa,spa_inner,idt,LnOpn,LnCtn,LnMgn,LnMgn_R,LnMgn_R_spa,lenOf,LnMgnRAdjust,LnMgnR_toSpace,nl,addLine,borderTop,cornerTop,preText,postText,borderBottom

def fib(n):
   fibnum = [0, 1]
   for i in range(2,n):
      fibnum.append(fibnum[i-1]+fibnum[i-2])
   w(fibnum)

def header(prnt=None):
   def printAttribLn():
      if ETALS: #were there other contributors?
         AUTHORS=yourGodTheCreatorOwner + ", " + ETALS + ', ' + 'et al.'
      else:AUTHORS=yourGodTheCreatorOwner
      #Who doesn't love a bit of ASCII art / styling??

      ##since we're doing centering stuff relative to elements left of them and the far-right margin (=80), ALL spacing values _M_U_S_T_!!! BE _E_V_E_N_!!
      def isEven(n):
         n=int(n)
         if n%2 is 0:return True
         else:return False

      def toEven(n,rounds=1):
         n=int(n)
         if isEven(n) is False:
            if rounds is 1:return n+1
            elif rounds is -1:return n-1
            elif rounds is -1:return n-1
            else:return n+1
         elif isEven(n) is True:return n
         else:raise Exception('MathError','format parameters must be even!')

      
      width = toEven(int(str.split(str.split(str(shutil.get_terminal_size()),'=',1)[1],',',1)[0]))


      bw=toEven(.75*width,-1)
      bwinner=bw-2
      bwinner_padding=bwinner-2

      #for unknown reasons, if width is greater than or 84 the right side goes out of alignment by a char. this fixes it
      if width >= 84:
         adjust=2
      else: adjust=1
      
      #boxy things to be messed with:
      #note: some character combinations require different setups here and below,,
      # BOX BORDER STYLES
      # OCTAL 57 = /, 134 = \, 137 = _, 174 = |,
      hz_t='\137';hz_b='\137' # horizontal line char! top+bottom ### IF UNDERSCORE USE CHARCODE=OCT(137)
      hzt_bw = hz_t*bw
      hzb_bw = hz_b*bwinner 
      vl='|';vr='|' #vertical line left/right :: if symmetrical, just set vr to vl
      clt='|';crt='|' #corner:left top and corner:right top :: / and \
      clb=clt;crb=crt #in the case of \ and /, the diagonal corners are the same.

      #texty things to be messed with
      spa=' ' #nonbreaking spaces. They matter.
      spa_inner=spa*bwinner #inner spaces width
      #indent should be calculated as
      idt=toEven((width-bw)/2,-1)*spa

      LnOpn=['Filename:','Author/s:','Modified:','Licensed under:']

      LnCtn=[os.path.basename(main.__file__)+' <- '+os.path.basename(__file__),AUTHORS,time.strftime('%d.%m.%Y @ %H:%M:%S UTC',time.gmtime(os.stat(main.__file__).st_mtime)),'GNU GPLv3 <http://fsf.org>']

      #manage + control the number of margin in spaces between the body text and right vertical rule
      def calcMgn(lineNumber):
         return toEven(bwinner-(len(LnOpn[lineNumber])+len(LnCtn[lineNumber])))//2

      def calcRMgn(lineNumber):
         return (0-(1-(toEven(((bwinner-(len(LnOpn[lineNumber])+len(LnCtn[lineNumber])))//2),-1))))

      def calcLenOf(lineNumber):
         return len(LnMgn[lineNumber])+len(LnOpn[lineNumber])+len(LnCtn[lineNumber])+calcRMgn(lineNumber)

      def calcRDiff(lineNumber):
         return LnMgnR[lineNumber] - (lenOf[lineNumber] - bwinner)

      def calcRMgnSpaces(lineNumber):
         return str(spa*(toEven(LnMgnRAdjust[lineNumber])-adjust))
      #they're not lists, they're arrays.

      LnMgn=[calcMgn(0)*spa,calcMgn(1)*spa,calcMgn(2)*spa,calcMgn(3)*spa]

      #fix a right-vertical-rule alignment bug whose existence I don't understand

      LnMgnR=[calcRMgn(0),calcRMgn(1),calcRMgn(2),calcRMgn(3)]

      #test strings lengths' relation to bw to fix another bug
      lenOf=[calcLenOf(0),calcLenOf(1),calcLenOf(2),calcLenOf(3)]
      
      LnMgnRAdjust=[calcRDiff(0),calcRDiff(1),calcRDiff(2),calcRDiff(3)]

      LnMgnR_toSpace=[calcRMgnSpaces(0),calcRMgnSpaces(1),calcRMgnSpaces(2),calcRMgnSpaces(3),]
               
      #concatenate strings
      nl='\n'
      addLine=[idt + vl + LnMgn[0] + LnOpn[0] + spa + LnCtn[0] + LnMgnR_toSpace[0] + vr + nl,\
               idt + vl + LnMgn[1] + LnOpn[1] + spa + LnCtn[1] + LnMgnR_toSpace[1] + vr + nl,\
               idt + vl + LnMgn[2] + LnOpn[2] + spa + LnCtn[2] + LnMgnR_toSpace[2] + vr + nl,\
               idt + vl + LnMgn[3] + LnOpn[3] + spa + LnCtn[3] + LnMgnR_toSpace[3] + vr + nl]

      #FOR DEBUGGING
      #w('{} {} {}\nlenA {} lenB {} lenC {} lenD {}\naLnMgn R {} bLnMgn R {} cLnMgn R {} dLnMgn R {}\naLnMgn new {} bLnMgn new {} cLnMgn new {} dLnMgn new {}'.format(width,bw,bwinner,lenA, lenB, lenC, lenD, aLnMgn_R, bLnMgn_R, cLnMgn_R, dLnMgn_R, aLnMgn_new, bLnMgn_new, cLnMgn_new, dLnMgn_new))
      
      
      borderTop = nl + idt + hzt_bw + nl
      cornerTop = idt + clt + spa_inner + crt + nl
      preText = idt + vl + spa_inner + vr + nl
      ### ... ###
      postText = preText
      borderBottom = idt + clb + hzb_bw + crb + nl
      #end def calculateAlign
      
      w('{}{}{}{}{}{}{}{}{}'.format(borderTop,cornerTop,preText,addLine[0],addLine[1],addLine[2],addLine[3],postText,borderBottom))

      ##end def printAttribLn()
   if prnt:w('Prints a customisable header with calculated and adjustable margins, dimensions, and alignments.')
   else:printAttribLn()
#end def header()
if main.__file__ is __file__:
   header()#one day we'll call all of them at once
else:pass
