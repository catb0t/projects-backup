#!/usr/bin/env python3
import signal, subprocess as subp

# Intercept ctrl-c, ctrl-\ and ctrl-z
def signal_handler(signal, frame):
    pass
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGQUIT, signal_handler)
signal.signal(signal.SIGTSTP, signal_handler)

subp