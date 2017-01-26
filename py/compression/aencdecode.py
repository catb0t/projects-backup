#!/usr/bin/env python3

from getprobs import getprobs
import random


def encode(string, prob):
	lo = 0
	hi = 1
	for i, e in enumerate(string):
		r = hi - lo
		hi = lo + r * probs[e][1]
		lo = lo + r * probs[e][0]
	return __import__("random").uniform(hi, lo)


def decode(num, prob):
    string = []
    while True:
        for symbol in prob.keys():
            start, width = prob[symbol]
            if 0 <= num - start < width:
                num = (num - start) / width
                string.append(symbol)
                break
        if symbol == '@':
            break

    return ''.join(string)

m = "BILL GATES@"
p = getprobs(m)
result = encode(m, p)
print(result)
result = 0.2572167752
r2 = decode(result, p)
print(r2)
