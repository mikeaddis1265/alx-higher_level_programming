#!/usr/bin/node
const { argv } = require('node:process');

if(isNaN(Number(argv[2]))){
    console.log('Missing number of occurrences');
}else if((x = Number(argv[2]) <= 0))
{
    //do nothing
}else{
    let count = Number(argv[2]);
    for (i = 0; i < count; i++){
        console.log('C is fun');
    }
}
