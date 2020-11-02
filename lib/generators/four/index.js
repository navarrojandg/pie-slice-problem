function generator(n) {
  return 1 + ((n * 29) % 100);
};

module.exports = generator;
