#!/usr/bin/env python3

import math

from itertools import chain, cycle, accumulate # last of which is Python 3 only

def factors(n):
    def prime_powers(n):
        # c goes through 2, 3, 5, then the infinite (6n + 1, 6n + 5) series
        for c in accumulate(chain([2, 1, 2], cycle([2, 4]))):
            if c * c > n: break
            if n % c: continue
            d, p = (), c
            while not n % c:
                n,p,d = n // c, p * c, d + (p,)
            yield d
        if n > 1: yield (n,)

    r = [1]
    for e in prime_powers(n):
        r += [a * b for a in r for b in e]
    return r

def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    return max(filter(is_prime, factors(600851475143)))

if __name__ == '__main__':
    x = main()
    assert(x == 6857)
    print(x)