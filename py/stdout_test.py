#!/usr/bin/env python3

import sys
from unicodedata import normalize

isascii = (lambda struni:
            (len(normalize('NFD', struni).encode('ascii', 'replace'))
                == len(struni)))

class myStdout(object):
    def __init__(self):
        pass

    def write(self, *args, **kwds):
        # remove stuff, etc
        return sys.__stdout__.write(
            "".join(
                " ".join(args)
                .replace("µ", "micro")
            )
        )

    def flush(self, *args, **kwds):
        return sys.__stdout__.flush()

NO_UNICODE_OUT = bool(len(sys.argv) - 1)

if NO_UNICODE_OUT:
    print("stdout switcheroo")
    sys.stdout = s = myStdout()

print(input("> "))
