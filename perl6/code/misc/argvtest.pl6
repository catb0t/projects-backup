sub MAIN(Bool :$help = True, Str :$hello, Int :$world) returns Int {
  say $help.perl, " ", $hello.perl, " ", $world.perl;
  return 0;
}