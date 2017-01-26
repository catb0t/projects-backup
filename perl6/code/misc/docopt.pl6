#!/usr/bin/env perl6

#`(

./my_program: do stuff with network

Usage:
   my_program tcp <host> <port> [--timeout=<seconds>]
   my_program serial <port> [--baud=<n>] [--timeout=<seconds>]
   my_program (-h | --help | --version)

Options:
   -h, --help  Show this screen and exit.
   --baud=<n>  Baudrate [default: 9600]

Mandatory arguments to long options are mandatory for short options too.

)

my grammar docopt {
  my rule TOP {
    | <any-ws> <any> <any-ws> <usage> <any-ws> <options> <any-ws> <any>
  }

  my rule usage {
    | "Usage:" <any-ws> <use-lines>+ #
  }

  my rule use-lines {
    | <fname> \s <example> \s #
  }

  my token fname {
    [ <!before \/> . ]+ # only the empty string and strings with path separators in them are disallowed.
  }

  my token example {

  }

  my rule options {
    | "Options:" <any-ws> <opts-lines>*
  }

  my token any-ws {
    \s* \n* \s*      # allow any amount of whitespace / newlines
  }

  my token any {
    .*               # allow any text for the "intro" and "outro"
  }

}