#include <stdio.h>

typedef enum {
  t_F, // only false value
  t_number,
  t_fixwid,
  t_string,
  t_func,
  t_array,
  t_hash,
  t_pair,
  t_realint,
  t_realchar,
  NUM_OBJTYPES
} objtype_t;

static const objtype_t CHAR_2OBJTYPE[] = {
  ['f' - 97] = t_F,
  ['n' - 97] = t_number,
  ['z' - 97] = t_fixwid,
  ['s' - 97] = t_string,
  ['q' - 97] = t_func,
  ['a' - 97] = t_array,
  ['h' - 97] = t_hash,
  ['p' - 97] = t_pair,
  ['i' - 97] = t_realint,
  ['c' - 97] = t_realchar
};

_Static_assert(
  ( (sizeof CHAR_2OBJTYPE) / (sizeof (objtype_t)) == ('z' - 97 + 1)),
  "CHAR_2OBJTYPE has too few or too many values"
);

int main (void) {
  for (size_t i = 0; i < 26; i++) {
    printf("index %zu: %d\n", i, CHAR_2OBJTYPE[i]);
  }
}
