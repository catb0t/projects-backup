import std.stdio, std.array, std.algorithm;

void main(string[] args) {
  for(int i=0;i<args.length;writeln(args[i++])){};

  foreach(a;args)writeln(a);
  each!writeln(args);
  writeln(true);
  return writeln(m());
}

int m() {
  int z = 38, s = 4;
  s--;
  z /= s;
  return z;
}