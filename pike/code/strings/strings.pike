#!/usr/bin/env pike

int main() {
  mixed x = a(({"asd", "asd"}));
  write("%d\n", x);
}

mixed a(mixed b){return sort((array)replace(lower_case(b)," ",""));}
int s(mixed i){return a(i[0])==a(i[1]);}