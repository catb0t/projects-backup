import std.stdio;

void main() {
  char[] a = "Hello,";
  char[] b = " World!";
  char[] c = a ~ b;
  writeln(c);
}