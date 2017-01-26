n=4**9;f=[0,1];r=str;
for i in range(1,n):f.append(f[i-1]+f[i-2])
print(r(r(r(f[n])[:1564][::-1].split(' '))[::-1]).split('8'))
