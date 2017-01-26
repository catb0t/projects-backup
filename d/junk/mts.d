import std.string,std.algorithm,std.stdio;

void main () {
  auto x = (string[]a) =>
    sort(
      split(
        strip(a[0].toLower), ""
      )
    )
    ==
    sort(
      split(
        strip(a[1].toLower), ""
      )
    )
  ;
  writeln(x(["asd", "dsa"]));
}