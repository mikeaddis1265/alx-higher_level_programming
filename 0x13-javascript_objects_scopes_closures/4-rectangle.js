#!/usr/bin/node
class Rectangle{
    constructor(w, h){
        if (h >0 && w > 0){
            this.width = w;
            this.height = h;
        }
        
    }
    print(){
        for (let i = 0; i < this.height; i++){
            let str = ""
            for (let j = 0; j < this.width; j++){
                str += 'X';
            }
            console.log(str);
        }
    }

    rotate(){
        let temp = this.height;
        this.height = this.width;
        this.width = temp;
    }
    double(){
        this.height= 2 * this.height;
        this.width = 2 * this.width;
    }
}
module.exports = Rectangle;
