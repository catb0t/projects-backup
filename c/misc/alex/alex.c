#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct {
  unsigned int a;
  unsigned int* gdata;

} data_t;

data_t* data_new (const unsigned int a);
void data_dtor (data_t* const d);

data_t* data_new (const unsigned int a) {
  data_t
    *out = malloc(sizeof (data_t)),
    sout = {
      .a = a,
      .gdata = malloc(sizeof (unsigned int) * a)
  };

  for (unsigned int i = 0; i < a; i++) {
    (sout.gdata) [i] = i;
  }

  return memcpy(out, &sout, sizeof sout);
}

void data_dtor (data_t* const d) {
  free(d->gdata);
  free(d);
}

int main(void) {

  data_t* m = data_new(6);

  for (size_t i = 0; i < 6; i++) {
    printf("%u ", m->gdata[i]);
  }

  data_dtor(m);

  char* a = malloc(5);

  free(a + 3);

  return 0;
}

