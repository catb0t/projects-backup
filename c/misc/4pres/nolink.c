#include <stdio.h>

int f(int);

int main (void) {
  return f(1);
}

int f (int a) {
  return a + 1;
}

