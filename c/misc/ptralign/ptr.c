#include <stdio.h>
#include <stdlib.h>

void test (const void* const h);

void test (const void* const h) {
  printf("%zd\n", *(const size_t* const) h);
}

int main (const int argc, const char* const * const argv) {
  (void) argc;
  size_t t = (size_t) atoi(argv[1]);

  test(&t);
}
