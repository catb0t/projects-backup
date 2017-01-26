#include <stdio.h>
#include <limits.h>
#include <stdint.h>
#include <inttypes.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

bool qualifies (const uint64_t);
size_t       f (const size_t);


int main(const int argc, const char* const * const argv) {
  (void) argc;
  if (! (argc - 1)) { return 1; }
  size_t arg = strtoull(argv[1], NULL, 10);
  uint64_t a = f(arg);
  printf("a: %" PRIu64 "\n", a);
  return 0;
}

bool qualifies (const uint64_t num) {
  char s[21];
  snprintf(s, 20, "%" PRIu64 "", num);

  uint64_t sum  = 0,
           mult = 1;
  size_t    len = strnlen(s, 400);

  for (size_t i = 0; i < len; i++) {
    uint64_t a = (uint64_t) s[i] - 48;
    sum += a, mult *= a;
  }

  //printf("sum: %" PRIu64 "\nmult: %" PRIu64 "\n", sum, mult);
  return sum * mult ? (! (num % sum)) && (! (num % mult)) : false;
}

size_t f (const size_t n) {
  uint64_t x = 0;
  size_t s_len = 1;
  uint64_t* nums = malloc(sizeof (uint64_t) * s_len);

  while (s_len <= n) {
    if (qualifies(x)) {
      ++s_len;
      //printf("len: %zu\n", s_len);
      nums = realloc(nums, sizeof (uint64_t) * s_len);
      nums[s_len - 1] = x;
    }
    ++x;
  }

  uint64_t o = nums[n];
  free(nums);
  return o;
}
