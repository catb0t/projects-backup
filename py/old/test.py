#Stevens/Carter
from time import *; from random import * #importing from china
pl = {0:"nul",1:"r",2:"p",3:"s"}; plT = {0:"nul",1:"rock",2:"paper",3:"scissors"}; ai = {0:"nul",1:"p",2:"s",3:"r"}; aiT = {0:"nul",1:"paper",2:"scissors",3:"rock"} #dictionaries. we're technically allocating 16 addresses when we should be allocating half that but it's okay

global pVal,aVal,rd,res,sFloat,mal; sleep(1) #lotsa global vars.

mal = 'malformed input: {}'; i1 = input(" RETURN to play ro/sham/bo or CTRL-C // <<ANY KEY>> to cancel\n "); #in order: a you-typed-junk-try-again template, a random token to check if the user hit enter or not, the preceding's part #2, and a prompt.


def not_set():
    pVal = randint(1,4)
    if pVal is 4: #randomise it a bit further in case the user is lazy and just presses enter:
        aVal = 4-(randint(2,4)) 
        pVal = randint(1,3)


#you know what really annoys me? if I use good old fashioned strict high-level method chaining on a while loop that tests the veracity of input, the loop breaks!!! :: try: while int(input("myprompt\n ") in (""): (...) except ValueError: (...)
while i1 in (""): #while True;
    pVal = input("(1)rock, (2)paper, (3)scissors, (ret)urn: ")
    if pVal is None:
        not_set()
    elif pVal is not 1 or 2 or 3: #
        print(mal.format(pVal))
    else:            
        try:
            pVal = int(pVal)
            break
        except ValueError:
            not_set()
    res = pVal/aVal
    print('\n{0} / {1}\n'.format(plT[pVal], aiT[aVal])) 
    #PL > AI ::: r > s > p > r...
    # paper / paper = 2, paper / rock = 2/3, paper / scissors = 1
    #
    print(res, "\n ")
