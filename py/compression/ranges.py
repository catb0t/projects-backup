#!/usr/bin/env python3

"""import random

def dict_zip_me(iterable):
    return dict(zip(iterable, range(len(iterable))))

class SmartKeyPair(object):
    def __init__(self, k, v):

        assert len(k) == len(v), "can't SmartKeyPair objects of disaparate lengths"
        assert iter(k), "need an iterable for keys"; assert iter(v), "need iterable for vals"

        self.keys = dict_zip_me(k)
        self.vals = dict_zip_me(v)
        self.kvpairs = range(len(k))

x = SmartKeyPair(range(10), [random.randint(0, 100)**i for i in range(10)])
print(sorted(x.keys))
print(sorted(x.vals))
y = SmartKeyPair(["a", "b", "c", "d", "e", "f"], [i / random.randint(0, 100) for i in range(6)])
print(sorted(y.keys))
print(sorted(y.vals))"""



def mkrange(length):
    r = [0]
    for i in range(length):
        print(r)
        r.append(r[-1] + 1)

    return r

print(mkrange(9))