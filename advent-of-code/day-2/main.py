'day 2 of advent of code'

print(__import__("os").getcwd())
Fopen = open('./advent-of-code/day-2/test_input', 'r').read()
Fopen = Fopen[:len(Fopen)-1]
for i in range(len(Fopen)):
    vals = Fopen.split('x')
    for e in range(len(vals)):
        pass
print(Fopen)
