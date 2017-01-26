#include <stdio.h>

int main(void) {
  fputs("STDERR", stderr);
  fputs("STDOUT", stdout);
  return 0;
}