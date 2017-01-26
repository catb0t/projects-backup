module FizzBuzz;

import std.stdio;
import std.conv;

void main() {
  string x,y;
  for (
    int i;
    i++ < 100;
    x = ((i % 3 ? "" : "Fizz")
      ~ (i % 5 ? "" : "Buzz")),
    y ~= (x ? x : i.to!string) ~ "\n"
  ){};
  write(y);
}

/*
import std.stdio,std.conv;void main(){string x;for(int i;i++<100;x=((i%3?"":"Fizz")~(i%5?"":"Buzz")),writeln(x?x:i.to!string)){};}
*/