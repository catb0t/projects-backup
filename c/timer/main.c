#include <stdio.h>
#include <time.h>

int main(void) {
  // Disable stdout buffering
  setvbuf(stdout, NULL, _IONBF, 0);

  clock_t start = clock(), diff;
  int i;
  for (i = 1; i < 1000000; i++) printf("%d", i % (i * 'a'));
  diff = clock() - start;

  long int msec = diff * 1000 / CLOCKS_PER_SEC;
  printf("Time taken %ld seconds %ld milliseconds", msec/1000, msec%1000);
  return 0;
}
