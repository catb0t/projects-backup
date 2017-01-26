#include <assert.h>
#include <inttypes.h>
#include <limits.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <stdio.h>
#include <time.h>

#define MAX_STR_LEN 1024
char*      chomp (char* const str);
char*     readln (const size_t len);
char*     str_rm (
  const char*   str,
  const size_t  len_str,
  const char*   omit,
  const size_t  len_omit,
        size_t* out_len
);
char** str_split (
  const char*   str,
  const size_t  len,
  const char    delim,
        size_t* out_len
);

size_t   str_count (
  const char*   haystack,
  const size_t  len_haystack,
  const char*   needle,
  const size_t  len_needle
);
size_t safestrnlen (const char* str);

void      _safefree (void*  ptr, uint64_t lineno);
void*   _safemalloc (size_t len, uint64_t lineno);

#define safefree(x) _safefree(x, __LINE__)
#define safemalloc(x) _safemalloc(x, __LINE__)

int main(void) {
  size_t out;

  char*   str = readln(512);

  const size_t slen = safestrnlen(str);

  char* str2 = str_rm(str, slen, " ", 1, &out);

  printf("str: %s len: %zu\n", str2, out);

  const char delim = ',';

  char** bits = str_split(str2, out, delim, &out);

  safefree(str);
  safefree(str2);

  for (size_t i = 0; i < out; i++) {
    printf("%s\n", bits[i]);
  }
  safefree(*bits);
}

char* readln (const size_t len) {
  char* buf = safemalloc( sizeof(char) * len );
  fgets(buf, MAX_STR_LEN, stdin);
  return chomp(buf);
}

char* chomp (char* const str) {
  if (!str) { return NULL; }
  char* new = (char *) str;
  new[ strcspn(new, "\n") ] = 0;
  return new;
}

// safestrnlen -- find the length of a string, defaulting to MAX_STR_LEN, without segfaulting
size_t safestrnlen (const char* str) {
  // it seems gnu strnlen segfaults on null pointer (aka empty string), so let's fix that
  if (!str) { return 0; }
  return strnlen(str, MAX_STR_LEN);
}

// _safefree -- free a pointer to allocated memory or die freeing NULL
void _safefree (void* ptr, uint64_t lineno) {
  if (!ptr) {
    printf("You fool! You have tried to free() a null pointer! (line %" PRIu64 ")\n", lineno);
    assert(ptr);
  } else {
    free(ptr);
  }
}

// _safemalloc -- allocate memory or die
void* _safemalloc (size_t len, uint64_t lineno) {
  void* mem = malloc(len);
  if (!mem) {
    printf("Couldn't malloc() %zu bytes (perhaps you have run out of memory?) (line %" PRIu64 ")\n", len, lineno);
    assert(mem);
  }
  return mem;
}

char** str_split (
  const char*   str,
  const size_t  len,
  const char    delim,
        size_t* out_len
) {

  char delim_str[1],
      *str_copy = strndup(str, MAX_STR_LEN);

  sprintf(delim_str, "%c", delim);

  size_t num_delim = str_count(str, len, delim_str, 1),
         len_new   = num_delim + 2;

  char** new       = safemalloc( len_new );

  if (!num_delim) {
    // no separator found
    new[0]   = str_copy;
    new[1]   = 0;
    *out_len = 1;
  } else {
    // separator found
    size_t i;
    for (i = 0; i < len_new; i++) {
      new[i] = strsep(&str_copy, delim_str);
    }
    new[i]   = 0;
    *out_len = i - 1;
  }

  assert(out_len != NULL);
  return new;
}

char*     str_rm (
  const char*   str,
  const size_t  len_str,
  const char*   omit,
  const size_t  len_omit,
        size_t* out_len
) {
  // malloc one more than exactly enough for the new string
  const size_t len_new = ( ( ( sizeof(char) * len_str ) - str_count(str, len_str, omit, len_omit) ) );
  char*            new = safemalloc( len_new + 1 );

  printf("%zu\n", len_new);

  char c[1];

  size_t i, j;
  for (i = 0, j = 0; j < len_new; i++) {
    sprintf(c, "%c", str[i]);
    if (!str_count(omit, len_omit, c, 1)) {
      new[j] = str[i];
      j++;
    }
  }
  new[j] = 0;
  *out_len = len_new;
  assert(out_len != NULL);
  return new;
}

size_t str_count (
  const char*   haystack,
  const size_t  len_haystack,
  const char*   needles,
  const size_t  len_needles
) {
  size_t s = 0;
  char c;

  for (size_t i = 0; i < len_haystack; i++) {
    c = haystack[i];
    for (size_t h = 0; h < len_needles; h++) {
      if (c == needles[h]) {
         s++;
       }
    }
  }
  return s;
}
