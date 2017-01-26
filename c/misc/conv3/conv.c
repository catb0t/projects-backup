#include <wchar.h>
#include <locale.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <assert.h>
#include <errno.h>
#include <time.h>

#define NLEN 2048
#define Out

#undef wcslen
#undef wcscmp
#undef wcsdup
#define wcscmp(s, c) wcsncmp((s), (c), NLEN)

#define wstrlen(s) wstrnlen((s), NLEN)
#define wstrdup(s) wstrndup((s), NLEN)

size_t udiff (const size_t x, const size_t y);

void wchomp (wchar_t** buf_ref);

wchar_t*   wstr_uniq (const wchar_t* const str);
wchar_t*    wstrndup (const wchar_t* const str, const size_t maxlen);
wchar_t*     wreadln (const size_t chars, FILE* const stream);
wchar_t** wstr_split (const wchar_t* const str, const wchar_t* const delims, Out size_t* const out_len);

bool op_comp_min_sizet (size_t a, size_t b);

ssize_t  wstr_find (const wchar_t* const str, wchar_t find);
size_t    wstrnlen (const wchar_t* const str, const size_t maxlen);
size_t* wstr_count (const wchar_t* const hsk, const wchar_t* const ndl);

#define alloc(typename, nmemb) ((typename *) malloc(nmemb * sizeof (typename)))
#define free_array(a, l) { assert(a); for (size_t i = 0; i < (l); i++) { free(a[i]); }; free(a); }

size_t udiff (const size_t x, const size_t y) {
  return x < y ? y - x : x - y;
}


wchar_t* wreadln (const size_t chars, FILE* const stream) {
  wchar_t *buf = alloc(wchar_t, chars + 1),
          *sts;

  fflush(stream);

  sts = fgetws(buf, (int) chars + 1, stream);

  fflush(stdin);

  if ( (! sts) || '\04' == buf[0] ) {
    free(buf);
    errno = EINVAL;
    return NULL;
  }

  wchomp(&buf);

  return buf;
}

void wchomp (wchar_t** buf_ref) {
  if (! buf_ref) { return; }

  (* buf_ref) [ wcscspn(*buf_ref, L"\n") ] = '\0';
}

ssize_t wstr_find (const wchar_t* const str, wchar_t find) {
  if (! str) { return -1; }
  const size_t len = wstrlen(str);

  for (size_t i = 0; i < len; i++) {
    if (str[i] == find) { return (ssize_t) i; }
  }

  return -1;
}

size_t* wstr_count (const wchar_t* const hsk, const wchar_t* const ndl) {
  if ( (! hsk) && (! ndl) ) { return NULL; }

  // all zeroes
  if ( (! hsk) && ndl) {
    return (size_t *) calloc(wstrlen(ndl), sizeof (size_t));
  }

  if (hsk && (! ndl) ) { return NULL; }

  size_t hlen = wstrlen(hsk), nlen = wstrlen(ndl);

  size_t* res = (size_t *) calloc(nlen, sizeof (size_t));

  for (size_t h = 0; h < hlen; h++) {
    wchar_t hc = hsk[h];
    for (size_t n = 0; n < nlen; n++) {
      wchar_t nc = ndl[n];
      if (hc == nc) { ++res[n]; }
    }
  }

  return res;
}

wchar_t* wstr_uniq (const wchar_t* const str) {
  if (! str) { return NULL; }

  const size_t len = wstrlen(str);

  if (! len) { return calloc(0, sizeof (wchar_t)); }

  wchar_t*   found = calloc(len, sizeof (wchar_t));

  for (size_t i = 0, j = 0; i < len; i++) {
    if (-1 == wstr_find(found, str[i])) {
      found[j] = str[i];
      j++;
    }
  }

  // save memory
  return realloc(found, sizeof (wchar_t) * wstrlen(found));
}

/* Duplicate S, returning an identical malloc'd string.  */
wchar_t* wstrndup (const wchar_t* const str, const size_t maxlen) {
  if (! str) { return NULL; }

  if (! maxlen) {
    return calloc(1, sizeof (wchar_t));
  }

  size_t   len = wstrnlen(str, maxlen);
  wchar_t* cpy = calloc(len + 1, sizeof (wchar_t));

  if (NULL == cpy) {
    return NULL;
  }

  return (wchar_t *) memcpy (cpy, str, sizeof (wchar_t) * len);
}

size_t wstrnlen (const wchar_t* const str, const size_t maxlen) {
  if ( (! str) || (! maxlen) || (! str[0])) { return 0; }

  size_t out = 0;

  const wchar_t* s = str;

  while (
    *(s++)
    && out < maxlen
  ) {
    out++;
  }

  return out;
}

#define define_array_minmax(T) \
  T* T ## _array_minmax (T* const ls, const size_t len, bool (* const cmp) (const T a, const T b)); \
  T* T ## _array_minmax (T* const ls, const size_t len, bool (* const cmp) (const T a, const T b)) { \
    if (! ls || ! len) { return NULL; } \
    T* outptr = ls;                     \
    for (size_t i = 0; i < len; i++) {  \
      outptr = cmp(ls[i], *outptr) ? ls + i : outptr; \
    } \
    return outptr; \
  } int __IDONTEXIST__ ## T

define_array_minmax(size_t);

bool op_comp_min_sizet (size_t a, size_t b) { return a < b; }

wchar_t** wstr_split (const wchar_t* const str, const wchar_t* const delims, Out size_t* const len) {

  if (! str || ! delims || ! len) {
    errno = EINVAL;
    return NULL;
  }

  wchar_t **out;

  size_t slen = wstrlen(str), dlen = wstrlen(delims);

  // empty input gives an array with one element, the empty string
  if (! slen) {
    out    = alloc(wchar_t *, 1);
    out[0] = alloc(wchar_t, 3);
    swprintf(out[0], 2, L"");
    *len = 1;
    return out;
  }

  // empty delimiter string gives array<wchar_t *> of each char of str
  if (! dlen) {
    out = alloc(wchar_t *, slen);
    for (size_t i = 0; i < slen; i++) {
      out[i] = alloc(wchar_t, 3);
      swprintf(out[i], 2, L"%lc", str[i]);
    }
    *len = slen;
    return out;
  }

  // list of counts of each delimiter
  size_t *delimct = wstr_count(str, delims),
           dctsum = 0;

  // sum the counts
  for (size_t i = 0; i < dlen; i++) {
    dctsum += delimct[i];
  }

  // if the sum is 0, just return an array with one element, the original string
  if (! dctsum) {
    free(delimct);
    out    = alloc(wchar_t *, 1);
    out[0] = wstrdup(str);
    *len = 1;
    return out;
  }

  // else find the delimiters

  wchar_t *scopy = wstrdup(str), // copy of (const * const) str
           *sptr = scopy;//,       // pointer we're going to change
          //*next;                // temp. pointer to the next delimiter

  out = alloc(wchar_t *, dctsum);

  size_t* lens_to_next = alloc(size_t, dlen);

  for (size_t i = 0; i < dctsum; i++) {
    for (size_t ns = 0; ns < dlen; ns++) {
      wchar_t* next = wcschr(sptr, delims[ns]);
      wprintf(L"next = %d\n", next[0]);
      if (NULL == next) { break; }
      lens_to_next[ns] = (size_t) (next - sptr);
      wprintf(L"len : %zu\n", lens_to_next[ns]);
    }

    size_t *minptr = size_t_array_minmax(lens_to_next, dlen, op_comp_min_sizet),
              diff = (size_t) (minptr - lens_to_next);


    out[i] = memcpy(out[i], sptr, diff);
    sptr += diff + 1;
  }

  free(scopy);
  free(delimct);
  free(lens_to_next);

  *len = dctsum + 1;
  return out;
}
