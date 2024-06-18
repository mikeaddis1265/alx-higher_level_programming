#!/usr/bin/node
const { argv } = require('node:process');
function add(a, b){
    return a + b;
}
let num1 = Number(argv[2]);
let num2 = Number(argv[3]);
console.log(add(num1, num2));
