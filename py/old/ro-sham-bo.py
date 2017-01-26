#ro-sham-bo.py, a rewrite of the one i was trying to update from 2.7
from random import *; from math import *; from time import sleep; #importing from china
r=randint(10000000000000000000,10000000000000000000000000000000000000000000000000000000000000) #debugging symbol.
plList={0:"TURN BACK! THE END IS NIGH",1:"scissors",2:"rock",3:"paper",4:"rock",5:"paper",6:"rock",7:"scissors"}  #By default, the player is more likely to throw a rock
aiList={0:"TURN BACK! THE END IS NIGH",1:"paper",2:"rock",3:"scissors",4:"paper",5:"scissors",6:"paper",7:"rock"} #By default, the AI is more likely to throw paper.
#Playing for some time makes it evident that the AI will eventually win, which hopefully encourages the player to not just roll randoms
global plRoll,aiRoll,gameIsRunning,inert #globvars
#plRoll=pi;aiRoll=pi #check whether the user pressed enter without submitting anything && check whether the ai's selection was properly set??

## doesn't work quiiiite properly... at all
##def roll(mode="all"): #how to roll the "dice" (get it, cause there's six valid choices per array??)
##   if mode == "all": #pl(ayer) aka roll for both
##      a = randint(1,8);if a >= 6: #6 or 7 or 8
##         plRoll = a-(randint(1,5));sleep(1);aiRoll = randint(1,a);return;elif a <= 3: #3 or 2 or 1
##         plRoll = a+(randint(1,5));sleep(1);aiRoll = randint(0,4)+a*(randint(1,2));else:pass;if mode == "cpu": #implying the user chose; now only roll for the compooper
##      pass
##def outcome():pass

gameIsRunning = input('RETURN to play roshambo or <CTRL-C> to exit \n ') #is the game running?
while gameIsRunning is "": #run the game.
   plRoll=0,aiRoll=0,inert=0
   def roll(mode="all"): #how to roll the "dice" (get it, cause there's six valid choices per array??)
      if mode == "all": #pl(ayer) aka roll for both
         a = randint(1,8)
         if a >= 6: #6 or 7 or 8
            plRoll = a-(randint(1,5)) 
            sleep(1)
            aiRoll = randint(1,a)
         elif a <= 3: #3 or 2 or 1
            plRoll = a+(randint(1,5))
            sleep(1)
            aiRoll = randint(0,4)+a*(randint(1,2))
         else:
            plRoll = a
            aiRoll = a // 2 + 1
      if mode == "cpu": #implying the user chose; now only roll for the compooper
         a = randint(1,8)
         if a >= 6: #6 or 7 or 8
            inert = a-(randint(1,5)) 
            sleep(1)
            aiRoll = randint(1,a)
         elif a <= 3: #3 or 2 or 1
            inert = a+(randint(1,5))
            sleep(1)
            aiRoll = randint(0,4)+a*(randint(1,2))
         else:
            inert = a
            aiRoll = a // 2 + 1pass
   def outcome():pass
   
   v = input('[1]:rock ... [2]:paper ... [3]:scissors ... [return]:random \n ') #start interactive mode
   if v == "": #roll something random if player didn't enter anything and instead just hit enter 
      print(plRoll)
      a = randint(1,8)
      if a >= 6: #6 or 7 or 8
         plRoll = a-(randint(1,5)) 
         sleep(1)
         aiRoll = randint(1,a)
      elif a <= 3: #3 or 2 or 1
         plRoll = a+(randint(1,5))
         sleep(1)
         aiRoll = randint(0,4)+a*(randint(1,2))
      else:
         plRoll = a
         aiRoll = a // 2 + 1
      #roll("all"); 
   elif v is 1 or 2 or 3 or 4 or 5 or 6 or 7:
      try:plRoll=int(v);
      except ValueError: print('input malformed or out of range!')
   elif v <= 0: print('input malformed or out of range!')
   elif v > 7: print('input malformed or out of range!')
   if aiRoll == 0:
      if plRoll == 0:
      roll('cpu')
   print(plRoll, aiRoll, "\n")
