from math import*
I=int
S=" "
C=","
L=len
P=print
def d(i):
 l=["","January","February","March","April","May","June","July","August","September","October","November","December"];w=i.split('/');f=I(w[0]);s=I(w[1]);y=w[2]
 if f>12:e=I(w[1]);P(l[e]+S+w[0]+C+S+y)
 elif f<13and s>12:e=I(w[0]);P(l[e]+S+w[0]+C+S+y)
 else:
  if f<s:o=l[f];t=l[s]
  else:o=l[s];t=l[f];o=o[0:I(ceil(L(o)/2))];t=t[I(ceil(L(t)/2)):L(t)]
  P(o+t+S+str(floor((f+s)/2))+C+S+y)
