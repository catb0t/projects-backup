import string,random
x = ''
cmap = string.printable[:62]
for i in range(2000):
	itr = cmap[random.randint(0,61)]
	if itr not in x:
		x += itr
else:
	print("py 62 char UUID:", x)
