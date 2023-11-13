#!/usr/bin/node

// a script that prints a square.

const argv = process.argv;
const x = argv[2];
const str = 'X';
if (!x || isNaN(x)) { console.log('Missing size'); } else {
  for (let i = 0; i < x; i++) { console.log(str.repeat(x)); }
}
