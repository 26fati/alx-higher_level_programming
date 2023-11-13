#!/usr/bin/node

// a script that prints the first argument passed to it.
const argv = process.argv;
if (argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
