#!/usr/bin/node

// a script that prints x times “C is fun”
argv = process.argv;
let x = argv[2]
if (!x || isNaN(x))
    console.log('Missing number of occurrences');
else {
    for (let i = 0; i < x; i++)
        console.log('C is fun');
}
