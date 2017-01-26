#!/usr/bin/env perl6

use Test;
plan 2;

class Wizard {
    has Int $!mana;

    method mana() is rw {
        return Proxy.new:
            FETCH => sub ($) { return $!mana },
            STORE => sub ($, $mana) {
                die "It's over 9000!" if ($mana // 0) > 9000;
                $!mana = $mana;
            }
    }
}

my Wizard $gandalf .= new;
$gandalf.mana = 150;
ok $gandalf.mana == 150, 'Updating mana works';
throws-like sub {
    $gandalf.mana = 9001;
}, X::AdHoc, 'Too much mana is too much';