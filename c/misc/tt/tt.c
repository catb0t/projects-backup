// Requires GNU C !!

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#define auto __auto_type

#define define_evenly_divides(type) \
  static inline pure bool type ## evenly_divides (const type a, const type b) \
  { return ! (a % b); } \
  int hidden1 ## type /* for the trailing semicolon */

define_evenly_divides(size_t);

typedef long double ldbl_t;

ldbl_t  triangle_ratio (const ldbl_t a, const ldbl_t b, const ldbl_t c);
bool is_valid_triangle (const ldbl_t a, const ldbl_t b, const ldbl_t c);

/* 
  smpr is the Semiperimeter of the triangle (half the perimeter)
  the return value is called the triangle ratio -- it is 1 for equilateral, less 
  than 1 for invalid triangles, and greater than 1 for all other valid triangles
*/
ldbl_t triangle_ratio (const ldbl_t a, const ldbl_t b, const ldbl_t c) {
  auto smpr = (a + b + c) / 2.f; // assuming x + y doesn't overflow 80-bit int (56 bit base)

  return (a * b * c) / (8.f * (smpr - a) * (smpr - b) * (smpr - c) );
}

// bool is_valid_triangle (const ldbl_t a, const ldbl_t b, const ldbl_t c) { return triangle_ratio(a, b, c) > 1; }

int main (void) {

  /* 
    I'm lazy. Don't ever. EVER. E V E R. use scanf. Okay???? it's awful for real use cases.
    Prefer fgets, or getchar in a loop, with strto*
  */
  long double a, b, c;

  puts("enter some numbers");

  // and above all, don't ignore its retval like i do
  scanf("%LG %LG %LG", &a, &b, &c);

  auto result = triangle_ratio(a, b, c);

  printf("ratio: %LG is %sa valid triangle\n", result, result > 1 ? "" : "not ");
}
