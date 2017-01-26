### DEFAULT HEADER INCLUDE ###
yourGodTheCreatorOwner='Cat Stevens <thebinaryminer@gmail.com>'
ETALS=''
import codecs,base64,time,os,sys,random,datetime,string,shutil;import __main__ as main
global a,b,c,d,e,f,g,h,j,k,l,m,o,q,r,s,t,u,v,x,y,z #in my code, <4 char vars (except i (and n,w,p) which are Reserved) are typically global and extremely volatile. stuff that gets set a few times and not read often, gets longer names
global one,two,three,four,five,six,seven,eight,nine,ten
one=None;two=3;three='undef';four=3.4; #etc #underhandedness to trick the Unsuspecting Richardi.
global w,p,fibnum,hours,minutes,difference,mTime
mTime = os.stat(main.__file__).st_mtime
w=print;p=print;q=input #for a programmer, I'm a very lazy person
#global width,bw,bwinner,bwinner_padding,adjust,hz_t,hz_b,hzt_bw,hzb_bw,vl,vr,clt,crt,clb,crb,spa,spa_inner,idt,LnOpn,LnCtn,LnMgn,LnMgn_R,LnMgn_R_spa,lenOf,LnMgnRAdjust,LnMgnR_spa,nl,addLine,brdTop,crnTop,preTxt,postText,borderBottom

def fib(n=0,nth=None):
   fibnum = [0, 1]
   for i in range(2,n):
      fibnum.append(fibnum[i-1]+fibnum[i-2])
   if n is 0:
      return None
   elif nth is not None:
      try:
         w(fibnum[nth-1])
      except IndexError:
         w('can\'t return value outside list index buffer')
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
            if rounds is 1:
               if isEven(n+1) is True:
                  return n+1
            elif rounds is -1:
               if isEven(n-1) is True:
                  return n-1
            else:
               if isEven(n+1) is True:
                  return n+1
         elif isEven(n) is True:return n
         else:raise Exception('MathError','format parameters must be even!')

      #get how long ago the file was modified
      def calcModDiff():
         difference = time.time() - mTime
         minutes = int(difference % 3600 / 60)
         hours = int(difference // 3600)
         days = hours // 24
         weeks = days // 7
         months = days // 30
         years = months // 12
         if hours + minutes is 0:
            return ' (less than a minute ago)'
         elif years > 5:
            return ' (half a decade ago: cat, marry alex!)'
         elif years > 1:
            return ' ({} years ago)'.format(years)
         elif years > 0:
            return ' (a year ago)'
         elif months > 1:
            return ' ({} months ago)'.format(months)
         elif months > 0:
            return ' (a month ago)'
         elif weeks > 1:
            return ' ({} weeks ago)'.format(weeks)
         elif weeks > 0:
            return ' ({} week ago)'.format(weeks)
         elif days > 1:
            return ' ({} days ago)'.format(days)
         elif days > 0:
            return ' ({} day ago)'.format(days)
         elif hours > 1:
            return ' ({} hours ago)'.format(hours)
         elif hours > 0:
            return ' ({} hour ago)'.format(hours)
         elif minutes > 1:
            return ' ({} minutes ago)'.format(minutes)
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

      LnOpn=['filename:', 'authored by', 'on', 'redistributable under the']

      LnCtn=[fName(), AUTHORS, time.strftime('%d-%m-%Y @ %H:%M:%S UTC',time.gmtime(mTime)) + calcModDiff(), 'GNU GPLv3 || <http://fsf.org>']

      #manage + control the number of margin in spaces between the body text and right vertical rule
      #mathhhhh
      def calcMgn(lnNum):
         return toEven(bwinner-(len(LnOpn[lnNum])+len(LnCtn[lnNum])),-1)//2

      def calcRMgn(lnNum):
         return (0-(1-(toEven(((bwinner-(len(LnOpn[lnNum])+len(LnCtn[lnNum])))//2),-1))))

      def calcLenOf(lnNum):
         return len(LnMgn[lnNum])+len(LnOpn[lnNum])+len(LnCtn[lnNum])+calcRMgn(lnNum)

      def calcRDiff(lnNum):
         return LnMgnR[lnNum] - (lenOf[lnNum] - bwinner)

      def calcRMgnSpa(lnNum):
         return ((LnMgnRAdjust[lnNum])-adjust)

      #they're not lists, they're arrays.

      LnMgn=[calcMgn(0)*spa,calcMgn(1)*spa,calcMgn(2)*spa,calcMgn(3)*spa]

      #fix a right-vertical-rule alignment bug whose existence I don't understand

      LnMgnR=[calcRMgn(0),calcRMgn(1),calcRMgn(2),calcRMgn(3)]

      #test strings lengths' relation to bw to fix another bug

      lenOf=[calcLenOf(0),calcLenOf(1),calcLenOf(2),calcLenOf(3)]

      LnMgnRAdjust=[calcRDiff(0),calcRDiff(1),calcRDiff(2),calcRDiff(3)]

      LnMgnR_spa=[calcRMgnSpa(0)*spa,calcRMgnSpa(1)*spa,calcRMgnSpa(2)*spa,calcRMgnSpa(3)*spa,]

      testLen=[LnMgn[0] + LnOpn[0] + spa + LnCtn[0] + LnMgnR_spa[0],\
               LnMgn[1] + LnOpn[1] + spa + LnCtn[1] + LnMgnR_spa[1],\
               LnMgn[2] + LnOpn[2] + spa + LnCtn[2] + LnMgnR_spa[2],\
               LnMgn[3] + LnOpn[3] + spa + LnCtn[3] + LnMgnR_spa[3]]

      for i in range(0,3):
         if len(testLen[i]) > bwinner:
            LnMgnR_spa[i] = int((toEven(LnMgnRAdjust[i])-adjust)-(len(testLen[i])-bwinner))*str(spa)

      #concatenate strings
      nl='\n'
      addLine=[idt + vl + LnMgn[0] + LnOpn[0] + spa + LnCtn[0] + LnMgnR_spa[0] + vr + nl,\
               idt + vl + LnMgn[1] + LnOpn[1] + spa + LnCtn[1] + LnMgnR_spa[1] + vr + nl,\
               idt + vl + LnMgn[2] + LnOpn[2] + spa + LnCtn[2] + LnMgnR_spa[2] + vr + nl,\
               idt + vl + LnMgn[3] + LnOpn[3] + spa + LnCtn[3] + LnMgnR_spa[3] + vr + nl]

      brdTop = nl + idt + hzt_bw + nl
      crnTop = idt + clt + spa_inner + crt + nl
      preTxt = idt + vl + spa_inner + vr + nl
      ### ... ###
      postTxt = preTxt
      brdBtm = idt + clb + hzb_bw + crb + nl

      w('{}{}{}{}{}{}{}{}{}{}{}{}'.format(brdTop,crnTop,preTxt,addLine[0],preTxt,addLine[1],preTxt,addLine[2],preTxt,addLine[3],postTxt,brdBtm))

      ##end def printAttribLn()
   if prnt:w('Cevagf n phfgbzvfnoyr urnqre jvgu pnyphyngrq naq nqwhfgnoyr znetvaf, qvzrafvbaf, naq nyvtazragf.')
   else:printAttribLn()
#end def header()
if main.__file__ is __file__:
   header(1)
else:pass
