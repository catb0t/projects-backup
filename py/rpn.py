#!/usr/bin/env python3.4

# simple rpn calculator in python3

import string

stack = []
ops = "+-*=/\\."

def main():
    expr = input("> ").split()
    for i in range(len(expr)):
        if expr[i] in string.digits:
            stack.append(float(expr[i]))
        elif expr[i] in ops:
            if expr[i] == ops[0]:
                stack.append(stack.pop() + stack.pop())
            elif expr[i] == ops[1]:
                stack.append(stack.pop() - stack.pop())
            elif expr[i] == ops[2]:
                stack.append(stack.pop() * stack.pop())
            elif expr[i] == ops[3]:
                stack.append(float(stack.pop() == stack.pop()))
            elif expr[i] == ops[4]:
                stack.append(stack.pop() / stack.pop())
            elif expr[i] == ops[5]:
                stack.append(float(stack.pop() % stack.pop()))
            elif expr[i] == ops[6]:
                try:
                    ret = stack.pop()
                    print(ret)
                except IndexError:
                    print("stack underflow: not enough items on stack")
        else:
            print("junk char at", i)
    #print(stack)

while 1:
    main()
