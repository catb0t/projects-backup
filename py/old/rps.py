#begin default_header
import head
from head import *
head.header()
time.sleep(1)
#endit
global score,bad,plRandom
plList={1:'scissors',2:'rock',3:'paper'}
aiList={1:'rock',2:'paper',3:'scissors'}
bad = 'bad input - try again \n'

def roll(both=None):
   if both:
      plRoll = plList[random.randint(1,3)]
      time.sleep(1)
      aiRoll = plList[random.randint(1,3)]
      return 'you roll {}\nai rolls {}\n'.format(plRoll,aiRoll)
   else:
      aiRoll = aiList[random.randint(1,3)]
      return str(aiRoll)

playing=q('enter to play\n ')
while playing is "":
   chz=q('1(scissors) 2(rock) 3(paper) or enter(random)\n')
   try:
      chz=int(chz)
   except:pass
   if chz is "":
      plRandom = True
   if type(chz) is int:
      plRandom = False
      plRoll = plList[chz]
   else:pass
   if plRandom is True:w(roll(1))
   else:
      w(plRoll, roll())
