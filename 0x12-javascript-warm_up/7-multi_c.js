#!/usr/bin/node

// a script that prints x times “C is fun”
const argv = process.argv;
const x = argv[2];
if (!x || isNaN(x)) { console.log('Missing number of occurrences'); } else {
  for (let i = 0; i < x; i++) { console.log('C is fun'); }
}
