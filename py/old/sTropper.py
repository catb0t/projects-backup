import re;a=input()
b=a.split(' ')
c=b[0][:1:]
f=[c.upper(),c.lower()]
if f[0] in a or f[1] in a:
   x=re.sub("H",'',(b[i] for i in range(len(b))))
print(x)
