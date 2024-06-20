#!/usr/bin/node
exports.esrever = function (list){
    let length = list.length;
    let numOfIteration = Math.floor(list.length / 2);

    for (let i = 0; i < numOfIteration; i++){
        let temp = list[i];
        list[i] = list[length - 1 - i];
        list[length - 1 - i] = temp;
    }

    return list;
}