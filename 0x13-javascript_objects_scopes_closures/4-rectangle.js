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

  // prints the rectangle using X
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // exchanges the width and the height of rectangle
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  // multiples the width and height by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
