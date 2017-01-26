#!/bin/bash
D=$(expr "$1" '*' '2')
P="print $D * '4'"
python -c "$P" | valgrind ./f en_US.utf8 $1