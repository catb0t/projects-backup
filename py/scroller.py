import time;s=input()*80
while 1:print("\033[2J",end=s[:80],flush=1);s=s[1:]+s[0];time.sleep(.1)
