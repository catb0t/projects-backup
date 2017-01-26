#!/bin/bash
if [[ $UID != "0" ]]; then echo "run me as root" && exit ; fi
OUT=""
s="|/-\\"
for _ in `seq 1 25`; do
  echo 3 > /proc/sys/vm/drop_caches
  printf "\r${s:i=++i%4:1}"
  this=$( ( time ./89 $1 ) 3>&1 1>/dev/null 2>&3 \
    | grep real \
    | cut -f2 \
    | python3 -c 'print( input()[2:-1] )')
  OUT="$OUT
$this"
done
echo -ne '\b \b'
prog=$(printf 'use Math::Round "nlowmult"; while (<>) { $ln++; $a += $_ }; print "%s, " . nlowmult(0.001, $a / $ln);' $1)
echo "$OUT" | perl -e "$prog"