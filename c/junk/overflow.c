#include <stdio.h>
#include <math.h>
#include <limits.h>
int main(void) {
  double i = pow(2, 128);
  int j    = (int) i;
  printf("int max:          %d\n", INT_MAX);
  printf("print dbl as int: %d\n", i);
  printf("cast dbl -> int:  %d\n", j);
  printf("double:           %f\n", i);
	return 0;
}
