const {floor, E} = Math;

function generator(n) {
  return 1 + (floor(n * (E**11)) % 100);
};

module.exports = generator;
