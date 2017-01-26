#!/usr/bin/env python3


def main():
    a, b, n = 0, 1, 0

    while a < int(4e6):
        a, b = b, a + b
        n += a if not a % 2 else 0
    return n

if __name__ == '__main__':
    x = main()
    assert(x == 4613732)
    print(x)