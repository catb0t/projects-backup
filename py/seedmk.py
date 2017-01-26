import random,time
endprog='hey' #Place program here
triespersec=800000 #approximate number of tries per second (to calculate time needed)
seed=0          #Starting seed. Modify if running multiple in parallel

chars="".join(map(chr,range(32,127)))+'\n'
length=len(endprog)
p=96**length
seconds=p/triespersec
prog,n="",0

print("Program length is {0} characters.\n95^{0}={1} possibilities.".format(length,p))
if seconds > 86400:
    print("Estimated time: {0} days, {1} hours".format(int(seconds/86400),int(seconds%86400/3600)))
elif seconds > 3600:
    print("Estimated time:{0} hours {1} minutes".format(int(seconds/3600),int(seconds%3600/60)))
elif seconds > 60:
    print("Estimated time:{0} minutes {1} seconds".format(int(seconds/60),int(seconds%60)))
else:
    print("Estimated time:{0} seconds".format(seconds))
print("Brute-forcing seed...")

seconds=time.clock()
while prog != endprog:
    n+=1
    random.seed(seed)
    prog = ""
    for t in range(1,length+1):
        prog += chars[int(random.random()*96)]
        if endprog[:t] != prog:
            seed += 1
            break
seconds=time.clock()-seconds
print('Found seed for "{0}"!\nSeed program:\n{1} {2}'.format(prog,length,seed))
print("Time elapsed: {0} seconds. Tries per second:{1}".format(seconds,int(n/seconds)))
