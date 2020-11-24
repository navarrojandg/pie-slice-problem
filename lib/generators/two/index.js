const yargs = require('yargs/yargs');
const argv = yargs(process.argv).argv;
const {slices, repeats} = argv;
const {floor, E} = Math;

class Generator2 {
  constructor() {
    this.colorCache = [];
    this.indexCache = 1;
  };
  static getColor(n) {
    return 1 + (floor(n * (E**11)) % slices);
  };

  generate() {
    let color = Generator2.getColor(this.indexCache);
    if (!!repeats) {
      while(this.isInvalidColor(color)) {
        color = Generator2.getColor(++this.indexCache);
      };
    };
    this.colorCache.push(color);
    this.indexCache++;
    return color;
  };

  isInvalidColor(color) {
    return this.colorCache.filter(cached => cached == color).length >= repeats; 
  };

  reset() {
    this.colorCache = [];
    this.indexCache = 1;
  };
};

module.exports = Generator2;