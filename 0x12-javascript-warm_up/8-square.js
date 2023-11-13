#!/usr/bin/node

// a script that prints a square.

argv = process.argv;
let x = argv[2]
let str = 'x';
if (!x || isNaN(x))
    console.log('Missing size');
else {
    for (let i = 0; i < x; i++)
        console.log(str.repeat(x));
}