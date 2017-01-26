#include <inttypes.h>
#include <stdio.h>

void loop (uint64_t);

void main2 (void);

int main(void) {
  //loop(10);
  main2();
}

void loop(const uint64_t n) {
  uint64_t i = n;
  while ( i ) { printf("%" PRIu64 ", %"PRIu64 "\n", n, i = i % 2 ? i + 1 : i / 2); }
}

/*
  The output is:
  10, 1
  10, 2

  Forever.

  The program will never terminate for positive values of n because if i is
  positive and odd, it will be incremented to an even value, which will never be
  0 when divided by 2.
*/

long double fac (const uint64_t);

void main2 (void) {
  printf("%LF, %LF\n", fac(10), fac(100));
}

__attribute_pure__ __attribute((const)) long double fac (const uint64_t n) {
  long double o = 1;
  for (uint64_t i = n; i; i--) {
    o *= i;
  }
  return o;
}
