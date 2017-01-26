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

#include "/home/cat/projects/c/misc/iter/insults.h"

#define DEC_BASE    10
#define DEC_DIGITS  "0123456789"
#define INT_DIGITS  10
#define ULL_DIGITS  20
#define NUM_PROBS   5
#define NUM_INSULTS ( ( sizeof(insults) / sizeof(insults[0]) ) - 1 )
#define MAX_STR_LEN 1024

// utils
char* str_reverse (const char* const str);
char*   str_chomp (const char* str);
char*      readln (const size_t      len);
char*      str_rm (
  const char*   str,
  const size_t  len_str,
  const char*   omit,
  const size_t  len_omit,
        size_t* out_len
);
char**  str_split (
  const char*   str,
  const size_t  len,
  const char    delim,
        size_t* out_len
);

bool     isEOL (const char* str);
bool  getint64 (int64_t*  restrict dest);
bool getuint64 (uint64_t* restrict dest);

uint64_t        rand_range (const uint64_t max);
uint64_t* str_to_ull_array (
  const char*   str,
  const size_t  len,
  const char*   remove_at,
  const char    split_at,
        size_t* out_len
);

size_t   str_count (
  const char*   haystack,
  const size_t  len_haystack,
  const char*   needle,
  const size_t  len_needle
);
size_t safestrnlen (const char* str);
size_t   safe_usub (size_t x, size_t y);

void    insult_user (void);
void  problem_intro (const uint8_t problem_number);
void      _safefree (void*  ptr, uint64_t lineno);
void*   _safemalloc (size_t len, uint64_t lineno);

#define safefree(x) _safefree(x, __LINE__)
#define safemalloc(x) _safemalloc(x, __LINE__)

// problem 1
uint64_t* count_div (const uint64_t range, const uint64_t div_by, uint64_t* out_len);
void     count_helper (void);
// problem 2
uint64_t          sum (const uint64_t xs[static 1], const size_t len);
void       sum_helper (void);
// problem 3
double      factorial (const double n);
void      fact_helper (void);
// problem 4
bool       guess_game (const uint64_t upper, const uint64_t tries, uint64_t* outcome);
void     guess_helper (void);
// problem 5
uint64_t          max (const uint64_t xs[static 1], const size_t len);
void       max_helper (void);

void (* problem_funs[NUM_PROBS]) (void) = {
  count_helper,
  sum_helper,
  fact_helper,
  guess_helper,
  max_helper,
};

/*
  "If ptr is a null pointer, no action shall occur." -- POSIX.1-2008
  But if I'm free()-ing a pointer I already free()-d, then something is wrong.
*/
// _safefree -- free a pointer to allocated memory or die freeing NULL
void _safefree (void* ptr, uint64_t lineno) {
  if (!ptr) {
    printf("You fool! You have tried to free() a null pointer! (line %" PRIu64 ")\n", lineno);
    assert(ptr);
  } else {
    free(ptr);
  }
}

// _safemalloc -- allocate memory or die
void* _safemalloc (size_t len, uint64_t lineno) {
  void* mem = malloc(len);
  if (!mem) {
    printf("Couldn't malloc() %zu bytes (perhaps you have run out of memory?) (line %" PRIu64 ")\n", len, lineno);
    assert(mem);
  }
  return mem;
}

// problem_intro -- describe a problem to the user
void problem_intro (const uint8_t problem_number) {
  const char* desc_tabl[NUM_PROBS] = {
    "count numbers less than N divisible by X",
    "summation of numbers",
    "factorial of input",
    "guess my number -- it's you against the hive mind.",
    "maximum and summation of comma-separated inputs",
  };

  printf("\nProblem #%" PRIu8 ": %s\n", problem_number, desc_tabl[problem_number - 1]);

}

// insult_user -- insult the user
void insult_user (void) {
  printf("%s\n", insults[rand_range(NUM_INSULTS)]);
}

/*

UTILITIES

*/

// safe_usub -- perform safe unsigned subtraction
size_t safe_usub (size_t x, size_t y) {
  return x > y ? x - y : y - x ;
}

char* str_reverse (const char* const str) {
  if (!str) { return NULL; }

  size_t len = safestrnlen(str);
  char*  new = safemalloc( sizeof(char) * len );

  size_t i;
  for (i = 0; i < len; i++) {
    new[i] = str[ safe_usub(i + 1, len) ];
  }

  new[i] = 0;

  return new;
}

// chomp -- cuts the last char (a newline?) from a string
char* str_chomp (const char* str) {
  char* new = strndup(str, MAX_STR_LEN);
  new[ safestrnlen(new) - 1 ] = 0;
  return new;
}

// readln -- returns a line of chomped STDIN, or NULL on blank line / EOF
char* readln (const size_t len) {
  char* buf = safemalloc( sizeof(char) * len );
  fgets(buf, MAX_STR_LEN, stdin);
  buf = str_chomp(buf);
  if (!isEOL(buf)) {
    return buf;
  }
  return NULL;
}

/* str_split -- split str of length len on delim, returning the new 2d array
   and writing its length to out_len
*/
char** str_split (
  const char*   str,
  const size_t  len,
  const char    delim,
        size_t* out_len
) {
  char delim_str[2],
      *str_copy = strndup(str, MAX_STR_LEN);

  sprintf(delim_str, "%c%c", delim, 0);

  size_t num_delim = str_count(str, len, delim_str, 1);

  char** new;

  if (num_delim < 2) {
    // no separator found
    new      = safemalloc( sizeof(char*) * 2 );
    new[0]   = str_copy;
    new[1]   = 0;
    *out_len = 1;

  } else {
    // separator found
    new = safemalloc( ( sizeof(char*) * num_delim ) + 1 );

    size_t i;
    char* token;

    for (i = 0; (token = strsep(&str_copy, delim_str)) != NULL; i++) {
      new[i] = token;
    }

    new[i + 1] = 0;
    *out_len   = i;
  }

  assert(out_len != NULL);
  return new;
}

/*
  str_rm -- remove all instances of the contents of *omit from str and return new memory
  result must be freed!
*/
char*     str_rm (
  const char*   str,
  const size_t  len_str,
  const char*   omit,
  const size_t  len_omit,
        size_t* out_len
) {
  // malloc one more than exactly enough for the new string
  const size_t len_new = (
    (
      ( sizeof(char) * len_str )
      -
      str_count(str, len_str, omit, len_omit)
    )
  );
  char* new = safemalloc( len_new + 1 );

  char c[2];

  size_t i, j;
  for (i = 0, j = 0; j < len_new; i++) {
    sprintf(c, "%c%c", str[i], 0);
    if (!str_count(omit, len_omit, c, 1)) {
      new[j] = str[i];
      j++;
    }
  }
  new[j] = 0;
  *out_len = len_new;
  assert(out_len != NULL);
  return new;
}

// isEOL -- string is eol?
bool isEOL (const char* str) {
  return !str
    || !safestrnlen(str)
    || str[0] == '\n';
}

bool getint64 (int64_t* restrict dest) {
  char* in = readln(ULL_DIGITS);
  if (!in) { return false; }
  *dest    = strtoll(in, NULL, DEC_BASE);
  assert(dest != NULL);
  return true;
}

bool getuint64 (uint64_t* restrict dest) {
  char* in = readln(ULL_DIGITS);
  if (!in) { return false; }
  *dest    = strtoull(in, NULL, DEC_BASE);
  assert(dest != NULL);
  return true;
}

// rand_range -- return a random number < max
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

// str_to_ull_array -- convert string of numbers to array of uint64_t
uint64_t* str_to_ull_array (
  const char*   str,
  const size_t  len,
  const char*   remove_at,
  const char    split_at,
        size_t* out_len
) {
  size_t out;
  char*     after_rm = str_rm(str, len, remove_at, safestrnlen(remove_at), &out);

  char** after_split = str_split(after_rm, out, split_at, &out);

  uint64_t*      new = safemalloc( sizeof(uint64_t) * out );

  for (size_t i = 0; i < out; i++) {
    new[i] = strtoull(after_split[i], NULL, DEC_BASE);
  }

  safefree(after_rm);
  safefree(after_split);

  *out_len = out;
  assert(out_len != NULL);

  return new;
}

// str_count -- count occurences of needles in haystack
size_t str_count (
  const char*   haystack,
  const size_t  len_haystack,
  const char*   needles,
  const size_t  len_needles
) {
  size_t s = 0;
  char c;

  for (size_t i = 0; i < len_haystack; i++) {
    c = haystack[i];
    for (size_t h = 0; h < len_needles; h++) {
      if (c == needles[h]) {
         s++;
       }
    }
  }
  return s;
}

// safestrnlen -- find the length of a string, defaulting to MAX_STR_LEN, without segfaulting
size_t safestrnlen (const char* str) {
  // it seems gnu strnlen segfaults on null pointer (aka empty string), so let's fix that
  if (!str) { return 0; }
  return strnlen(str, MAX_STR_LEN);
}

/*

BEGIN IMPLEMENTATIONS

*/

//1 - Write a program to count how many numbers between 1 and 100 are divisible by 3
//    with no remainder.Display the count on the console.
uint64_t* count_div (const uint64_t range, const uint64_t div_by, uint64_t* out_len) {

  if ((!range) || (!div_by)) {
    insult_user();
    return NULL;
  }

  uint64_t   x = 0;
  uint64_t* xs = safemalloc( sizeof(uint64_t) * range );

  for (size_t i = 1; i < range; i++) {
    if (!(i % div_by)) {
      xs[x] = i;
      x++;
    }
  }

  *out_len = x;
  return xs;
}

void count_helper (void) {
  problem_intro(1);
  bool valid;

  uint64_t range       = 0,
           div_by      = 0,
           *divlist    = NULL,
           divlist_len = 0;

  do {
    printf("enter the range!   ");
    fflush(stdout);

    valid  = getuint64(&range);

    printf("enter the divisor! ");
    fflush(stdout);

    valid &= getuint64(&div_by);

    if (!(divlist = count_div(range, div_by, &divlist_len)) || (!valid)) {
      printf("\nbye!\n");
      break;
    }

    for (uint64_t i = 0; i < divlist_len; i++) {
      printf("%" PRIu64 " %% %" PRIu64 " == 0 \n", divlist[i], div_by);
    }

    printf("numbers in range %" PRIu64 " divisible by %" PRIu64 ": ", range, div_by);
    fflush(stdout);

    if (!div_by) {
      printf("a slap in the face for dividing by zero\n");
    } else {
      printf("%" PRIu64 "\n", divlist_len);
    }

  } while(valid);
}

//2 - Write a program and continuously ask the user to enter a number or "ok" to exit.
//    Calculate the sum of all the previously entered numbers and display it on the console.
uint64_t sum (const uint64_t xs[static 1], const size_t len) {
  uint64_t s = 0;

  for (size_t i = 0; i < len; i++) {
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
double factorial (const double n) {
  return n < 2 ? 1 : n * factorial( (double) n - 1 );
}

void fact_helper (void) {
  problem_intro(3);

  bool valid;
  uint64_t in;

  do {
    printf("enter a number! ");
    fflush(stdout);

    valid = getuint64(&in);

    if (!valid) {
      insult_user();
      printf("bye!\n");
      break;
    }

    printf("%" PRIu64 "! = ", in);

    for (uint64_t i = 1; i < (in + 1); i++) {

      printf("%" PRIu64 "", i);

      if (!(in == i)) {
        printf(" x ");
      } else {
        printf(" = %.f\n" , factorial( (double) in ));
      }
    }

  } while(true);

}

//4 - Write a program that picks a random number between 1 and 10. Give the user 4
//    chances to guess the number. If the user guesses the number, display “You won";
//    otherwise, display “You lost".
bool guess_game (const uint64_t upper, const uint64_t tries, uint64_t* outcome) {
  uint64_t  guess,
            choice = rand_range(upper);

  bool over;

  // off-by-one
  for (uint64_t i = 1; i <= tries; i++) {
    printf("(%" PRIu64 " / %" PRIu64 ") enter a guess! ", i, tries);
    fflush(stdout);

    if (!getuint64(&guess)) { break; }

    if (guess == choice) {
      *outcome = guess;
      return true;
    }

    over = (i == tries);
    printf("You fool! That guess is %s!\n", (guess > upper) ? "not even close" : "wrong");
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
  if (!(getuint64(&upper))) {
    return;
  }
  printf("number of tries: ");
  fflush(stdout);
  if (!(getuint64(&tries))) {
    return;
  }

  if (guess_game(upper, tries, &outcome)) {
    printf("You guessed right! %" PRIu64 "\n", outcome);
  }

}

//5 - Write a program and ask the user to enter a series of numbers separated by
//    comma. Find the maximum of the numbers and display it on the console. For
//    example, if the user enters “5, 3, 8, 1, 4", the program should display 8.
uint64_t max (const uint64_t xs[static 1], const size_t len) {
  uint64_t h = 0;
  for (size_t i = 0; i < len; i++) {
    if (xs[i] > h) { h = xs[i]; }
  }
  return h;
}

void       max_helper (void) {
  problem_intro(5);

  char* buf;
  size_t out;

  do {
    printf("enter comma-separated numbers! ");
    fflush(stdout);

    buf = readln(MAX_STR_LEN);

    if (isEOL(buf)) {
      insult_user();
      printf("bye!\n");
      break;
    }
    
    uint64_t* nums = str_to_ull_array(buf, safestrnlen(buf), " ", ',', &out);

    printf("max of inputs: %" PRIu64 "\n", max(nums, out));
    printf("sum of inputs: %" PRIu64 "\n", sum(nums, out));
    safefree(nums);

  } while(true);

}
