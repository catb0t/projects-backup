#include <stdio.h>
#include <inttypes.h>
#include <string.h>
#include <stdlib.h>
#define U uint64_t
#define S size_t
S      f (S);
S f(S n){U x=0;S c=1,l;U*b=malloc(sizeof(U));while(c<=n){char s[21];snprintf(s,20,"%"PRIu64,x);U m=0,t=1;l=strnlen(s,21);for(S i=0;i<l;i++){U a=(U)s[i]-48;m+=a,t*=a;}if(m*t?(!(x%m))&&(!(x%t)):0)b=realloc(b,sizeof(U)*++c),b[c-1]=x;++x;}U o=b[n];free(b);return o;}

int main(const int argc, const char* const * const argv) {
  (void) argc;
  S arg = strtoull(argv[1], NULL, 10);
  U a = f(arg);
  printf("a: %" PRIu64 "\n", a);
  return 0;
}


