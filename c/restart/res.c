#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main (int argc, char** argv) {

  (void) argc;

  printf("arg: %s\n", argv[1]);

  fopen("./res", "re");

  int count = atoi(argv[1]);

  if ( getchar() == 'y' ) {

    ++count;

    char buf[20];
    sprintf(buf, "%d", count);

    char* newargv[3];
    newargv[0] = argv[0];
    newargv[1] = buf;
    newargv[2] = NULL;

    execve(argv[0], newargv, NULL);
  }

  return count;
}
