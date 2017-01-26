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

