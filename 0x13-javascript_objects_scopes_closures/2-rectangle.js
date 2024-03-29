#!/usr/bin/node
// This script defines a rectangle with width and height
// if w or h is equal to zero returns an empty object

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
