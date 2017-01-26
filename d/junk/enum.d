import std.stdio;
import std.exception;

void main(string[] args) {
  string number;
  try {
    readf("%s;", &number);
  } catch (Throwable e) {
    writeln("\n" ~ e.toString);
  }
  writeln(number);
}