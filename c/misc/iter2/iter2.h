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

#include "/home/cat/projects/c/misc/iter2/insults.h"

#define DEC_BASE    10
#define DEC_DIGITS  "0123456789"
#define INT_DIGITS  10
#define ULL_DIGITS  20
#define NUM_PROBS   5
#define NUM_INSULTS ( ( sizeof(insults) / sizeof(insults[0]) ) - 1 )
#define MAX_STR_LEN 1024
#define SHORT_INSTR 256

// utils
char* str_reverse (const char*  const str);
char*   str_chomp (const char*  const str);
char*      readln (const size_t len);
char*      str_rm (
  const char* const str,
  const size_t      len_str,
  const char* const omit,
  const size_t      len_omit,
        size_t*     out_len
);
char**  str_split (
  const char*   const str,
  const size_t  len,
  const char    delim,
        size_t* out_len
);

bool     isEOL (const char* const str);
bool  getint64 (int64_t*    restrict dest);
bool getuint64 (uint64_t*   restrict dest);

uint64_t        rand_range (const uint64_t max);
uint64_t* str_to_ull_array (
  const char* const str,
  const size_t      len,
  const char* const remove_at,
  const char        split_at,
        size_t*     out_len
);

size_t   str_count (
  const char* const haystack,
  const size_t      len_haystack,
  const char* const needle,
  const size_t      len_needle
);
size_t safestrnlen (const char* const str);
size_t   safe_usub (size_t x, size_t y);

void    insult_user (void);
void  problem_intro (const uint8_t problem_number);
void      _safefree (void* ptr,  uint64_t lineno);
void*   _safemalloc (size_t len, uint64_t lineno);

#define safefree(x)   _safefree(x, __LINE__)
#define safemalloc(x) _safemalloc(x, __LINE__)


// IMPLEMENTATIONS

// problem 1
char*    likes_msg     (char** names, const size_t len);
void     facebook_repl (void);

// problem 2
void      reverse_repl (void);

// problem 3
size_t     count_ocurs (const uint64_t xs[static 1], const size_t len, const uint64_t needle);
bool            nodups (const uint64_t xs[static 1], const size_t len);
int                cmp (const void* p1, const void* p2);
void     sortuniq_repl (void);

// problem 4
uint64_t*   removedups (const uint64_t xs[static 1], const size_t len, size_t* out_len);
void         uniq_repl (void);

// problem 5
uint64_t          max (const uint64_t xs[static 1], const size_t len);
uint64_t          min (const uint64_t xs[static 1], const size_t len);
void     minlist_repl (void);

void (* problem_funs[NUM_PROBS]) (void) = {
  facebook_repl,
  reverse_repl,
  sortuniq_repl,
  uniq_repl,
  minlist_repl,
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
    "facebook post like-count formatting",
    "reverse stdin",
    "sort unique input numbers",
    "print unique numbers from the input",
    "minimum of 5 or more comma-separated numbers",
  };

  printf("\nProblem #%" PRIu8 ": %s\n", problem_number, desc_tabl[problem_number - 1]);

}

// insult_user -- insult the user
void insult_user (void) {
  printf("%s\n", insults[rand_range(NUM_INSULTS)]);
}


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
  const size_t len_new = ( ( ( sizeof(char) * len_str ) - str_count(str, len_str, omit, len_omit) ) );
  char*            new = safemalloc( len_new + 1 );

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

bool isEOL (const char* str) {
  return !str
    || !safestrnlen(str)
    || str[0] == '\n';
}

bool getint64 (int64_t* restrict dest) {
  char* in = readln(ULL_DIGITS);
  if (!in) {
    return false;
  }
  *dest    = strtoll(in, NULL, DEC_BASE);
  assert(dest != NULL);
  return true;
}

bool getuint64 (uint64_t* restrict dest) {
  char* in = readln(ULL_DIGITS);
  if (!in) {
    return false;
  }
  *dest = strtoull(in, NULL, DEC_BASE);
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

uint64_t* str_to_ull_array (
  const char*   str,
  const size_t  len,
  const char*   remove_at,
  const char    split_at,
        size_t* out_len
) {
  size_t out;
  char* after_rm     = str_rm(str, len, remove_at, safestrnlen(remove_at), &out);

  char** after_split = str_split(after_rm, out, split_at, &out);

  uint64_t* new = safemalloc( sizeof(uint64_t) * out );

  for (size_t i = 0; i < out; i++) {
    new[i] = strtoull(after_split[i], NULL, DEC_BASE);
  }

  safefree(after_rm);
  safefree(after_split);

  *out_len = out;
  assert(out_len != NULL);

  return new;
}

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
  1- When you post a message on Facebook, depending on the number of people who like your post, Facebook displays different information.
  If no one likes your post, it doesn't display anything.
  If only one person likes your post, it displays: [Friend's Name] likes your post.
  If two people like your post, it displays: [Friend 1] and [Friend 2] like your post.
  If more than two people like your post, it displays: [Friend 1], [Friend 2] and [Number of Other People] others like your post.
  Write a program and continuously ask the user to enter different names, until the user presses Enter (without supplying a name). Depending on the number of names provided, display   a message based on the above pattern.
*/

char* likes_msg (char** names, const size_t len) {
  char* msg = safemalloc( sizeof(char) * (2 * SHORT_INSTR) );
  switch (len) {
    case 0:
      msg = NULL;
      break;
    case 1:
      sprintf(msg, "%s likes your post.", names[0]);
      break;
    case 2:
      sprintf(msg, "%s and %s like your post.", names[0], names[1]);
      break;
    default:
      sprintf(msg, "%s, %s, and %zu other%s like your post.", names[0], names[1], len - 2, len - 2 > 1 ? "s" : "");
  }
  return msg;
}

void facebook_repl (void) {
  problem_intro(1);
  char* msg;

  do {
    char*    buf = safemalloc( sizeof(char)  * SHORT_INSTR );
    char** names = safemalloc( sizeof(char*) * SHORT_INSTR );

    printf("enter a name!  ");
    fflush(stdout);

    size_t i;
    for (i = 0; (buf = readln(SHORT_INSTR - 1)); i++) {
      names[i] = buf;
      printf("enter another! ");
      fflush(stdout);
    }

    if ((msg = likes_msg(names, i))) {
      printf("%s\n", msg);
      safefree(msg);
    }
  } while (msg);
}

//2- Write a program and ask the user to enter their name. Use an array to reverse the name and then store the result in a new string. Display the reversed name on the console.
void reverse_repl (void) {
  problem_intro(2);

  char* buf = safemalloc( sizeof(char) * SHORT_INSTR );
  char* out = safemalloc( sizeof(char) * SHORT_INSTR );
  printf("enter some words! ");
  fflush(stdout);

  while (buf && out) {
    buf = readln(SHORT_INSTR - 1);
    out = str_reverse(buf);

    printf("%s reversed is %s\n", buf, out);
    printf("enter more!       ");
    fflush(stdout);
  }
}

//3- Write a program and ask the user to enter 5 numbers. If a number has been previously entered, display an error message and ask the user to re-try. Once the user successfully enters 5 unique numbers, sort them and display the result on the console.
size_t count_ocurs (const uint64_t xs[static 1], const size_t len, const uint64_t needle) {
  size_t s = 0;

  for (size_t i = 0; i < len; i++) {
    if (xs[i] == needle) {
      s++;
    }
  }
  return s;
}

bool nodups (const uint64_t xs[static 1], const size_t len) {
  for (size_t i = 0; i < len; i++) {
    if (count_ocurs(xs, len, xs[i]) > 1) {
      return false;
    }
  }
  return true;
}

int cmp (const void *p, const void *q) {
  uint64_t x = (uint64_t) *(const int *) p;
  uint64_t y = (uint64_t) *(const int *) q;

  if (x < y) { return -1; }
  if (x > y) { return  1; }

  return 0;
}


void  sortuniq_repl (void) {
  problem_intro(3);

  uint64_t out,
          *nums = safemalloc( sizeof(uint64_t) * SHORT_INSTR );
  char*     buf = safemalloc( sizeof(char)     * SHORT_INSTR );

  printf("enter some comma-separated numbers! ");
  fflush(stdout);


  while (buf) {
    buf = readln(SHORT_INSTR - 1);
    nums = str_to_ull_array(buf, safestrnlen(buf), " ", ',', &out);

    qsort(nums, out, sizeof(uint64_t), cmp);

    if (nodups(nums, out)) {
      printf("sorted: ");
      for (size_t i = 0; i < out; i++) {
        printf("%" PRIu64 " ", nums[i]);
      }
      printf("\n");

    } else {
      insult_user();
      printf("You fool! I said *unique* numbers!\n");
    }
    printf("enter more!                         ");
    fflush(stdout);

    if (nums) {
      safefree(nums);
    }
    if (buf) {
      safefree(buf);
    }
  }
}

//4- Write a program and ask the user to continuously enter a number or type "Quit" to exit. The list of numbers may include duplicates. Display the unique numbers that the user has entered.
uint64_t* removedups (const uint64_t xs[static 1], const size_t len, size_t* out_len) {
  uint64_t* new = safemalloc( sizeof(uint64_t) * len);
  size_t i, j;

  for (i = 0, j = 0; i < len; i++) {
    if (!count_ocurs(new, j, xs[i])) {
      new[j] = xs[i];
      j++;
    }
  }

  *out_len = j;
  assert(out_len != NULL);
  return new;
}

void uniq_repl (void) {
  problem_intro(4);

  size_t out;

  uint64_t *uniq_nums,
           *in_nums;

  char* buf = safemalloc( sizeof(char) * SHORT_INSTR );

  printf("enter some comma-separated numbers! ");
  fflush(stdout);

  while (buf) {
    if (!(buf       = readln(SHORT_INSTR - 1)))
    { insult_user(); break; }

    if (!(in_nums   = str_to_ull_array(buf, safestrnlen(buf), " ", ',', &out)))
    { insult_user(); break; }

    if (!(uniq_nums = removedups(in_nums, out, &out)))
    { insult_user(); break; }

    printf("uniques: ");
    for (size_t i = 0; i < out; i++) {
      printf("%" PRIu64 " ", uniq_nums[i]);
    }

    printf("\nenter more! ");
    fflush(stdout);
  }
}


//5- Write a program and ask the user to supply a list of comma separated numbers (e.g 5, 1, 9, 2, 10). If the list is empty or includes less than 5 numbers, display "Invalid List" and ask the user to re-try; otherwise, display the 3 smallest numbers in the list.
uint64_t max (const uint64_t xs[static 1], const size_t len) {
  uint64_t h = 0;
  for (size_t i = 0; i < len; i++) {
    if (xs[i] > h) { h = xs[i]; }
  }
  return h;
}

uint64_t min (const uint64_t xs[static 1], const size_t len) {
  uint64_t s = max(xs, len);
  for (size_t i = 0; i < len; i++) {
    if (s > xs[i]) { s = xs[i]; }
  }
  return s;
}

void minlist_repl (void) {
  problem_intro(5);

  size_t out;

  uint64_t *in_nums;

  char* buf = safemalloc( sizeof(char) * SHORT_INSTR );

  printf("enter some comma-separated numbers! ");
  fflush(stdout);

  while (buf) {
    if (!(buf       = readln(SHORT_INSTR - 1)))
    { insult_user(); break; }

    if (!(in_nums   = str_to_ull_array(buf, safestrnlen(buf), " ", ',', &out)))
    { insult_user(); break; }

    if ((out < 5) || !out) {
      insult_user();
      printf("You fool! I said 5 or more numbers!\n");

    } else {
      printf("min: %" PRIu64 "\n", min(in_nums, out));
    }
    printf("enter more! ");
    fflush(stdout);
  }
}
