const yargs = require('yargs/yargs');
const argv = yargs(process.argv).argv;
const {slices, repeats} = argv;

class Generator3 {
  constructor() {
    this.colorCache = [];
    this.indexCache = 1;
  };
  static getColor(n) {
    return 1 + ((n * 53) % slices);
  };

  generate() {
    let color = Generator3.getColor(this.indexCache);
    if (!!repeats) {
      while(this.isInvalidColor(color)) {
        color = Generator3.getColor(++this.indexCache);
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

module.exports = Generator3;