import random
program="3 93102" ##Place program here
program=program.split()
length=int(program[0])

random.seed(int(program[1]))
chars="".join(map(chr,range(32,127)))+'\n'
prog="".join([chars[int(random.random()*96)] for i in range(length)])

print("Your program:\n----------------------------------------\n", prog, "\n----------------------------------------\n")
