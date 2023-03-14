#!/usr/bin/node
// This script defines a square that inherits from the previous Square
const PrevSquare = require('./5-square.js');

class Square extends PrevSquare {
  /* prints the rectangle using the argument passed, if no argument is passed it uses 'X'
  */
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
