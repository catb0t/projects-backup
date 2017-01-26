#!/usr/bin/env node

"use strict";

let _ = require("lodash"),
  fp  = require("lodash/fp"),
  len = function (xs) {
    if (xs.length === undefined)
      throw new TypeError("'len': can't read property 'length' of undefined");
    return xs.length;
  },
  empty = function (xs) { return len(xs); },
  Stack = new Array()
  run = function;