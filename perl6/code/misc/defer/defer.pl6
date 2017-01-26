use strict;
class main {
  # use strict
  for 1 .. 5 -> $i {
    my $defer = Defer::Sub.new(
      sub (*@_) {
        print('end' ~ chr(10))
      }
    );
    print('start' ~ chr(10) ~ $i ~ chr(10))
  }
}
class Defer::Sub {
  our sub new (*@_) {
    my $class = shift(@_);
    @_ || fail($class ~ ' requires a function to call' ~ chr(10));
    my $self = {'func' => shift(@_)};
    return(bless($self, $class))
  }
  our sub DESTROY (*@_) {
    my $self = shift(@_);
    $self ~ 1.()
  }
}

;
