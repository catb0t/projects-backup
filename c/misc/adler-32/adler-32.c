#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int h,l,m=65521;
int A (const char* B) {
  int h = 0, l = 1;
  while (*B) {
    h += l += *B++;
  }
  return h % m << 16 | l % m;
}

/*
const char* string_repeat(const char str, const unsigned int times) {
  void* container = malloc(sizeof (char) * times);
  char* newstr = (char *) memset(container, str, times);
  newstr[times + 1] = '\0';
  return newstr;
}*/

int main(void) {
  printf("%u\n", A("?"));
  return 0;
}