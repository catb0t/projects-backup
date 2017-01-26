#!/usr/bin/env python3
is_pal = lambda n: str(n)[::-1] == str(n)

import builtins
from itertools import chain, cycle, accumulate # last of which is Python 3 only

any = lambda *t: builtins.any(t)
all = lambda *t: builtins.all(t)

def main():
    seen = set()
    for i, j in enumerate(range(100, 1000)): [seen.add(i) for i in [i * i, i * j, j * j]]
    f = map(is_pal, seen)
    return max(filter(lambda i: i[1], zip(seen, f)))
    #max(filter(is_pal, seen))


if __name__ == '__main__':
    x = main()[0]
    print(x)