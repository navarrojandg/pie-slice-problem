const {floor, PI, pow} = Math;

function generator(n) {
  return 1 + (floor(n * (PI**11)) % 100);
};

module.exports = generator;
