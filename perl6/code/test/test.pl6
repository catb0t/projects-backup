use strict;

my sub hello-name (Str $name?) returns Bool {
  if $name eq "" {
    say "Hello, $name!";
  } else {
    say "Hello!"
  }
}

hello-name(prompt "What's your name? ");
