#!/usr/bin/env python3

def main():
    return sum((i for i in range(1000) if (not i % 5) or (not i % 3)))

if __name__ == '__main__':
    x = main()
    assert(x == 233168)
    print(x)