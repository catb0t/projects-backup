#include <stdlib.h>
#include <stdio.h>
#include <stdarg.h>
#include <errno.h>

typedef long double ldbl_t;

#define MATH_PI (ldbl_t)3.14159265358979323846264338327950288419716939937510582097494459230
#define red_error(format, ...) fprintf(stderr, "\x1b[31m" format"\x1b[0m", __VA_ARGS__)

void      helpme (void);
void conv_anyval (const ldbl_t v, ldbl_t* const deg, ldbl_t* const rad);

ldbl_t angleconv_compose (ldbl_t val, ldbl_t a, ldbl_t b);
ldbl_t       str_to_ldbl (const char* const argv);
ldbl_t      conv_deg2rad (const ldbl_t v);
ldbl_t      conv_rad2deg (const ldbl_t v);

int main (const int argc, const char* const * const argv) {

  switch (argc) {

    case 2: {
      ldbl_t deg, rad, val;
      val = str_to_ldbl(argv[1]);

      if (EINVAL == errno) { red_error("%s\n", "str_to_ldbl: 0x0: argument points here (unexpected NULL)"); }

      conv_anyval(val, &deg, &rad);
      printf("%LG =\n\t%LG degrees\n\t%LG radians\n", val, deg, rad);

      break;
    }

    case 3: {
      ldbl_t out_deg, out_rad,
             in_deg = str_to_ldbl(argv[1]),
             in_rad = str_to_ldbl(argv[2]);

      if (EINVAL == errno) { red_error("%s\n", "str_to_ldbl: 0x0: argument points here (unexpected NULL)"); }

      out_deg = conv_rad2deg(in_rad),
      out_rad = conv_deg2rad(in_deg);

      printf(
        "%LG degrees = %LG radians\n"
        "%LG radians = %LG degrees\n",
        in_deg, out_rad,
        in_rad, out_deg
      );

      break;
    }

    default: {
        fprintf(stderr, "usage: \n\tconv_degrad VAL\n\tconv_degrad DEGREES RADIANS");
        return EXIT_FAILURE;
        break;
    }

  }

  return EXIT_SUCCESS;
}

ldbl_t str_to_ldbl (const char* const s) {

  if ( NULL == s ) {
   errno = EINVAL;
   return 0;
  }

  ldbl_t res = strtold(s, NULL);

  if (ERANGE == errno) {
    red_error("str_to_ldbl: %s: %s\n", s, "argument out of range");
    perror("str_to_ldbl: ");
    return 0;
  }

  return res;
}

void conv_anyval (const ldbl_t v, ldbl_t* const deg, ldbl_t* const rad) {
  *deg = conv_deg2rad(v);
  *rad = conv_rad2deg(v);
}

ldbl_t angleconv_compose (ldbl_t val, ldbl_t a, ldbl_t b) {
  return (val * a) / b;
}

ldbl_t conv_deg2rad (const ldbl_t v) {
  return angleconv_compose(v, 180, MATH_PI);
}

ldbl_t conv_rad2deg (const ldbl_t v) {
  return angleconv_compose(v, MATH_PI, 180);
}
