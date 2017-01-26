#include <assert.h>
#include <inttypes.h>
#include <limits.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <stdio.h>
#include <time.h>

#include "insults.h"

#define DEC_BASE    10
#define DEC_DIGITS  "0123456789"
#define INT_DIGITS  10
#define ULL_DIGITS  20
#define NUM_FUNCS   5
#define NUM_INSULTS (( sizeof(insults) / sizeof(insults[0] )) - 1)
// don't buffer overflow; use strn* instead!
// always use this macro for arg #2 to strn*
#define MAX_STR_LEN 1024

// utils
char*         chomp (      char* str);
char*        str_rm (const char* str, const size_t len_i, const   char* omit, const size_t  len_o);
char**    str_split (const char* str, const size_t len,   const   char  delim,      size_t* out);
bool   str_contains (const char* str, const size_t len,   const   char c);
bool          isEOL (const char* str);
bool     get_uint64 (uint64_t* restrict dest);
size_t    str_count (const char* str, const size_t len_str, const char* needles, const size_t len_needles);
uint64_t rand_range (uint64_t max);
uint64_t* s2numlist (const char* str, const size_t len, size_t* out_len, const char* remove_me, const char split_at_me);
void  problem_intro (const uint8_t problem_number);
void    insult_user (void);
void*      safefree (void* ptr,   uint lineno);
void*    safemalloc (size_t len,  uint lineno);
size_t  safestrnlen (const char* str);

// problem 1
uint64_t  count_div (const uint64_t range, const uint64_t div_by);
void   count_helper (void);
// problem 2
// I hereby promise not to give this function any NULL pointers.
uint64_t        sum (const uint64_t xs[static 1], const size_t len);
void     sum_helper (void);
// problem 3
uint64_t  factorial (const uint64_t n);
void    fact_helper (void);
// problem 4
bool     guess_game (const uint64_t upper, const uint64_t tries, uint64_t *outcome);
void   guess_helper (void);
// problem 5
// I hereby promise not to give this function any NULL pointers.
uint64_t        max (const uint64_t xs[static 1], const size_t len);
void     max_helper (void);

void (* func_ptrs[NUM_FUNCS]) (void) = {count_helper, sum_helper, fact_helper, guess_helper, max_helper};

/*
  "If ptr is a null pointer, no action shall occur." -- POSIX.1-2008
  But if I'm free()-ing a pointer I already free()-d, then something is wrong.
*/
// safefree -- free a pointer to allocated memory, or warn and error on freeing NULL.
// not a drop-in for free(3) -- use it like ptr = safefree(ptr, __LINE__) so the result is NULL.
void* safefree (void* ptr, uint lineno) {
  if (ptr == NULL) {
    printf("You fool! You have tried to free() a null pointer! (line %u)\n", lineno);
    assert(ptr != NULL);
  } else {
    free(ptr);
  }
  return NULL;
}

// safemalloc -- allocate memory, minimising boilerplate
void* safemalloc (size_t len, uint lineno) {
  void* mem = malloc(len);
  if (mem == NULL) {
    /*
      On Windows, MSVCRT does not support the z prefix for size_t and ssize_t
      http://msdn.microsoft.com/en-us/library/tcxf1dw6.aspx
      it expects %I(o|u|x|X) (capital eye) which means this is undefined beahviour
      but I could not be bothered with conditional compilation for one rarely used
      format string. if malloc fails, you deserve a segfault anyways.
    */
    printf("Couldn't malloc() %zu bytes (perhaps you have run out of memory?) (line %u)\n", len, lineno);
    assert(mem != NULL);
  }
  return mem;
}

// safestrnlen -- find the length of a string, defaulting to MAX_STR_LEN, without segfaulting
size_t safestrnlen (const char* str) {
  // it seems gnu strnlen segfaults on null pointer (aka empty string), so let's fix that
  if (!str) { return 0; }
  return strnlen(str, MAX_STR_LEN);
}

// get_uint64 -- read STDIN and cast to uint64_t
// returns false if the input wasn't a number, and writes the cast result to *dest
bool get_uint64 (uint64_t* restrict dest) {
  // it just so happens I think scanf() is really ugly and dumb
  // and this was a learning experience

  char in_buf_size[ULL_DIGITS + 1],
      *in_buf = chomp(fgets(in_buf_size, ULL_DIGITS, stdin));

  fflush(stdin);

  // in_buf was \n, \r or EOF
  if (isEOL(in_buf)) {
    printf("found EOF before input, finishing.\n");
    return false;
  }

  // if removing all the digits from a string leaves a non-empty string
  // then that string is not a number
  if (
    safestrnlen(
      str_rm( in_buf, safestrnlen(in_buf), DEC_DIGITS, safestrnlen(DEC_DIGITS) )
    )
  ) {
    insult_user();
    printf("That's no number!\n");
    return false;
  }

  *dest = (uint64_t) strtoull(in_buf, NULL, DEC_BASE);
  assert(dest != NULL);

  return true;
}

// to prevent me from accidentally dereferencing null pointers
// isEOL -- test if a string is NULL, zero-length or \n
bool isEOL(const char* str) {
  return !str       // NULL
    || !safestrnlen(str) // NULL ?????
    || str[0] == 10 // \n
    || str[0] == 13 // \r
    || str[0] == 4; // 0x04 (CTRL-D)
}

/*
  could be void chomp (char** str);
  and used like chomp(&str);
  but that would be longer
  http://stackoverflow.com/a/28462221/4532996 */
// chomp -- cut the first newline from a string
// for single lines, equivalent to ruby's gets.chomp
char* chomp (char* str) {
  if (!str) { return NULL; }
  str[ strcspn(str, "\r\n") ] = 0;
  return str;
}

// str_contains -- test if char c is in char* str
// more efficient than, but boolean-equivalent to str_count
bool str_contains (const char* str, const size_t len, const char c) {
  for (size_t i = 0; i < len; i++) {
    if (str[i] == c) { return true; }
  }
  return false;
}

// str_count -- count occurrences of any of needles in str
size_t str_count (const char* str, const size_t len_str, const char* needles, const size_t len_needles) {
  size_t s = 0;
  char c;

  for (size_t i = 0; i < len_str; i++) {
    c = str[i];
    for (size_t h = 0; h < len_needles; h++) {
      if (c == needles[h]) { s++; }
    }
  }
  return s;
}

// str_rm -- remove all instances of the contents of *omit from str and return new memory
// result must be freed!
char* str_rm (const char* str, const size_t len_i, const char* omit, const size_t len_o) {

  char* new;

  // malloc exactly enough memory for the new string.
  size_t diff = str_count(str, len_i, omit, len_o);
  if (diff > len_i) {
    new = safemalloc( sizeof(char) * len_i , __LINE__);
  } else {
    new = safemalloc( ( sizeof(char) * len_i ) - diff , __LINE__);
  }

  for (size_t p = 0, j = 0; p < len_i; p++) {
    if ( !str_contains(omit, len_o, str[p]) ) {
      new[j] = str[p];
      j++;
    }
  }

  return new;
}

// str_split -- split str on delim, returning a pointer to a 2D-array of char* results
// && writing the length to *out
// if the delimiter is not found in the string, then the string is made the first elt of the 2D-array
// && out will be 1
// the result of this function must be freed!
char** str_split (const char* str, const size_t len, const char delim, size_t* out) {

  // off-by-one... maybe I'll figure out why this is needed
  size_t l = len + 1;

  size_t len_new, delim_count;

  char *token,
       *str_copy     = strndup(str, MAX_STR_LEN),
       *str_copy2    = strndup(str, MAX_STR_LEN),
       *delim_as_str = safemalloc(sizeof(char), __LINE__),
       **new;

  sprintf(delim_as_str, "%c", delim);

  // if the delimiter was found in the string, split & marshal the toks
  // READ: not dividing by zero is A Good Thing™
  if ((delim_count = str_count(str, l, delim_as_str, 1))) {
    len_new = ( sizeof(char) * l ) / delim_count;
    new = safemalloc(len_new, __LINE__);

    size_t i = 0;
    for (
      ;
      (i < len_new) && (token = strsep(&str_copy, delim_as_str));
      i++
    ) {
      new[i] = token;
    }

    *out = i;
  } else {
    // no delimiter in string: just set the first elt to the string
    // && DON'T DIVIDE BY ZERO!
    len_new = 1;
    new     = safemalloc(len_new, __LINE__);
    new[0]  = str_copy2;
    *out    = len_new;
  }

  assert(out != NULL);

  /*
    technically, str_copy is now NULL as strsep(3) modified it (see man strsep)
    but we can free it anyways (not safefree) in case it's not
    this is the one time freeing a null pointer does not indicate
    a logic or flow error -- freeing null pointers is a no-op

    NOT QUITE: free() can *only* be used on pointers that still point where malloc()
    put them -- if the pointer has been modified to point somewhere else, like this
    one, then a crash will occur */
  //free(str_copy);
  delim_as_str = safefree(delim_as_str, __LINE__);

  return new;
}

// s2numlist -- split a string on delimiters after removing any of a list of chars, returning a pointer to the result
// and writing the length to *out_len
// the result of this function must be freed!
uint64_t* s2numlist (const char* str, const size_t len, size_t* out_len, const char* remove_me, const char split_at_me) {

  size_t list_len;

  char*      as_str = str_rm(str, len, remove_me, 1);

  char**   list_str = str_split(as_str, len, split_at_me, &list_len);

  uint64_t* as_nums = safemalloc(sizeof(uint64_t) * list_len, __LINE__);


  for (size_t i = 0; i < list_len; i++) {
    as_nums[i] = (uint64_t) strtoull(list_str[i], NULL, DEC_BASE);
  }

  *out_len = list_len;

  as_str   = safefree(as_str, __LINE__);
  list_str = safefree(list_str, __LINE__);

  return as_nums;
}

// rand_range -- return a random number < max
// if you do not have bsd's stdlib.h, uncomment the other implementation
uint64_t rand_range (uint64_t max) {

  // http://stackoverflow.com/a/6852396/4532996
  uint64_t
    // max <= RAND_MAX < ULONG_MAX, so this is okay.
    num_bins = max + 1ULL,
    num_rand = (uint64_t) RAND_MAX + 1ULL,
    bin_size = num_rand / num_bins,
    defect   = num_rand % num_bins;

  // This is carefully written not to overflow
  uint64_t x = 0;
  do {
    x = (uint64_t) rand();
  } while (num_rand - defect <= (uint64_t) x);

  // Truncated division is intentional
  return x / bin_size;
}

void insult_user (void) {
  printf("%s\n", insults[rand_range(NUM_INSULTS)]);
}

/*
  strnlen, though specified by POSIX.1-2008 would not appear to be
  defined in string.h except with GNU extensions turned on (i.e.,
  not -std=c11). I love Richard Stallman but I'd like my code to work
  on other platforms too thus this seemingly superfluous definition of
  strnlen.

  UPDATE: -std=gnu11 and -std=gnu99 allow GCC to compile C11 or C99,
  respectively, while enabling GNU safety extensions like strn*. GCC is
  available for modern platforms (and even Windows, though I would not
  call Windows "modern"), which does not come with a C compiler
  anyways, so it should be perfectly fine

size_t strnlen (const char *str, size_t max) {
  const char *end = memchr (str, 0, max);
  if (end) {
    return (size_t) (end - str);
  }
  return max;
}
*/

// problem_intro -- print a problem's description
void problem_intro (const uint8_t problem_number) {

  const char* desc_tabl[NUM_FUNCS] = {
    "counts number of numbers less than N divisible by X",
    "sums numbers from the input",
    "compute factorial of input" \
    "\n max. input is 20 -- 'integral' doubles higher than 20! will be very imprecise",
    "guess my number -- it's you against the hive mind.",
    "maximum of inputs",
  };

  printf("\nProblem #%" PRIu8 ": %s\n", problem_number, desc_tabl[problem_number - 1]);
}

/*



  BEGIN IMPLEMENTATIONS



*/

//1 - Write a program to count how many numbers between 1 and 100 are divisible by 3
//    with no remainder.Display the count on the console.
uint64_t count_div (const uint64_t range, const uint64_t div_by) {

  uint64_t s = 0;

  if (! (range && div_by) ) {
    printf("Floating point exception (core dumped)\n\n");
    insult_user();
    printf("\n");
    return 0;
  }

  for (uint64_t i = 1; i < range; i++) {
    if (!(i % div_by)) {
      printf("%" PRIu64 " %% %" PRIu64 " == 0\n", i, div_by);
      s++;
    }
  }

  return s;
}

void count_helper (void) {
  problem_intro(1);

  uint64_t range, div_by, div_input, s = 0;

  do {
    printf("enter a number! "); fflush(stdout);

    if (!get_uint64(&range)) { break; }

    printf("enter another! ");  fflush(stdout);

    if (!get_uint64(&div_by)) { break; }

    s += (div_input = count_div(range, div_by));

    printf("numbers less than %" PRIu64 " that are divisible by %" PRIu64 ": ", range, div_by);

    if (range && div_input) {
      printf("%" PRIu64 "\n", div_input);
    } else {
      printf("a slap in the face for dividing by zero\n");
    }

  } while(true);

  printf("sum of results: %" PRIu64 "\n", s);
}

//2 - Write a program and continuously ask the user to enter a number or "ok" to
//    exit. Calculate the sum of all the previously entered numbers and display
//    it on the console.
uint64_t sum (const uint64_t xs[static 1], const size_t len) {
  uint64_t s = 0;
  for (uint64_t i = 0; i < len; i++) {
    s += xs[i];
  }
  return s;
}

void sum_helper (void) {
  problem_intro(2);

  printf("\nHTTP/1.1 301 OK\n"
    "Status code 301\n" \
    "Message: Moved Permanently\n" \
    "Code explanation: Object moved permanently\n\n");

  max_helper();

}

//3 - Write a program and ask the user to enter a number. Compute the factorial of
//    the number and print it on the console. For example, if the user enters 5,
//    the program should calculate 5 x 4 x 3 x 2 x 1 and display it as 5! = 120.
uint64_t factorial (const uint64_t n) {
  if (n < 2) { return 1; }
  return n * factorial(n - 1);
}

void fact_helper (void) {
  problem_intro(3);

  bool valid;
  uint64_t num;

  printf("enter number to factorial or blank line / EOF to end\n");

  while ((valid = get_uint64(&num))) {
    // avoid overflow
    valid &= (num <= 20ULL);

    if (valid) {
      printf("%" PRIu64 "! == %" PRIu64 "\n", num, factorial(num));
    } else if (num > 20ULL) {
      insult_user();
      printf("BOB says: That number is too large, enter another!\n");
    } else { break; }
  }

  printf("bye!\n");
}

//4 - Write a program that picks a random number between 1 and 10.Give the user 4
//    chances to guess the number.If the user guesses the number, display “You won";
//    otherwise, display “You lost". (To make sure the program is behaving correctly,
//    you can display the secret number on the console first.)
bool guess_game (const uint64_t upper, const uint64_t tries, uint64_t *outcome) {
  uint64_t  guess,
            choice = rand_range(upper);

  bool over;

  // off-by-one
  for (uint64_t i = 1; i <= tries; i++) {
    printf("(%" PRIu64 " / %" PRIu64 ") enter a guess! ", i, tries);
    fflush(stdout);

    if (!get_uint64(&guess)) { break; }

    if (guess == choice) {
      *outcome = guess;
      return true;
    }

    over = (i == tries);
    if (guess > upper) { printf("You fool! That number is far too large!\n"); }
    printf("\nBOB says: It seems that guess is wrong%s\n\n", over ? "; you lose!" : ", enter another!");
    if (over) { insult_user(); return false; }
  }
  return false;
}

void guess_helper (void) {
  problem_intro(4);
  uint64_t  outcome,
            upper, tries;

  printf("enter the upper limit: ");
  fflush(stdout);
  if (!(get_uint64(&upper))) {
    return;
  }
  printf("number of tries: ");
  fflush(stdout);
  if (!(get_uint64(&tries))) {
    return;
  }

  if (guess_game(upper, tries, &outcome)) {
    printf("You guessed right! %" PRIu64 "\n", outcome);
  }
}

//5 - Write a program and ask the user to enter a series of numbers separated by
//    comma.Find the maximum of the numbers and display it on the console. For
//    example, if the user enters “5, 3, 8, 1, 4", the program should display 8.
uint64_t max (const uint64_t xs[static 1], const size_t len) {
  uint64_t high = 0;
  for (uint64_t i = 0; i < len; i++) {
    if (xs[i] > high) { high = xs[i]; }
  }
  return high;
}

void max_helper (void) {
  problem_intro(5);

  size_t out_len;

  char buf[MAX_STR_LEN],
      *input;

  printf("enter a comma separated list of numbers (EOF to exit): ");
  fflush(stdout);

  input = chomp(fgets(buf, MAX_STR_LEN, stdin));

  if (isEOL(input)) {
    printf("found EOF before input, finishing\n");
    return;
  }

  uint64_t* nums = s2numlist(input, safestrnlen(input), &out_len, " ", ',');

  printf("max of inputs: %" PRIu64 "\n", max(nums, out_len));
  printf("sum of inputs: %" PRIu64 "", sum(nums, out_len));

  nums = safefree(nums, __LINE__);

}
