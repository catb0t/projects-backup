f (char*);

i,z;f(char*s){i=strlen(s);z=1+log10(i);sprintf(realloc(s,i+z)+i,"%d",i+z);}

g(char*);
g(char*s){
  i=strlen(s);
  z=ceil(log10(i));
  s=realloc(s,i+z+1);
  sprintf(s+i,"%d",i+z);
}

int main(void) {
  char* s = malloc(1024);
  gets(s);
  g(s);
  printf("%s\n", s);
  return 0;
}
