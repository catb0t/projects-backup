#my token palindrome { (.) <~~> $0 || .? }
my token perlish    { .*[ea]?[ui]? rl $ }
my Str @words = '/usr/share/dict/words'.IO.lines;

for @words -> $word {
}

#`(
say "$word probably rhymes with Perl"
  if $word ~~ /<perlish>/;

say "$word is a palindrome"
  if $word eq $word.flip
  && $word.chars > 1;
)


#`(given $word {
  when /<perlish>/ {
    say "$word probably rhymes with Perl";
    proceed;
  }
  when $word eq $word.flip && $word.chars > 1 {
    say "$word is a palindrome";
    proceed;
  }
}
)

#`(if $word eq $word.flip
&& $word.chars > 1 {
  say "$word is a palindrome"; }
  if $word ~~ /<perlish>/ {
    say "$word probably rhymes with Perl"; }
)

#`($word eq $word.flip  && $word.chars > 1 && say "$word is a palindrome";
$word ~~ /<perlish>/ && say "$word probably rhymes with Perl";
)

#`( inline if:
real    16m14.219s
user    16m7.336s
sys     0m6.336s

real avg : 9.74219s / loop
)

#`( short circuit, 10 iterations:

real    1m1.925s
user    1m1.332s
sys     0m0.504s

real avg : 6.1925s / loop

)

#`( given/when:

real    10m18.568s
user    10m14.292s
sys     0m3.996s

real avg : 6.18568s / loop

)

#`( normal if:

real    10m5.880s
user    10m1.144s
sys     0m4.276s

real avg : 6.0588s / loop

)























#`( palindrome regex + normal if:

real    62m5.719s
user    61m57.012s
sys     0m4.932s

real avg : 37.25719s / loop

)

#`( backtrack-free palindrome regex + normal if, 10 iterations:

real    3m7.557s
user    3m6.980s
sys     0m0.432s

real avg : 18.557s / loop

)