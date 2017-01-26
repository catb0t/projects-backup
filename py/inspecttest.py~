from inspect import *
def a():
	cf = currentframe()
	go = getouterframes(cf)
	for frame in go:
		print(frame.lineno, frame.code_context[0])
def b():
	a()
b()
