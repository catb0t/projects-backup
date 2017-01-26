#include "/home/cat/projects/c/misc/iter/iter.h"

int main(void) {

  // a lot of things need this
  srand( (uint32_t) time(NULL) );
  uint64_t input;

  printf("Which problem? enter a number in 0..5 or (0 for all) ");
  fflush(stdout);

  if (!get_uint64(&input)) {
    return EXIT_FAILURE;
  }

  // input == 0
  if (!input) {
    for (size_t i = 0; i < NUM_FUNCS; i++) {
      (* func_ptrs[i])();
    }
  // 0 < input < 6
  } else if (input < (NUM_FUNCS + 1)) {
    (* func_ptrs[input - 1])();

  // input > 5
  } else {
    insult_user();
    return EXIT_FAILURE;
  }

  return EXIT_SUCCESS;
}

