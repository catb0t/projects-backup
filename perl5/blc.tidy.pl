$z = !pop;
sub g { $x ||= ( $c = getc, $z ? 8 : 1 ); vec $c, --$x, 1 }

sub I {
    my $i = pop;
    sub {
        my $c;
        (
            $B[$i] ||=
              defined( $c = getc )
            ? sub { pop->( $z ? b( $c, 8 ) : a($c) )->( I( $i + 1 ) ) }
            : sub {
                sub { pop }
            }
        )->(pop);
      }
}

sub P {
    if ( g() ) {
        my $i;
        $i++ while g();
        sub { $_[$i] }
    }
    elsif ( g() ) {
        my $p = P();
        my $q = P();
        sub {
            my @a = @_;
            $p->(@a)->( sub { $q->(@a)->(pop) } );
          }
    }
    else {
        my $p = P();
        sub {
            my @a = @_;
            sub { $p->( pop, @a ) }
          }
    }
}

sub e {
    pop->( sub { 0 } )->( sub { 1 } )->();
}
$| = 1;

sub d {
    my $x = pop;
    pop->(
        sub {
            $x = 2 * $x + e(pop);
            sub {
                my $r = pop;
                sub { d( $r, $x ) }
              }
        }
    )->( chr $x );
}

sub O {
    pop->(
        sub {
            print( $z? d( pop, 0 ) : e(pop) );
            sub {
                my $r = pop;
                sub { O($r) }
              }
        }
    )->("\n");
}

sub b {
    my ( $c, $x ) = @_;
    sub {
        $x-- ? pop->( a( vec $c, $x, 1 ) )->( b( $c, $x ) ) : sub { pop }
      }
}

sub a {
    my $c = pop;
    sub {
        my $x = pop;
        sub { $c ? pop : $x }
      }
}
print O P()->()->( I(0) )
