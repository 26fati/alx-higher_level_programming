#!/usr/bin/node

class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) { super.print(); } else {
      for (let i = 0; i < this.height; i++) { console.log(c.repeat(this.width)); }
    }
  }
}
module.exports = Square;
