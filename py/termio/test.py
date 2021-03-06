import math
import sys

# The only _varaibles_ required for this DEMO...

char = '*'
x = 20
y = 19

# A Simple clear screen command for this DEMO...

for n in range(0, 64, 1):
    print('\r\n')


# This function is just basic for this DEMO but shows the power of the ANSI _Esc_ codes...

def locate(user_string='$VER: Locate_Demo.py_Version_0.00.10_(C)2007-2012_B.Walker_G0LCU.', x=0, y=0):

    # Don't allow any user errors. Python's own error detection will check for
    # syntax and concatination, etc, etc, errors.

    x = int(x)
    y = int(y)
    if x >= 255:
        x = 255
    if y >= 255:
        y = 255
    if x <= 0:
        x = 0
    if y <= 0:
        y = 0
    HORIZ = str(x)
    VERT = str(y)

    # Plot the user_string at the starting at position HORIZ, VERT...

    print(("\033[" + VERT + ';' + HORIZ + 'f' + user_string))


# Plot the upwards slope of the triangle...

while x <= 35:
    locate(char, x, y)
    x = x + 1
    y = y - 1

# Plot the downwards slope of the triangle...

while x <= 52:
    locate(char, x, y)
    x = x + 1
    y = y + 1

# Plot the base of the triangle...

char = '***********************************'
locate(char, 19, 20)

# Write a string inside the triangle...

char = 'Drawing in text mode Python.'
locate(char, 23, 18)

# Print this line BELOW the triangle...

print('''


Cursor now set to the top.''')

# NOW reset the cursor back to the top of the window using the default x and y values.

locate('')

# Hold drawing until user input for sine wave plot...

char = exec(input('Press <CR> to continue with a _sine_ wave:- '))

# A Simple clear screen command for this DEMO...

for n in range(0, 64, 1):
    print('\r\n')

char = '*'
x = 3
y = 12

# Now plot a sinewave curve inside the Terminal.

for angle in range(0, 360, 5):

    # Generate a FLOATING point sine(angle) value...

    angle = float(angle)
    y = math.sin(angle * math.pi / 180.0)

    # INVERT, AND, keep the y scan inside the standard Terminal window size.

    y = 12 - int(y * 10)
    locate(char, x, y)

    # Move along one, (1), x position.

    x = x + 1

# Hold drawing until user input for a final clear screen...

char = \
    exec(input('''









Press <CR> to clear the screen, display the default string, and stop:- '''))

# A Simple clear screen command for this DEMO...

for n in range(0, 64, 1):
    print('\r\n')

# NOW reset the cursor back to the top of the window using the default x and y values
# and display the locate() function's default string...

locate()
