#!/usr/bin/env python3

x = []

while True:
    try:
        x += map(lambda a:a.strip(), input().split("\n"))
    except EOFError:
        break

x = list(filter(lambda a: bool(a), x))

for i, e in enumerate(x):
    print(i, e)

print(x)