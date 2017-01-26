class NonvivArray is Array {
    multi method AT-POS(NonvivArray:D: Int:D $pos) is raw {
        say 'foo';
        my $val = callsame;
        X::OutOfRange.new(got=>$pos, range=>0..self.elems-1).throw unless $val;
        $val;
    }

    multi method AT-POS(NonvivArray:D: int $ipos) is raw {
        say 'foo';
        my $val = callsame;
        X::OutOfRange.new(got=>$ipos, range=>0..self.elems-1).throw unless $val;
        $val;
    }
}

my NonvivArray $a;
$a.push: 1;
dd $a;
say $a[1];
