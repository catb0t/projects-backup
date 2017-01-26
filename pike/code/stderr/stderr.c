#include <stdio.h>
# ifndef __PIKE__
#   define werror(x) fputs(x, stderr)
# endif

int main() {
  werror("Hello World!");
}