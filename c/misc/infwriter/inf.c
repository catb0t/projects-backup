#include <stdio.h>
main(){for(FILE*f=fopen("a","w");;fputc(0,f),fclose(f));}