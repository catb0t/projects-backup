#include <locale.h>
#include <wchar.h>
#include <stdlib.h>
#include <stdio.h>

int main(const int argc, const char* const * const argv) {
  (void) argc;

  setlocale(LC_ALL, argv[1]);

  const size_t len = (size_t) atoi(argv[2]);

  wchar_t *buf = (wchar_t *) malloc(sizeof (wchar_t) * len),
         *stat = fgetws(buf, (int) len, stdin);

  wprintf(L"[%ls], [%ls]\n", stat, buf);

  free(buf);

  wprintf(L"we are still: %ls\n", L"alive");

  return EXIT_SUCCESS;
}
