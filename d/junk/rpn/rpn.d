module rpn;

import std.stdio;
import std.array;
import std.string;
import std.algorithm : among;

void main (string[] args) {

  int[] stk;

  string input;
  bool cont = true;

  do {
    write("> ");
    input = readln().strip();
    cont = stk.run(input);
  } while (input && cont);
}

void run(in ref int[] stk, in string ipt) {

  for(int i; i < ipt.length; i++) {

    char c = ipt[i];

    switch (c) {
      case 'a':

        break;

      default:
        writefln("unknown symbol %d at char %d (ignoring)\n", c, i);
        break;
    }
  }

  return true;
}
