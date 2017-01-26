#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <errno.h>
#include <limits.h>
#include <inttypes.h>

int main(void) {

  printf("%" PRIu64 ", %G, %F, %LG\n", UINT64_MAX, HUGE_VAL, HUGE_VALF, HUGE_VALL);

  fopen(__FILE__, "r");
  printf("errno = %s\n", ENOENT == errno ? "ENOENT" : "not set");

  errno = 0;

  fopen("idonotexist", "r");
  printf("errno = %s\n", ENOENT == errno ? "ENOENT" : "not set");

  errno = 0;

  unsigned long long r1 = strtoul("32578634534523458765467345", NULL, 10);
  printf("r1    = %llu\n", r1);
  printf("errno = %s\n", ERANGE == errno ? "ERANGE" : "not set");

  errno = 0;

  double r2 = strtod("34e375452345345345", NULL);
  printf("r2    = %G\n", r2);
  printf("errno = %s\n", ERANGE == errno ? "ERANGE" : "not set");

  errno = 0;

  r2 = strtod("INF", NULL);
  printf("r2    = %G\n", r2);
  printf("errno = %s\n", ERANGE == errno ? "ERANGE" : "not set");

  errno = 0;

  long double r3 = strtold("34e375452345345345", NULL);
  printf("r3    = %LG\n", r3);
  printf("errno = %s\n", ERANGE == errno ? "ERANGE" : "not set");

  errno = 0;

  r3 = strtold("INF", NULL);
  printf("r3    = %LG\n", r3);
  printf("errno = %s\n", ERANGE == errno ? "ERANGE" : "not set");

  return 0;

}


