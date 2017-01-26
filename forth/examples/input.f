: INPUT$ ( n -- addr n )
   PAD SWAP ACCEPT
   PAD SWAP ;

: INPUT# ( -- n true | d 1 | false )
  16 INPUT$ SNUMBER? ;
