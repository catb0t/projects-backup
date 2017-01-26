#include <criterion/criterion.h>
#include "conv.c"

Test(util, udiff) {
  cr_assert_eq(7, udiff(14, 7));
  cr_assert_eq(7, udiff(7, 14));
}

Test(wcs, chomp) {
  wchar_t* a = malloc(sizeof (wchar_t) * 5);
  swprintf(a, 5, L"abc\n");
  wchomp(&a);
  cr_assert(! wcscmp(a, L"abc"));
  free(a);
}

Test(wcs, str_find) {
  cr_assert(-1 == wstr_find(L"abc", L'z'));
  cr_assert(0  == wstr_find(L"abc", L'a'));
  cr_assert(1  == wstr_find(L"abc", L'b'));
  cr_assert(2  == wstr_find(L"abc", L'c'));
}

Test(wcs, str_count) {
  const wchar_t* const mystr = L"abccac"; // a = 2, b = 1, c = 3
  size_t  *cts = wstr_count(mystr, L"abc"),
         *cmp2 = alloc(size_t, 3);

  cmp2[0] = 2;
  cmp2[1] = 1;
  cmp2[2] = 3;

  cr_assert(! memcmp(cts, cmp2, sizeof (size_t) * 3));

  free(cts);
  free(cmp2);

  cts  = wstr_count(mystr, L"");
  cmp2 = alloc(size_t, 0);

  cr_assert(! memcmp(cts, cmp2, 0 * sizeof (wchar_t)));

  free(cts);
  free(cmp2);

  cts  = wstr_count(L"", L"asd");
  cmp2 = alloc(size_t, 0);

  cr_assert(! memcmp(cts, cmp2, 0 * sizeof (wchar_t)));

  free(cts);
  free(cmp2);

  cts  = wstr_count(L"aaabbcccddddeeeee", L"abcdeabcde");
  cmp2 = alloc(size_t, 10);

  cmp2[0] = 3;
  cmp2[1] = 2;
  cmp2[2] = 3;
  cmp2[3] = 4;
  cmp2[4] = 5;
  cmp2[5] = 3;
  cmp2[6] = 2;
  cmp2[7] = 3;
  cmp2[8] = 4;
  cmp2[9] = 5;

  cr_assert(! memcmp(cts, cmp2, 10));

  free(cts);
  free(cmp2);

  cr_assert(NULL == wstr_count(NULL, NULL));
  cr_assert(NULL == wstr_count(L"", NULL));
  cts = wstr_count(NULL, L"abc<");
  for (size_t i = 0; i < 3; i++) {
    cr_assert(! cts[i]);
  }
  free(cts);
}

Test(wcs, uniq) {
  wchar_t* uniq = wstr_uniq(L"abcabc");

  cr_assert(! wcscmp(uniq, L"abc"));

  free(uniq);

  uniq = wstr_uniq(L"asdfgsjkfghfsdflasdsjkafhgkadfklgjhdfksjgahjklfghajkdfhgkdjflghkdjfghjkdfgdfg");

  cr_assert(! wcscmp(uniq, L"asdfgjkhl"));

  free(uniq);

  uniq = wstr_uniq(L"");
  wchar_t* temp = alloc(wchar_t, 0);

  // easy pass
  cr_assert(! memcmp(temp, uniq, 0));

  free(temp), free(uniq);

  uniq = wstr_uniq(L" ");
  cr_assert(! wcscmp(uniq, L" "));

  free(uniq);
}

Test(wcs, ndup) {
  wchar_t* my2str = wstrdup(L"abcdef");

  cr_assert(! wcscmp(my2str, L"abcdef"));

  free(my2str);

  my2str = wstrndup(L"abc", 2);
  cr_assert(! wcscmp(my2str, L"ab"));

  free(my2str);
}

Test(wcs, nlen) {
  cr_assert(0 == wstrlen(L""));
  cr_assert(0 == wstrnlen(L"", 0));
  cr_assert(0 == wstrnlen(L"", 10));
  cr_assert(1 == wstrlen(L" "));
  cr_assert(1 == wstrnlen(L" ", 10));
  cr_assert(6 == wstrlen(L"abcdef"));
  cr_assert(3 == wstrnlen(L"abcdef", 3));
}

Test(util, array_min) {
  srand( 1 ); // important -- the min of 10 rand() calls with this seed is 424238335
  const size_t nlen = 10;
  size_t* const ss = alloc(size_t, nlen);
  for (size_t i = 0; i < nlen; i++) {
    ss[i] = (size_t) rand();
  }
  const size_t* const minptr = size_t_array_minmax(ss, nlen, op_comp_min_sizet);
  //424238335;
  cr_assert(424238335 == *minptr);
  free(ss);
}

// how dreadful.....
Test(wcs, str_split) {
  cr_assert(NULL == wstr_split(NULL, NULL, NULL));
  cr_assert(EINVAL == errno);

  const wchar_t* const empty = L"";

  size_t len;

  wchar_t** res = wstr_split(empty, empty, &len);

  cr_assert(! wcscmp(res[0], L""));
  cr_assert(1 == len);

  free_array(res, len);

  res = wstr_split(L"abcde", empty, &len);

  // { "a" "b" "c" "d" "e" }
  for (size_t i = 0; i < 5; i++) {
    cr_assert( ( (wchar_t) i + 97) == res[i][0] );
  }

  free_array(res, len);

  res = wstr_split(empty, L"some separators", &len);

  free_array(res, len);

  res = wstr_split(L"a b", L" ", &len);
  cr_assert(2 == len);

  wchar_t** tmp = alloc(wchar_t *, len);
  static const wchar_t* const __tmp[] = {L"a", L"b"};
  memcpy(tmp, __tmp, sizeof (wchar_t *) * len);

  for (size_t i = 0; i < (len - 1); i++) {
    wprintf(L"%zu r:%d\n", i, res[i][0]);
  }

  cr_assert(! memcmp(res, tmp, sizeof (wchar_t) * len));

  free_array(res, len);
  free(tmp);
}
