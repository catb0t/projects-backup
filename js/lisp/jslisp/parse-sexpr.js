#!/usr/bin/env js
var mal_rep = function () {
  var readline = require('readline'),
      rl = readline.createInterface(process.stdin, process.stdout, null),
      prompt = '> ';

  rl.on('line', function (line) {
    parse(line);
    rl.setPrompt(prompt);
    rl.prompt();
  }).on('close', function () {
    writeln("bye!");
    process.exit(1);
  }).on("SIGINT", function () {
    writeln("caught sigint");
    process.exit(2);
  });
  rl.setPrompt(prompt);
  rl.prompt();
};

var parse = function () {

}

mal_rep();