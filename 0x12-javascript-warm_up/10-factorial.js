#!/usr/bin/node
const { argv } = require('node:process');
function factorial(a){
    if(a == 1 || isNaN(a)){
        return 1
    }else
    {
      return a * factorial(a - 1);
    }
}
console.log(factorial(Number(argv[2])));
