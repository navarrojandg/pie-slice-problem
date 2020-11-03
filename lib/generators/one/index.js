const yargs = require('yargs/yargs');
const argv = yargs(process.argv).argv;
const { slices, repeats } = argv;
const {floor, PI} = Math;

const colorCache = [];

function generator(n) {
  let color = getColor(n);
  if (!!repeats) {
    while (isInvalidColor(color)) {
      ++color;
    };
  };
  colorCache.push(color);
  return color;
};

function getColor(n) {
  return 1 + (floor(n * (PI**11)) % slices);
};

function isInvalidColor(color) {
  return colorCache.filter(cached => cached == color).length >= repeats; 
};

module.exports = {
  generator1: generator
};
