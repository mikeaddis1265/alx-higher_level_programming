#!/usr/bin/node
const { count } = require('node:console');
const { argv } = require('node:process');
if (isNaN(Number(argv[2]))){
    console.log('Missing size');
}else{
    let count = Number(argv[2]);
    let row = 'X'.repeat(count);
    for (let i = 0; i < count; i++){
        console.log(row);
    }
}
