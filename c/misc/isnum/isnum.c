#include <stdbool.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>

bool is_base10_number (const char* const str);
int f (int*);
int g (int*);

bool is_base10_number (const char* const str) {

  if(!str[0])return false;

  size_t
    dpts = 0,
    cmas = 0;

  for (size_t i = 0; i < strlen(str); i++) {

    if ((str[i] == '-') && (!i)){
      continue;
    }

    if (
      (str[i] == ' ')
      || (str[0] == '.')
      || (str[0] == '+')
      ||
      (
        (!isdigit(str[i]))
        && (str[i] != '.')
        && (str[i] != ',')
      )
    ) {
      return false;
    }

    dpts += str[i] == '.';
    cmas += str[i] == ',';

    if (cmas) {
      if (i & ((i % 4) != 3) & str[i] == ',') {
        return false;
      }
    }

  }

  if (dpts > 1) { return false; }

  return true;
}

b,d,c,i;

g(int*s){
  b=*s;
  for(d=c=i=0;i++,*s++,d+=*s==46,c+=*s==44,b=c?i&(i%4!=3)&*s==44?0:b:b;)
    if(*s!=45&i);
    else if(!(*s!=45&i)&(*s==32)|(*s==46)|*s==43|(!isdigit(*s)&*s!=46&*s!=44)|!(d-1))b=0;
  return b;
}

f (char*s) {

  b=*s;

  for (d = c = i = 0; *(++s); i++) {

    if ((s[i] == '-') && (!i)){
      continue;
    }

    if (
      s[i] == ' '
      | s[0] == '.'
      | s[0] == '+'
      |
      (
        (!isdigit(s[i]))
        & (s[i] != '.'
        & (s[i] != ','
      )
      |!(d - 1)
    ) {
      b=0;
    }

    d += s[i] == '.';
    c += s[i] == ',';

    if (c) {
      if (i & ((i % 4) != 3) & s[i] == ',') {
        b=0
      }
    }

  }
  return b;
}
