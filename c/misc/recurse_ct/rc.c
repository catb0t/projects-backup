#include <inttypes.h>
#include <stdlib.h>
#include <criterion/criterion.h>

uint64_t sum_odds (const uint64_t upper);

uint64_t sum_odds (const uint64_t upper) {
  return (upper / 2) * (upper / 2);
}

Test(test, ten) {
  cr_assert_eq(sum_odds(10), 25);
}

Test(test, tt) {
  cr_assert_eq(sum_odds(3333), 2775556);
}

