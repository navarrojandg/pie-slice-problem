const yargs = require('yargs/yargs');
const argv = yargs(process.argv).argv;
const {slices, repeats} = argv;
const {floor, PI} = Math;

const colorCache = [];
let indexCache = 1;

function generator(n) {
  if (indexCache !== n) n = indexCache;
  let color = getColor(n);
  if (!!repeats) {
    while (isInvalidColor(color)) {
      color = getColor(++indexCache);
    };
  };
  colorCache.push(color);
  indexCache++;
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
