module foobar;

import std.stdio;

void main(string[] args) {
  foreach(a; args) {
    writeln(a);
  }
  immutable(char)[] s = "asd";
}
