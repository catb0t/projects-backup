import std.stdio;
import std.conv;

void main() {
    int[5] squares;

    writeln("Please enter numbers");

    for (int i; i < squares.length; i++) {
      int num;
      write("\nnumber" ~ i.to!string ~ " ");
      string inp = readln;
      try {
        num = inp[0.. $ - 1].to!int;
        squares[i] = num * num;
      } catch( ConvOverflowException) {
        writeln("nope.");
      }
    }

    writeln("=== The squares of the numbers ===");
    for (int i; i < squares.length; i++) {
      writeln(squares[i]);
    }

}