#include <errno.h>
#include <wchar.h>
#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>
#include <locale.h>
#include <limits.h>
#include <stdbool.h>

#define INT64_MAXDIGITS 22 // 20 for UINT64 + 1 for the sign + 1 for null

int64_t wprompt_int64 (const wchar_t* const, const wchar_t* const);
int64_t wstr_to_uint64 (const wchar_t* const);

void      wchomp (wchar_t**);
wchar_t* wreadln (const size_t);

int main (void) {

  setlocale(LC_ALL, "");

  const wchar_t *pr = L"Enter a number! ",
                *rt = L"Retry: ";

  int64_t a = wprompt_int64(pr, rt),
          b = wprompt_int64(pr, rt);

  if (EINVAL == errno) { return EXIT_FAILURE; }

  wprintf(L"%" PRIi64" - %" PRIi64 " = %" PRIi64 "\n", a, b, a - b);

  return EXIT_SUCCESS;
}

/*
  wprompt_int64: write `prompt` to stdout, then get input and try to turn it
  into an int64.

  if retry_prompt is not NULL, then the byte 4 or an empty line will not close
  the prompt, but print retry_prompt to stdout and ask for input until it is
  found or the program ends.

  if retry_prompt is NULL, then errno is set to EINVAL and 0 is returned the
  first time the byte 4 or an empty line is found.

  otherwise, the value of errno is not set and the input is converted to a
  signed number and returned.
*/
int64_t wprompt_int64 (const wchar_t* const prompt, const wchar_t* const retry_prompt) {

  // retry if retry_prompt is not null
  const bool do_retry = NULL != retry_prompt;

  wprintf(L"%ls", prompt);

  wchar_t* in;
  do {
    in = wreadln(INT64_MAXDIGITS);

    // CTRL-D doesn't write a newline but it looks odd to write the prompt without
    // first writing a newline
    wprintf(L"%ls", NULL == in ? L"\n" : L"");

    if ( !do_retry || ((NULL != in) && in[0] ) ) {
      break;
    }

    free(in);

    wprintf(L"%ls", retry_prompt);
  }
  while ( true );

  if (! in) { errno = EINVAL; return 0; }

  // if wstr_to_uint64 sets errno, let it propogate up
  int64_t out = wstr_to_uint64(in);

  free(in);

  return out;
}

/*
  wstr_to_uint64: convert a wide string to uint64_t


*/
int64_t wstr_to_uint64 (const wchar_t* const buf) {

  wchar_t* end;

  int64_t o = wcstoll(buf, &end, 10);

  if ( (*end) && end != buf) {
    errno = EINVAL;
  }

  return o;
}

wchar_t* wreadln (const size_t chars) {
  wchar_t *buf = (wchar_t *) malloc(chars * sizeof (wchar_t)),
          *sts;

  fflush(stdin);

  sts = fgetws(buf, (int) chars, stdin);

  fflush(stdin);

  if ( (! sts) || '\04' == buf[0] ) {
    free(buf);
    errno = EINVAL;
    return NULL;
  }

  wchomp(&buf);

  return buf;
}

void wchomp (wchar_t** buf) {
  if (! buf) { return; }

  (*buf) [ wcscspn(*buf, L"\n") ] = '\0';
}
