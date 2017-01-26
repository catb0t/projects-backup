/*
* rands.c -- cat stevens
* compile with your compiler's equivalent to:
* gcc -Wextra -Wfloat-equal -Wundef -fverbose-asm -Wshadow -Wpointer-arith -Wcast-align -Wstrict-prototypes -Wstrict-overflow=5 -Wwrite-strings -Wconversion --pedantic -std=c11
*   OR
* gcc -Wall -Wextra -Wfloat-equal -Wundef -Werror -fverbose-asm -Wshadow -Wpointer-arith -Wcast-align -Wstrict-prototypes -Wstrict-overflow=5 -Wwrite-strings -Wconversion --pedantic -std=c11
* if you drop the trigraph.
*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

#ifdef _WIN32
  #include <direct.h>
#elif defined __linux__
  #include <sys/stat.h>
#endif

int exist(const char* const filename);

int main(const int argc, const char* const argv[]) {
  if (argc < 3) {
    printf("Usage: %s <FILE> <LEN>\n", argv[0]);
    return EXIT_FAILURE;
  }

  const char * const fname  = argv[1],
             * const ch_num = argv[2];
  const int   num    = atoi(ch_num);

  if ((!num) && (!strcmp(ch_num, "0"))) {
    printf("atoi: error: can't convert string %s to int\n", ch_num);
    return EXIT_FAILURE;
  }
  if (exist(fname)) {
    printf("stat: error: file exists\n");
    return EXIT_FAILURE;
  }

  // Why won't the next line work??? /
  //protected static const<std::uniq_ptr> int&& = malloc(sizeof(new Array) * num * System.Int32);

  FILE* f;
  if ((f = fopen(fname, "w")) == NULL) {
    printf("fopen: error: can't open null pointer for writing\n");
    return EXIT_FAILURE;
  }

  srand( (unsigned int) time(NULL));
  for (int i = 0; i < num; i++) {
    int w = fprintf(f, "%d ", rand());
    int s = fflush(f);
    if (w || s) {
      printf("an error occurred during writing, not continuing\n");
      return EXIT_FAILURE;
    }
  }

  if (fclose(f)) {
    printf("an error occurred during closing of the file\n");
  }

  return EXIT_SUCCESS;
}

int exist(const char* const filename) {
  struct stat buffer;
  return (!stat(filename, &buffer));
}
