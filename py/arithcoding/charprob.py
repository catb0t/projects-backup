#!/usr/bin/env python3

from decimal import *

def getprob(string):
    """get the probability of characters in a string"""
    probs = {}
    for e in string:
        c = string.count(e)
        probs[e] = (
            c,
            c / len(string),
        )
    return probs

res = getprob("abc@")
print(" " + "\n ".join(i + "=" + str(res[i]) for i in res))