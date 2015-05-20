'use strict';

// NOTE:
// This is a dynamic programming solution. There also exists a simple recursive solution to the problem.

function Validator () {
	this.validLC = ['a','b','c','d','e','f','g','h','i','j'];
	this.valicUC = ['Z','N','L','Q','R'];
}

Validator.prototype = {
	isValidLC : function isValidLC (c) {
		for (var i = 0; i < this.validLC.length; i++) {
			if (this.validLC[i] === c) return true;
		}

		return false;
	},
	isValidUC : function isValidLC (c) {
		for (var i = 0; i < this.valicUC.length; i++) {
			if (this.valicUC[i] === c) return true;
		}

		return false;
	},
	isZ: function isZ (z) {
		return z === 'Z';
	},
	validateSingleWord: function validateSingleWord (word) {
		var w = word.split('').reverse().join(''); // Work backwards to limit memory.
		var lastIsUC = false;
		var lastIsLC = false;
		var sizeOfCurrentBlock = 0;

		for (var i = 0; i < w.length; i++) {
			if (this.isValidLC(w[i])) {
				sizeOfCurrentBlock++;

				if (lastIsLC) {
					// if it's the second LC and the next one isn't an UC, then reject
					if (i + 1 === w.length) 
					{
						return false; // Reject 2 adjacent LC
					}
					if (!this.isValidUC(w[i+1])) 
					{
						return false;
					}
				}

				lastIsLC = true;
				lastIsUC = false;
			} else if (this.isValidUC(w[i])) {
				if (this.isZ(w[i])) {
					// Case Z
					if (sizeOfCurrentBlock === 1) {
					} else if (sizeOfCurrentBlock === 2 && lastIsLC) {
					} else {
						return false;
					}
				}
				else {
					// Case N,L,Q,R
					if (sizeOfCurrentBlock == 2) {
						sizeOfCurrentBlock = 1;
					} else {
						return false;
					}
				}

				lastIsUC = true;
				lastIsLC = false;
			} else {
				return false;
			}
		}

		return true;
	}
};

var validateString = function validateString (s) {
	var v = new Validator(s);
	var ss = s.split(/\s+/g); // Split on whitespace
	var output = [];
	for (var i = 0; i < ss.length; i++) {
		if (v.validateSingleWord(ss[i])) {
			output.push(ss[i].toString() + " VALID\n");
		} else {
			output.push(ss[i].toString() + " INVALID\n");
		}
 	}

 	// Problem says that it should "return one line per valid string." It's
 	// unclear whether or not it meant to return a string, log it to the console,
 	// or 'yield' it from a generator. I chose to return a string in this case.
 	return output.join('');
}

// Require JS dependency for test execution
module.exports.validateString = validateString;



