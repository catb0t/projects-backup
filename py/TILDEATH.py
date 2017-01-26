n=s='\n';m=',';X='[';Y=']';c=';';A='~ATH';D='import';b,g,k=[],[],[];r=range;l=len;f=open('t','r').read().split(n)
def d(j,u):
 p=[]
 for e in j:
  if e!=u:p.append(e)
 return''.join(p)
for h in r(l(f)):f[h]=f[h].split('//')[0].split()
while[]in f:f.remove([])
for h in r(l(f)):
 i=f[h]
 if i[0]==D and l(i)==2and i[1][l(i[1])-1]==c and d(i[1],c)not in b:g.append(0);b.append(d(i[1],c))
 elif i[0].startswith(A):
  i=i[0].split('){')
  for e in r(l(i)):
   if i[e].startswith(A):
    i[e]=i[e].split('(')
    if i[0][1]in b:g[b.index(i[0][1])]+=(i[1].count('+')-i[1].count('-'))
 elif i[0].startswith('bifurcate')and l(i)==2and i[1][l(i[1])-1]==c:
  i=i[1].split(X)
  if i[0] in b:
   z=d(d(i[1],c),Y).split(m)
   for e in r(l(z)):g.append(g[b.index(i[0])]);b.append(z[e])
   g.remove(g[b.index(i[0])]);b.remove(i[0])
 elif i[0].startswith(X)and i[0].endswith('.DIE();')and l(i)==1:
  z=d(i[0],X).split(Y)[0].split(m)
  for e in r(l(z)):
   k.append((z[e],g[b.index(z[e])]))
for e in r(l(k)):k0=k[e][0];k1=k[e][1];s+=k0+'='+str(k1)+n+('DIE '+k0+n)*abs(k1)
print s
