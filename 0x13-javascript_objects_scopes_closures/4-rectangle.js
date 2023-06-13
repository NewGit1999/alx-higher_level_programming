#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let a = 0;
    for (a = 0; a < this.height; a++) {
      let b = 0;
      let demension = '';
      for (b = 0; b < this.width; b++) {
        demension = demension + 'X';
      }
      console.log(demension);
    }
  }

  rotate () {
    const recv = this.width;
    this.width = this.height;
    this.height = recv;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
