#!/usr/bin/node
const { argv } = require('node:process');

function isNumeric(str) {
    let num = Number(str);
    return !isNaN(num);
}

if (isNumeric(argv[2])) {  
    console.log('My number: ' + argv[2]);
} else {
    console.log('Not a number');
}
