#!/usr/bin/node
// This script defines a square that inherits from rectangle
const S = require('./5-square.js');

class Square extends S {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let string = '';
        for (let j = 0; j < this.width; j++) {
          string += c;
        }
        console.log(string);
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
