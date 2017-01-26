#!/usr/bin/env python3

def main():
    import re
    from sys import argv
    with open(argv[1], "r") as f:
        fct = f.read()

    fct
        .replace("CAN HAS", "using")
        .replace("HOW IZ I", "function")
        .replace("IM OUTTA YR", "done")
        .replace("I HAS A", "var")
        .replace
