#!/usr/bin/env python2

import sys

if sys.stdout.isatty():
    print "Hello tty"
else:
    print "stdin: not a typewriter"

