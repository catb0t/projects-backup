#!/usr/bin/env python3

import os, sys, readline

def main():
    try:
        os.stat(sys.argv[1])
    except:
        interpret()
    else:
        f = open(sys.argv[1])
        prog = f.read()
        f.close()
        parse(prog)

def interpret():
    while True:
        try:
            parse(input("bf; "))
        except KeyboardInterrupt:
            print("\n;;")
        except EOFError:
            exit(0)

class Program(object):
    def __init__(self):
        self.tape = [0] * 2 ** 10
        self.ptr  = 0

    def incr(self):
        self.tape[self.ptr] += 1

    def decr(self):
        self.tape[self.ptr] -= 1

    def rmov(self):
        self.ptr += 1

    def lmov(self):
        self.ptr -= 1

    def wnum(self):
        d = sys.stdout.write(str(self.tape[self.ptr]) + "\n")

    def emit(self):
        d = sys.stdout.write(chr(self.tape[self.ptr]))

    def inp(self):
        self.tape[self.ptr] = input()[0]

    def nxtbr(self):
        ct = 1
        for i, e in enumerate(self.tape):
            if ct == 0:
                return i
            if e == "[":
                ct += 1
            elif e == "]":
                ct -= 1
        #raise SyntaxError("no matching brace")

    def lstbr(self):
        t = self.tape[::-1]
        ct = 1
        for i, e in enumerate(t):
            if ct == 0:
                return i
            if e == "[":
                ct -= 1
            elif e == "]":
                ct += 1
        #raise SyntaxError("no matching brace")

    def goto(
            self: object,
            i: int
        ) -> None:
        self.ptr = i

    def lb(self):
        if self.tape[self.ptr] == 0:
            self.goto(self.nxtbr())

    def rb(self):
        if self.tape[self.ptr] != 0:
            self.goto(self.lstbr())

def parse(prog):
    tape = Program()
    for idx, elem in enumerate(prog):
        if elem == "+":
            tape.incr()
        elif elem == "-":
            tape.decr()
        elif elem == ">":
            tape.rmov()
        elif elem == "<":
            tape.lmov()
        elif elem == ".":
            tape.emit()
        elif elem == ",":
            tape.inp()
        elif elem == "[":
            tape.lb()
        elif elem == "]":
            tape.rb()
        elif elem == ";":
            tape.wnum()

if __name__ == "__main__":
    main()