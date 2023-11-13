#!/usr/bin/node

// a script that computes and prints a factorial.

function factorial (n) {
  if (n === 1 || !n) { return (1); } else { return (factorial(n - 1) * n); }
}

const argv = process.argv;
const n = Number(argv[2]);
console.log(factorial(n));
