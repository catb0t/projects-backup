function ScratchLexer(text) {
	var words = text.split(/\s+/);
	var next = 0;
	this.nextWord = function () {
		if (next >= words.length) return null;
		return words[next++];
	};
}

function Scratch () {
	var dictionary = {};

	this.stack = [];

	this.addWords = function (new_dict) {
		for (var word in new_dict)
			dictionary[word.toUpperCase()] = new_dict[word];
	};

	this.run = function (text) {
		var lexer = new ScratchLexer(text);
		var word;
		var num_val;

		while (word = lexer.nextWord()) {
			word = word.toUpperCase();
			num_val = parseFloat(word);
			if (dictionary[word]) {
				dictionary[word](this);
			} else if (!isNaN(num_val)) {
				this.stack.push(num_val);
			} else {
				throw "Unknown word";
			}
		}
	};
}

var PrintingWords = {
	// Print and discard top of stack.
	"PRINT": function (terp) {
		if (terp.stack.length < 1) throw "Not enough items on stack";
		var tos = terp.stack.pop(); alert(tos);
	},
	// Print out the contents of the stack.
	"PSTACK": function (terp) {
		alert(terp.stack);
	}
};
// Ensure Forth compatibility.
PrintingWords["."] = PrintingWords["PRINT"];
PrintingWords[".S"] = PrintingWords["PSTACK"];

var MathWords = {
	"+": function (terp) {
		if (terp.stack.length < 2) throw "Not enough items on stack";
		var tos = terp.stack.pop();
		var _2os = terp.stack.pop();
		terp.stack.push(_2os + tos);
	},
	"-": function (terp) {
		if (terp.stack.length < 2) throw "Not enough items on stack";
		var tos = terp.stack.pop();
		var _2os = terp.stack.pop();
		terp.stack.push(_2os - tos);
	},
	"*": function (terp) {
		if (terp.stack.length < 2) throw "Not enough items on stack";
		var tos = terp.stack.pop();
		var _2os = terp.stack.pop();
		terp.stack.push(_2os * tos);
	},
	"/": function (terp) {
		if (terp.stack.length < 2) throw "Not enough items on stack";
		var tos = terp.stack.pop();
		var _2os = terp.stack.pop();
		terp.stack.push(_2os / tos);
	},
	"SQRT": function (terp) {
		if (terp.stack.length < 1) throw "Not enough items on stack";
		var tos = terp.stack.pop();
		terp.stack.push(Math.sqrt(tos));
	}
};

var StackWords = {
	// Duplicate the top of stack (TOS).
	"DUP": function (terp) {
		if (terp.stack.length < 1) throw "Not enough items on stack";
		var tos = terp.stack.pop();
		terp.stack.push(tos);
		terp.stack.push(tos);
	},
	// Throw away the TOS -- the opposite of DUP.
	"DROP": function (terp) {
		if (terp.stack.length < 1) throw "Not enough items on stack";
		terp.stack.pop();
	},
	// Exchange positions of TOS and second item on stack (2OS).
	"SWAP": function (terp) {
		if (terp.stack.length < 2) throw "Not enough items on stack";
		var tos = terp.stack.pop();
		var _2os = terp.stack.pop();
		terp.stack.push(tos);
		terp.stack.push(_2os);
	},
	// Copy 2OS on top of stack.
	"OVER": function (terp) {
		if (terp.stack.length < 2) throw "Not enough items on stack";
		var tos = terp.stack.pop();
		var _2os = terp.stack.pop();
		terp.stack.push(_2os);
		terp.stack.push(tos);
		terp.stack.push(_2os);
	},
	// Bring the 3rd item on stack to the top.
	"ROT": function (terp) {
		if (terp.stack.length < 3) throw "Not enough items on stack";
		var tos = terp.stack.pop();
		var _2os = terp.stack.pop();
		var _3os = terp.stack.pop();
		terp.stack.push(_2os);
		terp.stack.push(tos);
		terp.stack.push(_3os);
	},
};
