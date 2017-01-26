#!/usr/bin/env python3.6

"""Counts subsquares."""


def add_one_if_mod (sq_size, side_len):
    """Add one if not S mod N."""
    return abs( ( sq_size % side_len ) - 1 )


def count_subsquares_oflen(sq_size, side_len):
    """Count subquares of a size in a square."""
    squareme = side_len - (sq_size + 1)
    return ( abs(squareme) ** 2 ) + add_one_if_mod(sq_size, side_len)


def count_subsquares(sq_size):
    """Count the number of subsquares in a square of size N."""
    side_lens = [i for i in range(2, sq_size)]
    return sum(map(lambda i: count_subsquares_oflen(sq_size, i), side_lens))


for i in range(2, 51):
    print( f"{i}:", count_subsquares(i) )
