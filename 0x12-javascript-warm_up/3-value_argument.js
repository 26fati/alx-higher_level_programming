#!/usr/bin/node

// a script that prints the first argument passed to it.
argv = process.argv;
let i = 2;
if (argv[2] == undefined) {
    console.log('No argument');
}
else {
    while (argv[i] != undefined) 
     {
        console.log(argv[i]);
        i++;   
    }
}