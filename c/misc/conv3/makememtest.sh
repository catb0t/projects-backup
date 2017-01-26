#!/bin/sh

FILENAME=conv_memtest.c
CONTENTS=$(cat test_*.c | sed -r 's/(^Test.*|cr_assert.*|^}|^#)/\/\/\1/gm')
(
  echo '/* BEGIN GENERATED CODE */
#include "conv.c"
void test (void);

int main (void) { test(); return EXIT_SUCCESS; }

void test (void) {
'
  printf "%s" "$CONTENTS"
  printf "\n%s\n" "} /* END GENERATED CODE */ "
) > $FILENAME
