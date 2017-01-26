# header
ax = 0x656
try:
    import head
    from head import *
    #header()
except ImportError:
    from random import *
    while 1: print(chr(randint(0, ax)), end='')
# end

def forward(times):
   i=0
   while i < times:
      s(0.5)
      w('moved between space', sr(i), 'and', sr(i+1))
      i += 1
      
def turn(angle):
   if angle < 90 or angle > 270:
      dirct = 'right'
   else:
      dirct = 'left'
   w('pivoted', sr(angle), 'degrees', dirct)

if main.__file__ is __file__:
   forward(4)
   turn(340)
   
