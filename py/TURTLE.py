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

t = turtle

def starter():
   #start off
   t.penup()
   t.setx(-100)
   t.sety(-100)
   t.pendown()
   
def m_c():
   # make a c
   t.left(215)
   t.circle(-140,250)

def m_s():
   t.left(140)
   t.circle(70,220)
   t.circle(-70,220)

if main.__file__ is __file__:
   starter()
   m_c()
   t.penup()
   t.left(40)
   t.forward(250)
   t.pendown()
   m_s()
   t.done()#t.bye()
