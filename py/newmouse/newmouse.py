#!/usr/bin/env python3.4

import sys, string

TOLERANCE      = 1.0e-6
PI             = 3.14159265358979323846264338327950288419716939937510582097494459230
SPEED_OF_LIGHT = 299792458.0
ELEMENTARY_CHG = 1.60217653e-19
GRAV_ACCEL     = 9.80665
GRAV_CONST     = 6.6742e-11
PLANCK         = 6.6260693e-34
H_BAR          = 1.05457168e-34
PERMEABILITY   = 4.0e-7 * PI
PERMITTIVITY   = 1.0/(PERMEABILITY * SPEED_OF_LIGHT ** 2)
MASS_ELECTRON  = 9.1093826e-31
MASS_PROTON    = 1.67262171e-27
MASS_NEUTRON   = 1.67492728e-27
AVAGADRO       = 6.0221415e23
BOLTZMANN      = 1.3806505e-23
AU             = 1.49597870e11
GM_EARTH       = 3.9860005e14
GM_SUN         = 1.32712438e20
R_EARTH        = 6.378140e6
LB_KG          = 0.45359237
IN_CM          = 2.54
GAL_L          = 3.7854118


DEFAULT_ANGLE_FACTOR   = 1.0
DEFAULT_DISPLAY_MODE   = 2
DEFAULT_DISPLAY_DIGITS = 15
DEFAULT_DISPLAY_WIDTH  = 0
DEFAULT_WORDSIZE       = 32
DEFAULT_OCTHEX_DIGITS  = (DEFAULT_WORDSIZE - 1) / 4 + 1

PROMPT  = "\n > "
VERSION = 1
stack   = []

if len(sys.argv) > 1:
    f = open(sys.argv[1], 'r')
    prog = f.read().split()
    f.close()
    run(prog)
    exit(0)
else:
    print(" newmouse interpreter version", str(VERSION))
    print(" &H")
    while True:
        try:
            f = input(PROMPT)
            prog = f.split()
            run(prog)
        except KeyboardInterrupt:
            print(" exit")
            exit(0)
        except EOFError:
            print()
            exit(0)

def run(prog):
    index = 0
    while index < len(prog):
        element = prog[index]
        if element in string.digits:
            stack.append(int(element))
        elif element in x:
            pass
        else:
            pass
