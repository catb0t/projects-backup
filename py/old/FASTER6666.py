import math,time
a=6666
for i in range(1*10**10):
   n = math.ceil((a * 10**i)**.5)
   upper = ((a+1) * 10**i)**.5
   while n <= upper:
      print(str(n) + '  |  ' + str(n**2))
      n+=1
