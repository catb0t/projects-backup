### DEFAULT HEADER INCLUDE
import time,os,sys,random,datetime;import __main__ as main
def header():
   final='nah'
   global a,b,c,d,e,f,g,h,j,k,l,m,o,p,q,r,s,t,u,v,w,x,y,z,lf,tb,ln,us #in my code, <4 char vars (except i and n which are Reserved) are typically global and extremely volatile. stuff that gets set a few times and not read often, gets longer names
   lf='\n';tb='    ';uname='CarterStevens';us='_';ln=(40*us) + lf
   def fib(n):
      a=0;b=1;c=0
      for i in range(0,n):
         t=a;a=b;b=t+b;c+=1;print(a)
      else:return
   def printAttribLn():
      print("",ln,'Name:{0}{1}(from {2})'.format(tb,os.path.basename(__file__),(main.__file__),),lf,'Authors:{0}{1}'.format(tb,uname),lf,'Finalised:{0}{1}({2})'.format(tb,final,os.stat(main.__file__).st_mtime),lf,ln)
   try:
      printAttribLn()
   except OSError:
      
      pass;
      try:
         printAttribLn()
      except OSError:
         print("F A T A L: Tried to handle a basic NameError but it couldn't be resolved successfully!")

header()
