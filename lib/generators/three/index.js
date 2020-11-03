const yargs = require('yargs/yargs');
const argv = yargs(process.argv).argv;
const {slices, repeats} = argv;

const colorCache = [];

function generator(n) {
  let color = getColor(n);
  if (!!repeats) {
    while(isInvalidColor(color)) {
      color = getColor(++n);
    };
  };
  colorCache.push(color);
  return color;
};

function getColor(n) {
  return 1 + ((n * 53) % slices);
};

function isInvalidColor(color) {
  return colorCache.filter(cached => cached == color).length >= repeats;
};

module.exports = {
  generator3: generator,
};
