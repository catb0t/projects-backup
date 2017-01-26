#include <stdio.h>
#include <time.h>
#include <errno.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#define dabs(x)           ((x < 0) ? -x : x)
#define alloc(type, size) (type *) malloc(sizeof (type) * (size))
#define is_even(n)        ((n % 2) ? true : false)
#define to_even(n)        (is_even(n) ? n + 1 : n)

typedef enum {
  c_white = 1 << 1,
  c_black = 1 << 2,
  c_antup = 1 << 3,
  c_antdn = 1 << 4,
  c_antlf = 1 << 5,
  c_antrt = 1 << 6,
} cellstate_t;

typedef /* stack'd */ struct {
  size_t x, y;
} point_t;

typedef /* heap'd */ struct {
  cellstate_t** data;

  size_t        dim, langton_iter, uid;

} matrix_t;

static const char states[] = {
  [c_white]           = '.',
  [c_black]           = '#',

  [c_antdn | c_white] = 'v',
  [c_antdn | c_black] = 'V',

  [c_antup | c_white] = '^',
  [c_antup | c_black] = 'A',

  [c_antlf | c_white] = '<',
  [c_antlf | c_black] = '(',

  [c_antrt | c_white] = '>',
  [c_antrt | c_black] = ')',
};

matrix_t* matrix_new (const size_t);

cellstate_t* matrix_getpos (const matrix_t* const);

point_t  point_new (const size_t, const size_t);

bool   cell_isant (const cellstate_t);
bool cell_iswhite (const cellstate_t);
bool cell_isblack (const cellstate_t);

char** matrix_to_s (const matrix_t* const m);

void              show_legend (void);
void               matrix_see (const matrix_t* const);
void          matrix_destruct (matrix_t* const);
void matrix_next_langton_iter (matrix_t* const);


int main(void) {

  //show_legend();
  printf("\033[2J");

  matrix_t* m = matrix_new(17);

  for (size_t i = 0; i < 18; i++) {
    printf("\033[1;1H");
    matrix_see(m);
    matrix_next_langton_iter(m);
    int a = system("sleep 1");
    (void) a;
  }


  matrix_destruct(m);

  return EXIT_SUCCESS;
}

static size_t size_t_sub (const size_t in, const signed long long op) {
  if ( ((unsigned) dabs(op)) > in ) {
    return 0;
  }
  /* TODO: check overflow of size_t... */
  return (in - ( (size_t) op));
}

bool cell_isant (const cellstate_t c) {
  return !! (c & (c_antlf | c_antdn | c_antrt | c_antup));
}
bool cell_iswhite (const cellstate_t c) {
  return !! (c & c_white);
}
bool cell_isblack (const cellstate_t c) {
  return !! (c & c_black);
}

point_t point_new (const size_t x, const size_t y) {
  return (point_t) {x, y};
}

void show_legend (void) {
  printf(
    "[c_white]           = '.' = %d,\n"
    "[c_black]           = '*' = %d,\n"
    "[c_antdn | c_white] = 'v' = %d,\n"
    "[c_antdn | c_black] = 'V' = %d,\n"
    "[c_antup | c_white] = '^' = %d,\n"
    "[c_antup | c_black] = 'A' = %d,\n"
    "[c_antlf | c_white] = '<' = %d,\n"
    "[c_antlf | c_black] = '(' = %d,\n"
    "[c_antrt | c_white] = '>' = %d,\n"
    "[c_antrt | c_black] = ')' = %d,\n",
    c_white,
    c_black,
    c_antdn | c_white,
    c_antdn | c_black,
    c_antup | c_white,
    c_antup | c_black,
    c_antlf | c_white,
    c_antlf | c_black,
    c_antrt | c_white,
    c_antrt | c_black
  );
}


matrix_t* matrix_new (const size_t in_size) {

  static size_t uid = 0;

  const size_t sz = to_even(in_size);

  const matrix_t stk = {
      .dim          = sz,
      .uid          = ++uid,
      .langton_iter = 1,

      .data    = alloc(cellstate_t *, sz),
    };

  for (size_t i = 0; i < sz; i++) {
    stk.data [i] = alloc(cellstate_t, sz);

    for (size_t j = 0; j < sz; j++) {
      stk.data [i][j] = c_white;
    }
  }

  stk.data [sz / 2][sz / 2] |= c_antlf;

  return memcpy( alloc(matrix_t, 1), &stk, sizeof stk);
}

void matrix_destruct (matrix_t* const m) {
  const size_t dim = m->dim;

  for (size_t i = 0; i < dim; i++) {
    free(m->data[i]);
  }

  free(m->data);
  free(m);
}

char** matrix_to_s (const matrix_t* const m) {
  const size_t dim = m->dim;

  char** lines = alloc(char *, dim);

  for (size_t i = 0; i < dim; i++) {
    lines[i] = alloc(char, dim);
    for (size_t j = 0; j < dim; j++) {
      lines [i][j] = states[ (m->data) [i][j] ];
    }
  }

  return lines;
}

void matrix_see (const matrix_t* const m) {
  const size_t dim = m->dim;

  printf("matrix #%zu %zux%zu itern #%zu white=%d isant=%d pos=%zu,%zu {\n",
    m->uid,
    m->dim,
    m->dim,
    m->langton_iter,
    cell_iswhite( *matrix_getpos(m)),
    cell_isant( *matrix_getpos(m)),
    m->ant_pos.x,
    m->ant_pos.y
  );

  char** lines = matrix_to_s(m);

  for (size_t i = 0; i < dim; i++) {
    printf("\t");
    for (size_t j = 0; j < dim; j++) {
      printf("%c ", lines[i][j]);
    }
    free(lines[i]);
    printf(" %zu\n", i + 1);
  }
  free(lines);

  printf("} /* matrix #%zu iteration #%zu */\n", m->uid, m->langton_iter);

}

cellstate_t* matrix_getpos (const matrix_t* const m) {
  return & ((m->data) [m->ant_pos.x][m->ant_pos.y]);
}

static point_t matrix_nav (const point_t p, const cellstate_t dir) {

  /*

  1 2 3 = y
  . . . 1
  . * . 2
  . . . 3
        ^
        x

  */

  size_t
    new_x = size_t_sub(
      p.x,
      (dir & c_antup
        ? -1 :
        (dir & c_antdn ? 1 : 0))),

    new_y = size_t_sub(
      p.y,
      (dir & c_antrt
        ? -1 :
        (dir & c_antlf ? 1 : 0)));

  return (point_t) { .x = new_x, .y = new_y };

}

static cellstate_t cell_rotate (const cellstate_t s, const bool dir) {
  /* false for left and true for right

      up
    lf  rt
      dn
  */

  switch (s) {
    case c_antup: return dir ? c_antrt : c_antlf;
    case c_antdn: return dir ? c_antlf : c_antrt;
    case c_antlf: return dir ? c_antup : c_antdn;
    case c_antrt: return dir ? c_antdn : c_antup;

    default: errno = EINVAL; return (cellstate_t) 0;
  }

  return s;
}

void matrix_next_langton_iter (matrix_t* const m) {

  cellstate_t* old = matrix_getpos(m);

  /* at a white square turn 90* right and 90* left at a black one */
  m->facing = cell_rotate(
    m->facing,
    cell_isblack( *matrix_getpos(m) )
  );

  // 0 is not a real cellstate_t enumeration value
  if (EINVAL == errno && !m->facing) {
    errno = 0;
    return;
  }

  m->ant_pos = matrix_nav(m->ant_pos, m->facing);

  *matrix_getpos(m) = m->facing | c_black;

  *old = c_black;

  ++m->langton_iter;
}
