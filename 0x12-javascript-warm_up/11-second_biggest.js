#!/usr/bin/node

// a script that searches the second biggest integer in the list of arguments.

const argv = process.argv;
const arr = [];
if (!argv[2] || argv.length === 3) { console.log('0'); } else {
  for (let i = 2; i < argv.length; i++) { arr.push(Number(argv[i])); }
  arr.sort((a, b) => a - b);
  console.log(arr);
  console.log(arr[arr.length - 2]);
}
