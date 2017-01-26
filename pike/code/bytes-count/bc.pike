#ifndef __PIKE__
  #include <stdio.h>
  #include <string.h>
  #include <stdlib.h>
  #define string const char*
  #define write(x) printf("%s", x)
  #define string_to_utf8
#endif
int main () {
  string x = "";

  do {
    x = Stdio.stdin->gets();
    write( (string) strlen( x ) + "\n");
  } while (x != "");
}
mixed bc (mixed s) {
  mixed o = "";
  for ()
}