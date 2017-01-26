#include "test.h"

int main (void) {

  size_t len;
  const char* const a = "abc def gh ij asdasd a";

  for (size_t i = 0; i < safestrnlen(a); i++) {
    printf("%c %d\n", a[i], a[i]);
  }
  printf("\n");

  char** spl = str_split(a, ' ', &len);

  for (size_t i = 0; i < len; i++) {
    printf("idx: %zu str: ", i);
    for (size_t j = 0; j < safestrnlen(spl[i]); j++) {
      printf("%d ", spl[i][j]);
    }
    printf("(end)\n");
  }
  // leaks for brevity
  return 0;
}
