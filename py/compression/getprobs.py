#!/usr/bin/env python3

from decimal import Decimal, getcontext

getcontext().prec = 3


def _nodupsfreq(string):
    """list deduplicator & freq counter"""
    l, res = [], []
    for ch in string:
        if ch not in l:
            l.append(ch)
            res.append(string.count(ch))
    return l, res


def getprobs(string):
    """return a set of probability range for a string"""
    k, v = _nodupsfreq(string)
    collate = {}
    rs = [(0, 0)]
    for i in range(len(v)):
        nxt = (v[i] / len(string))
        prange = (rs[-1][1], rs[-1][1] + nxt)
        rs.append(prange)
        collate[k[i]] = prange

    return collate

m = "aKHAFHLKFKLJHlkhlkjhkshdlfjhsdkfh"
x = getprobs(m)
__import__("pprint").pprint(x)
