### DEFAULT HEADER INCLUDE ###
yourGodTheCreatorOwner='catb0t <thebinaryminer@gmail.com>'
ETALS=''
import time,os,sys,random,datetime,string;import __main__ as main
global a,b,c,d,e,f,g,h,j,k,l,m,o,q,r,s,t,u,v,x,y,z #in my code, <4 char vars (except i (and n,w,p) which are Reserved) are typically global and extremely volatile. stuff that gets set a few times and not read often, gets longer names
global one,two,three,four,five,six,seven,eight,nine,ten
one=None;two=3;three='undef';four=3.4;#etc#underhandedness to trick the Unsuspecting Richardi.
global w,p,fibnum,width
w=print;p=print; #for a programmer, I'm a very lazy person

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

      def toEven(n,rnd=1):
         n=int(n)
         if isEven(n) is False:
            if rnd is 1:return n+1
            elif rnd is -1:return n-1
            elif rnd is -1:return n-1
            else:return n+1
         elif isEven(n) is True:return n
         else:raise Exception('MathError','format parameters must be even!')
      
      width=84#toEven(83) #give a shell width (probably 80, so it's the default
      bw=toEven(.75*width,-1)
      bwinner=bw-2

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

      aLnOpn='Name:'
      bLnOpn='Authors:'
      cLnOpn='Modified:'
      dLnOpn='License:'

      aLnCtn=os.path.basename(main.__file__)+' <- '+os.path.basename(__file__)
      bLnCtn=AUTHORS
      cLnCtn=time.strftime('%d.%m.%Y @ %H:%M:%S UTC',time.gmtime(os.stat(main.__file__).st_mtime))
      dLnCtn='GNU GPLv3 <http://fsf.org>'

      #manage + control the number of margin in spaces between the body text and right vertical rule
      aLnMgn=spa*(toEven(bwinner-(len(aLnOpn)+len(aLnCtn)))//2)
      bLnMgn=spa*(toEven(bwinner-(len(bLnOpn)+len(bLnCtn)))//2)
      cLnMgn=spa*(toEven(bwinner-(len(cLnOpn)+len(cLnCtn)))//2)
      dLnMgn=spa*(toEven(bwinner-(len(dLnOpn)+len(dLnCtn)))//2)

      #next four blocks fix a right-vertical-rule alignment bug whose existence I don't understand
      aLnMgn_R = (0-(1-(toEven(((bwinner-(len(dLnOpn)+len(dLnCtn)))//2),-1))))
      bLnMgn_R = (0-(1-(toEven(((bwinner-(len(dLnOpn)+len(dLnCtn)))//2),-1))))
      cLnMgn_R = (0-(1-(toEven(((bwinner-(len(dLnOpn)+len(dLnCtn)))//2),-1))))
      dLnMgn_R = (0-(1-(toEven(((bwinner-(len(dLnOpn)+len(dLnCtn)))//2),-1))))

      #test strings lengths' relation to bw to fix another bug
      lenA=len(aLnMgn)+len(aLnOpn)+len(aLnCtn)+aLnMgn_R
      lenB=len(bLnMgn)+len(bLnOpn)+len(bLnCtn)+bLnMgn_R
      lenC=len(cLnMgn)+len(cLnOpn)+len(cLnCtn)+cLnMgn_R
      lenD=len(dLnMgn)+len(dLnOpn)+len(dLnCtn)+dLnMgn_R
      
      aLnMgn_new = aLnMgn_R - (lenA - bwinner)
      bLnMgn_new = aLnMgn_R - (lenB - bwinner)
      cLnMgn_new = aLnMgn_R - (lenC - bwinner)
      dLnMgn_new = aLnMgn_R - (lenD - bwinner)

      aLnMgn_R_spa = spa*(toEven(aLnMgn_new)-adjust)
      bLnMgn_R_spa = spa*(toEven(bLnMgn_new)-adjust)
      cLnMgn_R_spa = spa*(toEven(cLnMgn_new)-adjust)
      dLnMgn_R_spa = spa*(toEven(dLnMgn_new)-adjust)
      
      #concatenate strings
      aLine= vl + aLnMgn + aLnOpn + spa + aLnCtn + aLnMgn_R_spa + vr
      bLine= vl + bLnMgn + bLnOpn + spa + bLnCtn + bLnMgn_R_spa + vr
      cLine= vl + cLnMgn + cLnOpn + spa + cLnCtn + cLnMgn_R_spa + vr
      dLine= vl + dLnMgn + dLnOpn + spa + dLnCtn + dLnMgn_R_spa + vr

      #FOR DEBUGGING
      w('{} {} {}\nlenA {} lenB {} lenC {} lenD {}\naLnMgn R {} bLnMgn R {} cLnMgn R {} dLnMgn R {}\naLnMgn new {} bLnMgn new {} cLnMgn new {} dLnMgn new {}'.format(width,bw,bwinner,lenA, lenB, lenC, lenD, aLnMgn_R, bLnMgn_R, cLnMgn_R, dLnMgn_R, aLnMgn_new, bLnMgn_new, cLnMgn_new, dLnMgn_new))
      
      nl='\n'
      line_1 = idt + hzt_bw + nl
      line_2 = idt + clt + spa_inner + crt + nl
      line_3 = idt + vl + spa_inner + vr + nl
      line_4 = idt + aLine + nl
      line_5 = idt + bLine + nl
      line_6 = idt + cLine + nl
      line_7 = idt + dLine + nl
      line_8 = line_3
      line_9 = idt + clb + hzb_bw + crb +nl

      w('{}{}{}{}{}{}{}{}{}{}{}'.format(nl,line_1,line_2,line_3,line_4,line_5,line_6,line_7,line_8,line_9,nl))

      ##end def printAttribLn()
   if prnt:w('Prints a customisable header with calculated and adjustable margins and dimensions.')
   else:printAttribLn()

if main.__file__ is __file__:
   header()
else:pass
