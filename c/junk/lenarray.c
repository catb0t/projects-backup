#include <stdio.h>

int main(int argc, char const *argv[]) {
  printf("%d, %d", argc, sizeof(argv));
  return 0;
}