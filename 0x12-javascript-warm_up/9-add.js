#!/usr/bin/node

// a script that prints the addition of 2 integers.

function add(a, b) {
    console.log(Number(a) + Number(b));
}

argv = process.argv;
add(argv[2], argv[3]);