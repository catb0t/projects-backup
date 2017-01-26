#include <stdio.h>

int main (void) {

  freopen("/dev/stdout", "w", stderr);

  fprintf(stderr, "%s\n", "Hello, stderr");

  return 0;
}
