### DEFAULT HEADER INCLUDE ###
yourGodTheCreatorOwner="Carter 'Cat' Stevens"
ETALS=''
import time,os,sys,random,datetime,string;import __main__ as main
global a,b,c,d,e,f,g,h,j,k,l,m,o,q,r,s,t,u,v,x,y,z,lf,tb,ln,us #in my code, <4 char vars (except i (and n,w,p) which are Reserved) are typically global and extremely volatile. stuff that gets set a few times and not read often, gets longer names
global one,two,three,four,five,six,seven,eight,nine,ten
one=None;two=3;three='undef';four=3.4;#etc#underhandedness to trick the Unsuspecting Richardi.
global w,p,fibnum

w=print;p=print; #for a programmer, I'm a very lazy person

def fib(n):
	fibnum = [0, 1]
	for i in range(2,n):
	    fibnum.append(fibnum[i-1]+fibnum[i-2])
	w(fibnum)
	
def header(prnt=None):
   def printAttribLn():
      
      #Who doesn't love a bit of ASCII art / styling??

      if ETALS: #were there other contributors?
         AUTHORS=yourGodTheCreatorOwner + ", " + ETALS + ', ' + 'et al.'
      else:AUTHORS=yourGodTheCreatorOwner

      #boxy things to be messed with:
      bw = 70 #box width!
      # 57 = /, 134 = \, 137 = _, 174 = |,  
      hrt='\137';hrb=hrt # horizontal line char! top+bottom ### IF UNDERSCORE USE CHARCODE=OCT(137)
      if hrb is hrt: hl=hrt; hlbw = hl*bw #
      vl='\174';vr=vl #vertical line left/right :: if symmetrical, just set vr to vl
      clt='\57';crt='\134' #corner:left top and corner:right top :: / and \
      clb=crt;crb=clt #in the case of \ and /, the diagonal corners are the same.
      
      #texty things to be messed with
      nbs=' ' #nonbreaking spaces. They matter.
      nbw=nbs*bw #inner spaces width
      nbd=nbs+nbs #nonbreaking default for between rowname and rowtext
      pr=(bw//8) #ratio to use for the left inner margin
      pre=vl+(pr*nbs) #turn the left inner margin into actual nbsps and add the preceding char
      fn=pre+'Name:{}'.format(nbd+(4*nbs)+os.path.basename(main.__file__)+' <- '+os.path.basename(__file__))
      fa=pre+'Author/s:{}'.format(nbd+AUTHORS)
      ft=pre+'Modified:{}'.format(nbd+time.strftime('%d.%m.%Y @ %H:%M:%S UTC',time.gmtime(os.stat(main.__file__).st_mtime)))
      fg=pre+'License:{}'.format(nbd+(1*nbs)+'GNU GPLv3 <http://fsf.org>')

      #manage + control the number of spaces after the body text
      neol=(bw-len(fn)+1)*nbs; aeol=(bw-len(fa)+1)*nbs; teol=(bw-len(ft)+1)*nbs; geol=(bw-len(fg)+1)*nbs

      #concatenate strings
      nstr=fn+neol;astr=fa+aeol;tstr=ft+teol;gstr=fg+geol

      #indent should be calculated as(80 // 79 - (<inner-width> + <extras=2> = total width))
      idt=int(((80-bw)//2)-1)*nbs
      #arbitrary=int(80//(79-int(max(len(nstr),len(astr),len(tstr),len(gstr)))-4))*nbs
      
      w('''
{}{}{}
{}{}{}{}
{}{}{}{}
{}{}{}
{}{}{}
{}{}{}
{}{}{}
{}{}{}{}
{}{}{}{}

      '''.format(\
               nbs,  idt,   hlbw,      \
               idt,  clt,   nbw,   crt,\
               idt,  vl,    nbw,   vr, \
               idt,  nstr,  vr,        \
               idt,  astr,  vr,        \
               idt,  tstr,  vr,        \
               idt,  gstr,  vr,        \
               idt,  vl,    nbw,   vr, \
               idt,  clb,   hlbw,  crb,\
               )
            )
      ### CONCATENATED ###
      ### w('{}{}{}\n{}{}{}{}\n{}{}{}{}\n{}{}{}\n{}{}{}\n{}{}{}\n{}{}{}\n{}{}{}{}\n{}{}{}{}'.format(nbs,idt,hlbw,idt,clt,nbw,crt,idt,vl,nbw,vr,idt,nstr,vr,idt,astr,vr,idt,tstr,vr,idt,gstr,vr,idt,vl,nbw,vr,idt,clb,hlbw,crb))         
      ##end def printAttribLn()
   if prnt:w('Prints a customisable header with calculated and adjustable margins and dimensions.')
   else:printAttribLn()
   
if main.__file__ is __file__:
   header()
else:pass
