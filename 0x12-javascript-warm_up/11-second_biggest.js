#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length <= 3 ){
    console.log(0);
}

let first = Number(argv[2]);
let second = Number(argv[2]);

for (let i = 3; i <= argv.length; i++){
    if ( Number(argv[i]) > first){
        let temp = first;
        first = Number(argv[i]);
        second = temp;
    }
    else{
        if (Number(argv[i] > second) || (first == second)){
            second = Number(argv[i]);
        }
       
    }
}
console.log(second)