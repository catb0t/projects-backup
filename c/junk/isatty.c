#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main (void) {
  const char* fds[] = {"stdin", "stdout", "stderr"};

  for (int i = 0; i < 3; i++) {
    printf("%s is%s a tty\n", fds[i], isatty(i) ? "" : "n't");
  }
  return EXIT_SUCCESS;
}