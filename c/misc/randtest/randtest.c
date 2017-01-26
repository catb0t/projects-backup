#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long myStrtoL(const char* str, const int base);
int  myAtoI  (const char* str);

int main(const int argc, const char* argv[]) {

  for (int i = 0; i < argc; i++) {
    const char* str = argv[i];
    int  toi = myAtoI(str);
    long tol = myStrtoL(str, 10);
    printf("#%d %s:\n\ta -> i: %d\n\ts -> l: %ld\n", i, str, toi, tol);
  }

  return EXIT_FAILURE;
}

long myStrtoL(const char* str, const int base) {
  char* ptr;
  long num = strtol(str, &ptr, base);
  if ((!num) && (!strcmp(str, "0"))) {
    return 0;
  }
  return num;
}

int myAtoI(const char* str) {
  int num = atoi(str);
  if ((!num) && (!strcmp(str, "0"))) {
    return 0;
  }
  return num;
}
