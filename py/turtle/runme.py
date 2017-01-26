# header
ax = 0x656
try:
    import head
    from head import *
    header()
    timeMe('start')
except ImportError:
    from random import *
    while 1: print(chr(randint(0, ax)), end='')
# end

j = turtle.Turtle() #we create a turtle called j (Jack?)

def g(n):
    j.forward(100)
    j.left(n)

j.setx(60)
j.speed(10000000000000000000000000000000000000000000000000000)

g(160)
g(-43)
g(270)
g(-97)
g(-43)
g(200)
g(-940)
g(17)
g(-86)

w('Final heading is', j.heading(), 'degrees')
w('done in',sr(timeMe('show') * 1000), 'msec')
turtle.Screen().exitonclick()
