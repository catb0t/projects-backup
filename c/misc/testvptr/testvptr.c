#include <stdio.h>
#include <stdlib.h>

void f (void* a, const size_t len, const size_t align);

void f (void* a, const size_t len, const size_t align) {

  ssize_t* s = (ssize_t *) a;
  (void) s;

  printf("len: %zu align: %zu len * align: %zu\n", len, align, len * align);

  for (size_t i = 0; i < len; i++) {
    printf("%zd\n", s[i]);
  }
}

int main (void) {

  ssize_t* s = malloc(5 * sizeof(ssize_t));

  for (ssize_t i = 0; i < 5; i++) {
    s[i] = i;
    printf("%zu\n", s[i]);
  }

  f(s, 5, sizeof (ssize_t));
}
