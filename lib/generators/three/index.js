function generator(n) {
  return 1 + ((n * 53) % 100);
};

module.exports = generator;
