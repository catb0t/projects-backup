#include <stdio.h>

main (n) {

  puts(&n);
  puts(&n+1);
  puts(&n+2);

  ++n;
  puts(&n);
  puts(&n+1);
  puts(&n+2);

  return 0;
}
