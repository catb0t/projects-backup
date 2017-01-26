#include <stdio.h>

int main(int argc, char const *argv[]) {
  do {
    printf("%s\n", argc++ % 2 ? (const char *) argc : "");
  } while (argc < 100);
  return 0;
}
