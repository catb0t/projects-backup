#!/usr/bin/env js

var Assert = function () {
  "use strict";

  var AssertionError = function (msg) {
    var final = "Assertion failed: " + msg;
    console.error(final);
  };

  var args = arguments;
  var res  = true;

  for(var i = 0; i < args.length; i++) {
    var d   = ((i - 1) < 0) ? 0 : i - 1;
    res     = (args[i] === args[d]);
    if(!res || typeof res === "undefined" || res === null || res !== res) {
      throw new AssertionError(args[i] + " != " + args[d]);
    }
  }

  var atn = "not_undefined";

  try {
    atn = assert(res);
  } catch (e) {
    if(e instanceof ReferenceError) {
      return true;
    }
  }

  if(typeof atn === "undefined") {
    return true;
  }
};


// create a car constructor function
var Car = function (c, n) {
	this.color = c;
	this.number = n;
}
// create a carGarage array
var carGarage = [];
// create a loop that creates cars and places them in carGarage
var fillgarage = function () {
	for (var i = 0; i < 10; i++) {
		carGarage[i] = new Car(i < 5 ? "green" : "blue", i);
	}
}

fillgarage();

// test code
for(var i = 0; i < carGarage.length; i++){
	var car = carGarage[i];
  var c = car.color + " car #" + car.number;
  Assert(c, (i < 5 ? "green" : "blue") + " car #" + i);
	console.log(c);
}