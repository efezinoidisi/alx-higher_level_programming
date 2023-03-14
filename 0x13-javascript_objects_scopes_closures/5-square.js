#!/usr/bin/node
// This script defines a square that inherits from rectangle
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
