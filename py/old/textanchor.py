### DEFAULT HEADER INCLUDE ###
yourGodTheCreatorOwner='Carter Stevens <thebinaryminer@gmail.com>'
ETALS=''

import time,os,sys,random,datetime,string,shutil;import __main__ as main
global a,b,c,d,e,f,g,h,j,k,l,m,o,q,r,s,t,u,v,x,y,z #in my code, <4 char vars (except i (and n,w,p) which are Reserved) are typically global and extremely volatile. stuff that gets set a few times and not read often, gets longer names
global one,two,three,four,five,six,seven,eight,nine,ten
one=None;two=3;three='undef';four=3.4;#etc#underhandedness to trick the Unsuspecting Richardi.
global w,p,fibnum,hours,minutes,difference
w=print;p=print; #for a programmer, I'm a very lazy person
#global width,bw,bwinner,bwinner_padding,adjust,hz_t,hz_b,hzt_bw,hzb_bw,vl,vr,clt,crt,clb,crb,spa,spa_inner,idt,LnOpn,LnCtn,LnMgn,LnMgn_R,LnMgn_R_spa,lenOf,LnMgnRAdjust,LnMgnR_toSpace,nl,addLine,borderTop,cornerTop,preText,postText,borderBottom

def fib(n=0,nth=None):
   fibnum = [0, 1]
   for i in range(2,n):
      fibnum.append(fibnum[i-1]+fibnum[i-2])
   if n is 0:
      return None
   elif nth is not None:
      w(fibnum[nth-1])
   else:w(fibnum)

def header(prnt=None):
   def printAttribLn():
      if ETALS: #were there other contributors?
         AUTHORS=yourGodTheCreatorOwner + ', ' + ETALS + ', ' + 'et al.'
      else:AUTHORS=yourGodTheCreatorOwner

      ##since we're doing centering stuff relative to elements left of them and the far-right margin spacing values _M_U_S_T_!!! BE _E_V_E_N_!!
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

      #get how long ago the file was modified
      def calcModDiff():
         difference = time.time() - os.stat(main.__file__).st_mtime
         minutes = int(difference % 3600 / 60)
         hours = int(difference // 3600)
         days = hours // 24
         weeks = days // 7
         if hours + minutes is 0:
            return ' (less than a minute ago)'
         elif days > 30:
            return ' (over a month ago)'
         elif days > 7:
            return ' ({}w ago)'.format(weeks)
         elif days > 0:
            return ' ({}d ago)'.format(days)
         elif hours > 1:
            return ' ({} hour ago)'.format(hours)
         elif hours is 1:
            return ' ({} hour ago)'.format(hours)
         else:return ' ({} minute ago)'.format(minutes)

      #decide a filename
      def fName():
         selfFName=os.path.basename(__file__)
         mainFName=os.path.basename(main.__file__)
         if main.__file__ is __file__:
            return selfFName
         else:
            return '{} ( <- {})'.format(mainFName,selfFName)
         
      #Who doesn't love a bit of ASCII art / styling??

      width = toEven(int(str.split(str.split(str(shutil.get_terminal_size()),'=',1)[1],',',1)[0]))

      bw=int(.85*width)
      bwinner=bw-2
      bwinner_padding=bwinner-2
      adjust=1
      
      #texty things to be messed with
      spa=' ' #ONE character!!
      spa_inner=spa*bwinner #inner spaces width
      #indent should be calculated as
      idt=toEven((width-bw)/2,-1)*spa

      #boxy things to be messed with:
      #note: some character combinations require different setups here
      # BOX BORDER STYLES: OCTAL 57 = /, 134 = \, 137 = _, 174 = |,
      hz_t='\137';hz_b='\137' # horizontal line char! top+bottom ### IF UNDERSCORE USE CHARCODE=OCT(137)
      hzt_bw = spa+(hz_t*bwinner)
      hzb_bw = hz_b*bwinner 
      vl='|';vr='|' #vertical line left/right :: if symmetrical, just set vr to vl
      clt='/';crt='\\' #corner:left top and corner:right top :: / and \
      clb=crt;crb=clt #in the case of \ and /, the diagonal corners are the same.
      
      LnOpn=['filename:','authored by','on','redistributable under the']

      LnCtn=[fName(),AUTHORS,time.strftime('%d.%m.%Y @ %H:%M:%S UTC',time.gmtime(os.stat(main.__file__).st_mtime)) + '{}'.format(calcModDiff()),'GNU GPLv3 || <http://fsf.org>']

      #manage + control the number of margin in spaces between the body text and right vertical rule
      #mathhhhh
      def calcMgn(lineNumber):
         return toEven(bwinner-(len(LnOpn[lineNumber])+len(LnCtn[lineNumber])),-1)//2

      def calcRMgn(lineNumber):
         return (0-(1-(toEven(((bwinner-(len(LnOpn[lineNumber])+len(LnCtn[lineNumber])))//2),-1))))

      def calcLenOf(lineNumber):
         return len(LnMgn[lineNumber])+len(LnOpn[lineNumber])+len(LnCtn[lineNumber])+calcRMgn(lineNumber)

      def calcRDiff(lineNumber):
         return LnMgnR[lineNumber] - (lenOf[lineNumber] - bwinner)

      def calcRMgnSpaces(lineNumber):
         return ((LnMgnRAdjust[lineNumber])-adjust)

      #they're not lists, they're arrays.

      LnMgn=[calcMgn(0)*spa,calcMgn(1)*spa,calcMgn(2)*spa,calcMgn(3)*spa]

      #fix a right-vertical-rule alignment bug whose existence I don't understand

      LnMgnR=[calcRMgn(0),calcRMgn(1),calcRMgn(2),calcRMgn(3)]

      #test strings lengths' relation to bw to fix another bug

      lenOf=[calcLenOf(0),calcLenOf(1),calcLenOf(2),calcLenOf(3)]

      LnMgnRAdjust=[calcRDiff(0),calcRDiff(1),calcRDiff(2),calcRDiff(3)]

      LnMgnR_toSpace=[calcRMgnSpaces(0)*spa,calcRMgnSpaces(1)*spa,calcRMgnSpaces(2)*spa,calcRMgnSpaces(3)*spa,]

      testLen=[LnMgn[0] + LnOpn[0] + spa + LnCtn[0] + LnMgnR_toSpace[0],\
               LnMgn[1] + LnOpn[1] + spa + LnCtn[1] + LnMgnR_toSpace[1],\
               LnMgn[2] + LnOpn[2] + spa + LnCtn[2] + LnMgnR_toSpace[2],\
               LnMgn[3] + LnOpn[3] + spa + LnCtn[3] + LnMgnR_toSpace[3]]

      for i in range(0,3):
         if len(testLen[i]) > bwinner:
            LnMgnR_toSpace[i] = int((toEven(LnMgnRAdjust[i])-adjust)-(len(testLen[i])-bwinner))*str(spa)
            
      #concatenate strings
      nl='\n'
      addLine=[idt + vl + LnMgn[0] + LnOpn[0] + spa + LnCtn[0] + LnMgnR_toSpace[0] + vr + nl,\
               idt + vl + LnMgn[1] + LnOpn[1] + spa + LnCtn[1] + LnMgnR_toSpace[1] + vr + nl,\
               idt + vl + LnMgn[2] + LnOpn[2] + spa + LnCtn[2] + LnMgnR_toSpace[2] + vr + nl,\
               idt + vl + LnMgn[3] + LnOpn[3] + spa + LnCtn[3] + LnMgnR_toSpace[3] + vr + nl]
      
      borderTop = nl + idt + hzt_bw + nl
      cornerTop = idt + clt + spa_inner + crt + nl
      preText = idt + vl + spa_inner + vr + nl
      ### ... ###
      postText = preText
      borderBottom = idt + clb + hzb_bw + crb + nl

      w('{}{}{}{}{}{}{}{}{}{}{}{}'.format(borderTop,cornerTop,preText,addLine[0],preText,addLine[1],preText,addLine[2],preText,addLine[3],postText,borderBottom)) 

      ##end def printAttribLn()
   if prnt:w('Prints a customisable header with calculated and adjustable margins, dimensions, and alignments.')
   else:printAttribLn()
#end def header()
if main.__file__ is __file__:
   header()#one day we'll call all of them at once
else:pass
