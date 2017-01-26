#!/usr/bin/perl

use strict;
use warnings;

for my $i (1 .. 5) {
    my $defer = Defer::Sub->new(sub { print "end\n" });
    print "start\n$i\n";
}

package Defer::Sub;

use Carp;

sub new {
    my $class = shift;
    croak "$class requires a function to call\n" unless @_;
    my $self  = {
    	func => shift,
    };
    return bless($self, $class);
}

sub DESTROY {
    my $self = shift;
    $self->{func}();
}
