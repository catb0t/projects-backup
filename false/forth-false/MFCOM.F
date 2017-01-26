\ Makefile for a stand-alone 80386 False compiler for BEForth

marker UnFalseCom

include falsecom.f

: FalseCom  ( -- )  \ the do-everything word
  command-line  ['] false-file catch  if
    ." For some reason FalseCom could not compile!" cr
    ." FalseCom command line: FALSECOM FalseFileToCompile" cr cr
    ." But welcome to the 32 bit DOS-extended BEForth. Type BYE to quit." cr
    cr 2drop quit
  else
    cr ." FalseCom didn't have any FATAL errors compiling."
    cr ." Any executable output written to A.COM" cr
    bye
  then ;

' FalseCom is booter
save falsecom.bin  \ huge binary with all of Forth in it :-)
bye
