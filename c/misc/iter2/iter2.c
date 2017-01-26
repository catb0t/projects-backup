#include "/home/cat/projects/c/misc/iter2/iter2.h"

int main(void) {

  srand( (uint32_t) time(NULL) );

  uint64_t input;

  printf("Which problem? enter a number in 0..5 or (0 for all) ");
  fflush(stdout);

  if (!getuint64(&input)) {
    insult_user();
    return EXIT_FAILURE;
  }

  // input == 0
  if (!input) {
    for (size_t i = 0; i < NUM_PROBS; i++) {
      (* problem_funs[i])();
    }
  // 0 < input < 6
  } else if (input < (NUM_PROBS + 1)) {
    (* problem_funs[input - 1])();

  // input > 5
  } else {
    insult_user();
    return EXIT_FAILURE;
  }

  return EXIT_SUCCESS;
}
