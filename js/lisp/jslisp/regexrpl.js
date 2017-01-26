#!/usr/bin/env js
var writeln = console.log,
    write   = function (a) { process.stdout.write(String(a)); };

var mal_rep = function () {
  var readline = require('readline'),
      rl = readline.createInterface(process.stdin, process.stdout, null),
      prompt = '> ';

  rl.on('line', function (line) {
    test(line);
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

var test = function (string) {
  var rx = [
    [
      "string", // https://regex101.com/r/hC1iJ4/1
      /(["`])([^\1\\]*?(?:\\.[^\1\\]*)*)\1/,
      " $1$2$1 "
    ],
    [
      "whole number", // https://regex101.com/r/mU9xR1/1
      /([+-]?(?:[\d][\d_]*[\d]|[\d])(?:e[+-]?[+-]?[\d_]+)?[YZEPTGMKHDdcmμnpfazy]*)/
    ],
    [
      "decimal", // https://regex101.com/r/eU3pF5/1
      /([+-]?(?:\d[\d_]*\d[,.]\d*|\d+[,.]|[.,]\d+|\d+[,.]\d+)(?:e[+-]?[+-]?(?:\d[\d_]*\d|\d))?[YZEPTGMKHDdcmμnpfazy]*)/
    ],
    [
      "rational", // https://regex101.com/r/gR3uO2/4
      /((?:[+-]?(?:[\d][\d_]*[\d]|[\d])(?:e[+-]?[+-]?[\d_]+)?[YZEPTGMKHDdcmμnpfazy]*)?[+-]?(?:[+-]?(?:\d[\d_]*\d[,.]\d*|\d+[,.]|[.,]\d+|\d+[,.]\d+)(?:e[+-]?[+-]?(?:\d[\d_]*\d|\d))?[YZEPTGMKHDdcmμnpfazy]*|[+-]?(?:[\d][\d_]*[\d]|[\d])(?:e[+-]?[+-]?[\d_]+)?[YZEPTGMKHDdcmμnpfazy]*)\/(?:[+-]?(?:\d[\d_]*\d[,.]\d*|\d+[,.]|[.,]\d+|\d+[,.]\d+)(?:e[+-]?[+-]?(?:\d[\d_]*\d|\d))?[YZEPTGMKHDdcmμnpfazy]*|[+-]?(?:[\d][\d_]*[\d]|[\d])(?:e[+-]?[+-]?[\d_]+)?[YZEPTGMKHDdcmμnpfazy]*))/,
      ///
    ],
    [
      "arbitrary base number", // https://regex101.com/r/wK4lR0/2
      /(0[a-z0-9]+:[a-zA-Z0-9]+)/
    ],
    [
      "identifier", // https://regex101.com/r/yP6nQ8/1
      /([^\d'"`;\s(){}\[\]][^"`';\s(){}\[\]]*)/,
      " $1 "
    ],
    [
      "symbol", // https://regex101.com/r/kB4cR7/1
      /'([^\d'"`;\s(){}\[\]][^"`';\s(){}\[\]]*)/,
      " '$1 "
    ],
  ], ms = [];
  for (var res, i = 0; i < rx.length; i++) {

    res = rx[i][1].exec(string);

    writeln(rx[i][0] + ": " + (res === null ? res : res[0]));

    if (null != res) {
      ms.push(rx[i][0])
    }
  }
  var a = ms.sort();
  if (ms.length > 1) {
    writeln("\n WARN! more than one match: " + ms);
    if (
      (a.indexOf("identifier") !== -1)
      &&
      ((a.indexOf("rational") !== -1)
        || (a.indexOf("decimal") !== -1)
        || (a.indexOf("whole number") !== -1)
        || (a.indexOf("arbitrary base number") !== -1))) {
      writeln(" probably a number");
    }
  } else {
    (a[0] === "identifier" &&
      (((string[0] === `\"`)
      || (string[0] === "`"))
      || (string.endsWith("`"))
      || (string.endsWith(`"`))))
    || typeof a[0] === "undefined"
      ? writeln("\n probably an unclosed string")
      : writeln("\n is: " + a[0]);
  }
};

mal_rep();
