my regex perlish    { .*[ea]?[ui]? rl $ }

my sub calc-things (Str $word) returns Nil {
  if $word eq $word.flip && $word.chars > 1 { say "$word is a palindrome"; }
  if $word ~~ /<perlish>/ { say "$word probably rhymes with Perl"; }
  return Nil
}

my Str @file = '/usr/share/dict/words'.IO.lines;

