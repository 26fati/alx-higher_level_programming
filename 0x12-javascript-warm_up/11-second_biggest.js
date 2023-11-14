#!/usr/bin/node

// a script that searches the second biggest integer in the list of arguments.

const argv = process.argv;
const arr = argv.map(Number).slice(2).sort((a, b) => a - b);
if (!argv[2] || argv.length === 3) { console.log('0'); } else {
  console.log((arr[arr.length - 2]));
}
