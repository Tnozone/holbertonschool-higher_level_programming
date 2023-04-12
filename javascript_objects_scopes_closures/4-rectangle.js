#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        str += 'X';
      }
      console.log(str);
      str = '';
    }
  }

  rotate () {
    if (!this.width || !this.height) {
    } else {
      [this.width, this.height] = [this.height, this.width];
    }
  }

  double () {
    if (!this.width || !this.height) {
    } else {
      this.width *= 2;
      this.height *= 2;
    }
  }
}

module.exports = Rectangle;
