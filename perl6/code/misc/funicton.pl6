my @arr = 1..get;
my sub sqr (Int:D $x) returns Int:D {
  return $x ** 2
}

for @arr -> $i {
  say sqr $i
}