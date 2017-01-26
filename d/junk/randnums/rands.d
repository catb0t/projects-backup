module RandsToFile;

import core.exception;
import std.algorithm.iteration;
import std.array;
import std.conv;
import std.range;
import std.random;
import std.stdio;

void main(string[] argv) {
  string fname;
  auto num_len = 50_000;
  if (argv.length < 2) {
    writefln("usage: %s FILE [number of numbers]\n\tOR\nusage: %s --help (show this message)", argv[0], argv[0]);
    return;
  } else {
    fname = argv[1];
    try {
      // template to convert string to number
      // D templates are like C++ templates but better
      num_len = argv[2].to!int;
    } catch(RangeError) {
      ;
    } catch(ConvException) {
      writefln("can't convert %s to int, using default %d instead\n", argv[1], num_len);
    }
  }
  auto f = File(fname, "w");
  auto nums = mkNums(num_len);
  fname.write(nums);
}

auto mkNums(int n)
  in { assert(n < 1_000_000); } // contract programming

  body {
    auto nums = iota(0, n).array;
    return nums;
  }
