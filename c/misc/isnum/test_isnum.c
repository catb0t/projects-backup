#include <criterion/criterion.h>
#include "isnum.c"

Test(num, a) {
  cr_assert_eq(f("123"), true);
}

Test(num, b) {
  cr_assert_eq(f("-123"), true);
}

Test(num, c) {
  cr_assert_eq(f("0"), true);
}

Test(num, d) {
  cr_assert_eq(f("123.456"), true);
}

Test(num, e) {
  cr_assert_eq(f("123,456.789"), true);
}

Test(num, f) {
  cr_assert_eq(f("123456789"), true);
}

Test(num, g) {
  cr_assert_eq(f("0000001.00000"), true);
}

Test(num, h) {
  cr_assert_eq(f("00.00"), true);
}

Test(num, i) {
  cr_assert_eq(f("999999999.9999999999999999999999999999999999999999999999999999"), true);
}

Test(num, j) {
  cr_assert_eq(f("-999999999.9999999999999999999999999999999999999999999999999999"), true);
}

Test(num, k) {
  cr_assert_eq(f(""), false);
}

Test(num, l) {
  cr_assert_eq(f("lolz"), false);
}

Test(num, m) {
  cr_assert_eq(f("n4melyh4xor"), false);
}

Test(num, n) {
  cr_assert_eq(f("  1.2"), false);
}

Test(num, o) {
  cr_assert_eq(f("9.3 1.3"), false);
}

Test(num, p) {
  cr_assert_eq(f("1e5"), false);
}

Test(num, q) {
  cr_assert_eq(f("50cl05e.buty3ts0f4r"), false);
}

Test(num, r) {
  cr_assert_eq(f("1,2,3,4.5678"), false);
}

Test(num, s) {
  cr_assert_eq(f("1,234.5,678"), false);
}

Test(num, t) {
  cr_assert_eq(f(".234"), false);
}

Test(num, u) {
  cr_assert_eq(f("+1"), false);
}

Test(num, v) {
  cr_assert_eq(f("1.234.3"), false);
}

Test(num, w) {
  cr_assert_eq(f("12345,678"), false);
}
