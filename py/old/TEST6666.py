import time
a=6666
z=[]
while 1:
   for i in range(a,2**31-1): # big number, oops
      if str(i).startswith(str(a)): # check if the number is of the format we want
         b=i**.5 # sqrt it
         if b.is_integer()==True: # if it's an int, print it
            print(b)
