#!/usr/bin/node

// script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer.

const argv = process.argv;
if (!argv[2] || isNaN(argv[2])) { console.log('Not a number'); } else { console.log(`My number: ${Math.trunc(Number(argv[2]))}`); }
