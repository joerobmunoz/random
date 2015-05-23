var assert = require('assert');
var v = require('./solution.js');

function applyAssert (given, expected) {
	assert.equal(v.validateString(given), expected);
}

applyAssert('a', 'a VALID\n');

applyAssert('l', 'l INVALID\n');

applyAssert('Ze', 'Ze VALID\n');

applyAssert('Za Nj', 'Za VALID\nNj INVALID\n');

applyAssert('QZja\nRhfa', 'QZja VALID\nRhfa INVALID\n');

applyAssert('NZaZb', 'NZaZb VALID\n');

applyAssert('ZNZaZb', 'ZNZaZb VALID\n');

applyAssert('ZZa', 'ZZa VALID\n');

applyAssert('ZZaZb', 'ZZaZb INVALID\n');

applyAssert('abc', 'abc INVALID\n');

applyAssert('Zabc', 'Zabc INVALID\n');

console.log("ALL TESTS PASS!");