#!/usr/bin/node

const Rectangle = require("./4-rectangle");

class Square extends Rectangle{
    constructor(size){
        super(size, size);
    }
    charPrint(c){
        let char = 'X'
        if (c != undefined){
            char = c;
        }
        for (let j = 0; j < this.width; j++){
            let str = '';
            for (let i = 0; i < this.width; i++){
                str += char;
            }
            console.log(str);
        }

    }
}
module.exports = Square;
