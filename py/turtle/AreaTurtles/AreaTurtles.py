# header
ax = 0x656
try:
    import head
    from head import sp, dt, t, nl, w
    head.header()
    t1 = head.Timer(1)
except ImportError:
    from random import *
    while 1: print(chr(randint(0, ax)), end='')
# end

class Area(object):
    '''runtime for area calculators'''

    def __init__(self, base=None, height=None, radius=None):

        var = ('base', 'height', 'radius')
        arglist = [base, height, radius]
        types = (float, int)

        for i in range(len(arglist)):
            if type(arglist[i]) in types and type(arglist[i]) != None:
                try:
                    float(arglist[i])
                except:
                    raise TypeError('expected a number but got junk instead')
            elif type(arglist[i]) == None:
                pass

        self.args = {var[i]:arglist[i] for i in range(len(arglist))}

    def rect(self):
        base = self.args['base']
        height = self.args['height']
        area = float(head.Round(base * height).trim())
        return area

    def circ(self):
        radius = self.args['radius']
        area = float(head.Round((head.math.pi * radius) ** 2).trim())
        return area

    def tri(self, no_force_trim=False):
        base = self.args['base']
        height = self.args['height']
        if no_force_trim == False:
            area = head.Round((base * height) / 2).trim()
        else:
            area = ((base * height) / 2)
        return float(area)

    def house(self):
        base = self.args['base']
        height = self.args['height']
        area_rect = (base * height)
        area_tri = (Area(base * .5, height).tri('no_force_trim')) * 2
        total_area = area_rect + area_tri
        return float(total_area)

class TRuntime(object):
    '''underlying runtime for all turtle classes & classmethods'''
    def __init__(self):
        head.turtle.setup(.99,.99)
        Monty = head.turtle.Turtle() # Monty is the uncanonical name for the Python project's mascot
        ActEnv = head.turtle.Screen()

        ActEnv.bgcolor('black')
        ActEnv.title('Monty Runtime')

        Monty.color('white')
        Monty.pensize('2')
        Monty.ht()

        self.tty = Monty
        self.env = ActEnv

        self.resolve_center = lambda: self.tty.pu(); self.tty.setx(0); self.tty.seth(0); self.tty.pd()

    def rect(self, base, height=None):
        if height == None:
            height = base
        heading = 0

        self.tty.begin_fill()

        if height == base:
            while heading < 360:
                self.tty.seth(heading)
                self.tty.fd(base)
                heading += 90

        else:
            i = 0
            while heading < 360:
                self.tty.seth(heading)
                if head.isEv(i) == False:
                    self.tty.fd(base)
                else:
                    self.tty.fd(height)
                heading += 90
                i += 1

        self.tty.end_fill()
        self.env.exitonclick()

    def circ(self, radius):
        self.tty.begin_fill()
        self.tty.circle(radius)
        self.tty.end_fill()
        self.env.exitonclick()
        
    def tri(self, mode):
        if type(mode) == list and type(mode[0]) == str:
            mode[1] = float(mode[1])
            heading = 0
            if mode[0] == 'iso':
                mode = mode.remove(mode[0])
                for i in range(len(mode)):
                    mode[i] = float(mode[i])
                
            elif mode[0] == 'right':
                hypo = mode[1]
                leg = mode[2]
                leg2 = (hypo ** .5) / 2

                self.tty.begin_fill()

                self.tty.seth(heading)
                self.tty.fd(hypo)

                heading += 90

                self.tty.seth(heading)
                self.tty.fd(leg2)

                self.tty.seth(heading)
                self.tty.fd(leg)
                self.tty.end_fill()

            elif mode[0] == 'equi':
                self.tty.begin_fill()
                for i in range(3):
                    self.tty.seth(heading)
                    self.tty.fd(mode[1])
                    heading += 120
                self.tty.end_fill()
            else:
                raise ValueError('invalid triangle type')
        self.env.exitonclick()
        
    def house(self, base):
        height = base
        heading = -90

        self.tty.begin_fill()

        if height == base:
            while heading < 360:
                self.tty.seth(heading)
                self.tty.fd(base)
                heading += 90

        else:
            i = 0
            while heading < 360:
                self.tty.seth(heading)
                if head.isEv(i) == False:
                    self.tty.fd(base)
                else:
                    self.tty.fd(height)
                heading += 90
                i += 1

        heading = 90 
        self.tty.seth(heading)
        self.tty.fd(base)
        
        base /= 2
        height /= 2

        hypo = ((base ** 2) + (height ** 2)) ** .5

        self.tty.seth(0)
        self.tty.fd(base)

        self.tty.seth(heading)
        self.tty.fd(height)
        heading += 135
        self.tty.seth(heading)
        self.tty.fd(hypo)

        self.tty.seth(0)
        self.tty.fd(base * 2)
        self.tty.end_fill()
        self.tty.begin_fill()
        heading -= 180
        self.tty.seth(heading)
        
        heading += 90
        self.tty.seth(heading)
        self.tty.fd(hypo)
        heading += 135
        self.tty.seth(heading)
        self.tty.fd(hypo)

        self.tty.end_fill()
        self.env.exitonclick()        

rect = lambda base, height: Area(base, height).rect()
tri = lambda base, height: Area(base, height).tri()
circ = lambda radius: Area(radius=radius).circ()
house = lambda base, height: Area(base, height).house()
mkrect = lambda base, height: TRuntime().rect(base, height)
mkcirc = lambda radius: TRuntime().circ(radius)
mktri = lambda mode, len_a, len_b: TRuntime().tri([mode, len_a, len_b])
mkhouse = lambda base: TRuntime().house(base)
