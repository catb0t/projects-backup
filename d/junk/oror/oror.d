import std.stdio;
import std.array;
import std.algorithm;

void main(string[]a) {

  auto x=a[2].split("");
  string y;

  if(canFind(["^","<"],a[1]))
    x.reverse;

  if(canFind(["v","^"], a[1]))
    y=join(x,"\n");

  else
    y=join(x,"");

  y.write;
}
