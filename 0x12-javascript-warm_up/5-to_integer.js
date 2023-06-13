#!/usr/bin/node
const argument = process.argv[2];
const N = parseInt(argument, 10);
if (isNaN(N)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + N);
}
