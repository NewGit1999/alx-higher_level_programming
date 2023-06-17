#!/usr/bin/node
const total = (function add (a, b) {
  return parseInt(a) + parseInt(b);
})(process.argv[2], process.argv[3]);
console.log(total);
