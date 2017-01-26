#include <stdio.h>

/*
  We're going to solve Project Euler problem # 2:
  Sum the even fibonacci numbers below 4e6.
*/

long fib(long n);

int main(void) {

  long upto = 4000000, t = 0, sum = 0, f = fib(0);

  while ((f = fib(t++)) < upto) {

    if (!(f % (long)2))
      sum += f;

  }
  printf("%ld\n", sum);
  return 0;
}

long fib(long n) {
  long fnow = 0, fnext = 1, tempf;

  while (--n > 0) {
    tempf = fnow + fnext;
    fnow = fnext;
    fnext = tempf;
  }
  return fnext;
}