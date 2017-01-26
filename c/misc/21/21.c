#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <inttypes.h>

#define auto __auto_type
#define alloc(type, num) (type *) malloc(sizeof (type) * (num))

int8_t* hand2ints (const char* const hnd);

int main(void) {
  auto x = hand2ints("1 2 9 J Q K");
  for (size_t i = 0; i < 6; i++) {
    printf("%d\n", x[i]);
  }
  return 0;
}

int8_t* hand2ints (const char* const hnd) {
  const size_t hl = strnlen(hnd, 300);
  auto out = alloc(int8_t, hl);

  for (size_t i = 0, j = 0; j < hl; j++) {
    if ( hnd[i] == ' ' ) {
      continue;

    } else if ( hnd[i] <= '9' && hnd[i] >= '1' ) {
      out[i] = (int8_t) abs(hnd[i] - 48);

    } else {
      switch (hnd[i]) {
        case 'A': { i++; out[i] = -1; break; }
        case 'J': { i++; out[i] = 10; break; }
        case 'Q': { i++; out[i] = 10; break; }
        case 'K': { i++; out[i] = 10; break; }

        default: { break; }
      }
    }
  }

  return out;
}
