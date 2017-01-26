use v6;

my ($major, $minor) = prompt("Dimensions? ").comb(/\d+/);
die "Please enter two dimensions" unless $major && $minor;

my @array := [ for ^$major { [ for ^$minor { '@' } ] } ];

@array[ (^$major).pick  ][ (^$minor).pick ] = ' ';

.Str.say for @array;