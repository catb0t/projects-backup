struct s_fxpt_t {
  uint32_t igrl;
  uint32_t frac;
  uint8_t frac_align;
};

typedef struct s_fxpt_t fixed_point_t;

fixed_point_t fxpt_new (const uint32_t integral, const uint32_t fractional, const uint8_t frac_align);
fixed_point_t fxpt_add (const fixed_point_t lhs, const fixed_point_t rhs);
fixed_point_t fxpt_sub (const fixed_point_t lhs, const fixed_point_t rhs);
fixed_point_t fxpt_mul (const fixed_point_t lhs, const fixed_point_t rhs);
fixed_point_t fxpt_div (const fixed_point_t lhs, const fixed_point_t rhs);
fixed_point_t fxpt_pow (const fixed_point_t lhs, const fixed_point_t rhs);

fixed_point_t fxpt_new (const uint32_t integral, const uint32_t fractional, const uint8_t frac_align) {
  fixed_point_t new;
  new.igrl       = integral;
  new.frac       = fractional;
  new.frac_align = frac_align;
  return new;
}

fixed_point_t fxpt_add (const fixed_point_t lhs, const fixed_point_t rhs) {
  fixed_point_t out;
  uint32_t n_ig, n_fc;
  n_ig = lhs.igrl + rhs.igrl;

  n_fc = (lhs.frac + rhs.igrl) % INT32_MAX;
  n_ig += (n_fc / 10);
  n_fc %= 10;

  out.igrl = n_ig;
  out.frac = n_fc;
  return out;
}

void write_fxpt (const char* const pre, fixed_point_t val, const char* const post) {
  (void)pre, (void)post, (void)val;
  //printf("%s%d.%d%s", pre, val.);
}


void run_main (void);

void run_main (void) {
  fixed_point_t a = fxpt_new(10, 5, 0);
  fixed_point_t b = fxpt_new(5, 5, 0);
  fixed_point_t c = fxpt_add(a, b);
  printf("%d.%d\n", c.igrl, c.frac);
}
