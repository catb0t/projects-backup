#include <assert.h>
#include <stdlib.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdio.h>

#define MAX_STR_LEN 1048
#define safestrnlen(x) strnlen((x), MAX_STR_LEN)

size_t str_count (
  const char*   haystack,
  const char*   needles
);

char** str_split (
  const char*   str,
  const char    delim,
        size_t* out_len
);

size_t str_count (
  const char*   haystack,
  const char*   needles
) {
  size_t s = 0,
         len_haystack = safestrnlen(haystack),
         len_needles = safestrnlen(needles);

  for (size_t i = 0; i < len_haystack; i++) {
    char c = haystack[i];
    for (size_t h = 0; h < len_needles; h++) {
      if (c == needles[h]) {
         s++;
       }
    }
  }
  return s;
}

char** str_split (
  const char*   str,
  const char    delim,
        size_t* out_len
) {

  char delim_str[2],
       *str_copy = strndup(str, MAX_STR_LEN);

  snprintf(delim_str, 2, "%c", delim);


  size_t len = safestrnlen(str);
  size_t num_delim = str_count(str, delim_str);
  printf("count: %zu\n", num_delim);

  char** new;


  if (0 == num_delim) {
    // no separator found
    new      = malloc( sizeof (char *) );
    new[0]   = str_copy;
    *out_len = 1;

  } else if (1 == num_delim) {

    // one separator
    new = malloc( sizeof (char *) * 2 );
    size_t i;
    for (
      i = 0;
      (i < len) && str[i] != delim;
      i++
    );
    str_copy[i] = '\0';
    new[0] = str_copy;
    new[1] = &(str_copy[i + 1]);
    *out_len = 2;

  } else {
    // separators found, alloc two more
    size_t num_pieces = num_delim + 2;

    new = malloc( sizeof (char *) * num_pieces );

    printf("pieces: %zu\n", num_pieces);

    size_t i;
    char* token;

    for (i = 0;
      (token = strsep(&str_copy, delim_str)) != NULL;
      i++
    ) {
      new[i] = token;
    }

    *out_len = i;

  }

  assert(out_len != NULL);
  return new;
}
