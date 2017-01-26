#include <stdlib.h>
#include <stdio.h>
#include <stdarg.h>

#define call(self, md, ...) self->md(self, __VA_ARGS__)
#define call_v(self, md) self->md(self)
#define setattr(self, attr, val) self->attr = (val)
#define getattr(self, attr) ((self)->(attr))

typedef struct st_test test_t;

typedef struct st_test {
  size_t data;

  void (* set_data) (test_t* const, const size_t);
  size_t (* get_data) (const test_t* const, ...);
  void (* dtor) (test_t* const, ...);
} test_t;

test_t*     test_new (const size_t);
void    _test_setter (test_t* const, const size_t);
size_t  _test_getter (const test_t* const t, ...);
void   test_destruct (test_t* const, ...);

test_t* test_new (const size_t data) {
  test_t* t   = malloc(sizeof (test_t));
  t->data     = data;
  t->set_data = _test_setter;
  t->get_data = _test_getter;
  t->dtor     = test_destruct;

  return t;
}

void test_destruct (test_t* const t, ...) {
  free(t);
}

void _test_setter (test_t* const t, const size_t data) {
  t->data = data;
}

size_t _test_getter (const test_t* const t, ...) {
  return t->data;
}

int main (void) {

  test_t* t = test_new(5);

  printf("%zu\n", call_v(t, get_data));
  call(t, set_data, 10);

  printf("%zu\n", call_v(t, get_data));

  call_v(t, dtor);
}
