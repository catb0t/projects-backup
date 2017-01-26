#include "/home/cat/projects/git/c-projects/calc/object/object.h"
#include <stdio.h>

size_t f (const size_t max, const size_t a, const size_t b);
size_t f2 (const size_t max, const array_t* const divs);

define_array_new_fromctype(size_t);

int main(void) {
  printf("%d\n", f(1000, 3, 5) == 233168);
  static const size_t a[] = {
    3, 5
  };
  array_t* b = array_new_from_size_t_lit(a, 2, t_realuint);
  printf("%d\n", f2(1000, b) == 233168);
  array_destruct(b);
  return 0;
}

size_t f (const size_t max, const size_t a, const size_t b) {
  size_t sum = 0;
  for (size_t i = 0; i < max; i++) {
    sum += (i % a * i % b) ? 0 : i;
  }
  return sum;
}

size_t f2 (const size_t max, const array_t* divs) {
  size_t sum = 0;
  const size_t len = array_length(divs);

  for (size_t i = 0; i < max; i++) {
    size_t mul = 0;
    for (size_t j = 0; j < len; j++) {
      object_t** this = array_get_ref(divs, j, NULL);
      fixwid_t*  num = (*this)->fwi;
      mul *= i % (size_t) num->value;
      fixwid_destruct(num);
    }
    sum += mul ? 0 : i;
  }
  return sum;
}
