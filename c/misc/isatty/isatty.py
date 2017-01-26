#!/usr/bin/env python2

import sys, os

if sys.stdout.isatty():
    print "Hello tty %s" % os.ttyname(1)
else:
    print "stdout: not a typewriter: how boring"
