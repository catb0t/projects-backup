module ManageTrashSo;

import std.stdio;
import std.string;
import std.algorithm;

int main(string[] args) {
  auto x = y(["ASD", "asd"]);
  writeln(x);
  x = c(["asd", "ASD"]);
  writeln(x);
  return 233;
}

auto y(string[]a) pure {
  return sort(split(strip(a[0].toLower),"")) == sort(split(strip(a[1].toLower),""));
}

auto c = (string[]a) => sort(split(strip(a[0].toLower),"")) == sort(split(strip(a[1].toLower),""));

auto s(string h) pure {
  return sort(split(strip(h.toLower),""));
}