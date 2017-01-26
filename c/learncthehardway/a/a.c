#include <stdio.h>

int main(int argc, char *argv[]) {
  // go through each string in argv

  for (int i = 0; i < argc; printf(argv[i++]));
  return 0;
}
