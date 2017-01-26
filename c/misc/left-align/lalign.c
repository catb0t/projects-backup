#include <stdlib.h>
#include <stdio.h>
#include <string.h>

f(s,n,c,p) {
  return memset(p,c,asprintf(&p,"%*s",n,s)-strlen(s));
}

int main(int argc, char const *argv[]) {
  printf("%s\n", f("foo", 5, " "));
  return 0;
}