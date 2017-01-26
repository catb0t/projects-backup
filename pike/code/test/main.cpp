# ifndef __PIKE__
#   include<stdio.h>
#   define write(x) printf(x)
# endif
int main() {
  write("Hello, World!\n");
  return 0;
}