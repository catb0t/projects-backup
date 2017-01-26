#include <stdlib.h>
#include <stdio.h>

int main (void) {

  char* s = malloc(sizeof (char) * 10);
  char* r = fgets(s, 9, stdin);

  puts(s);
  puts(r);

  return 0;
}
