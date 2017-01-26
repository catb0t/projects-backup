import sys, string
x=''
y = ''.join(sorted(list(string.printable)))[5:]
fil = open(sys.argv[1], 'r').read()
for i in range(len(y)):
    if y[i] not in x:
        print(chr(i+32), fil.count(y[i]))
    x += y[i]
