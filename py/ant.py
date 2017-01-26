#!/usr/bin/env python3.6
combin = "\u030c"
antdirs = {"u": "^", "d": "v", "l": "<", "r": ">"}

def print_matrix(m):
    for i in m:
        for j in i:
            print(j, end=" ")
        print()


def matrix_find(m, o):
    for idx, elt in enumerate(m):
        for idy, elt2 in enumerate(elt):
            if elt2 == o:
                return (idx, idy)

    return None


def next_iteration(m):
    nl = {k: matrix_find(m, v) for k, v in antdirs.items()}
    direction, pos = list(
        {k: v for k, v in nl.items() if v is not None}.items()
    )[0]



def main(n):
    m = [
        ["." for j in range(n)]
        for i in range(n)
    ]
    m[n // 2][n // 2] = antdirs["l"]
    print_matrix(m)
    next_iteration(m)

if __name__ == '__main__':
    main(10)
