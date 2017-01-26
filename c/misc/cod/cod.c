int f (int);

i,j;f(n){for(i=1;(j=i)<=n;i++)while(j)printf("%d",j--);}

int main(const int argc, const char* const * const argv) {
  f(atoi(argv[1]));
  return 0;
}
