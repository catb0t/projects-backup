c=input()
a=[0]
s=0
i=0
def g(i,n):
 p=i
 if n:i+=1
 while c[i].isdigit():i+=1
 a[s]=int(c[p:i]);return i-1
def e():
 a.pop(s);s-=1
while i<len(c):
 d=c[i]
 if d.isdigit():i=g(i,0)
 elif d=='c':s+=1;a.insert(s,0)
 elif d=='d':e()
 elif d=='+':s+=1
 elif d=='-':
  if c[i+1].isdigit():i=g(i,1)
  else:s-=1
 elif d=='o':print(a[s],end=' ')
 elif d=='?':
  if a[s]==0:e()
 elif d=='#':
  if a[s]==0:i+=1
 i+=1