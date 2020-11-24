const fs = require('fs');
const path = require('path');
const yargs = require('yargs/yargs');
const argv = yargs(process.argv).argv;
const { colors, slices, repeats } = argv;
const generator1 = new (require('./lib/generators/one'));
const generator2 = new (require('./lib/generators/two'));
const generator3 = new (require('./lib/generators/three'));
const generator4 = new (require('./lib/generators/four'));

const filename = path.join(__dirname, 'dataset.txt'); 
const puzzles = {
  one: [],
  two: [],
  three: [],
  four: [],
};

for (let i = 1; i <= colors; i++) {
  if (i % 3 == 1) {
    puzzles.one.unshift([generator1.generate()]);
    puzzles.two.unshift([generator2.generate()]);
    puzzles.three.unshift([generator3.generate()]);
    puzzles.four.unshift([generator4.generate()]);
  } else {
    puzzles.one[0].push(generator1.generate());
    puzzles.two[0].push(generator2.generate());
    puzzles.three[0].push(generator3.generate());
    puzzles.four[0].push(generator4.generate());
  };
  if (i % 3 == 0) {
    // take the previous value and transform to string
    puzzles.one[0] = puzzles.one[0].join(',');
    puzzles.two[0] = puzzles.two[0].join(',');
    puzzles.three[0] = puzzles.three[0].join(',');
    puzzles.four[0] = puzzles.four[0].join(',');
  };
};

// reverse the order of the puzzles
puzzles.one = puzzles.one.reverse();
puzzles.two = puzzles.two.reverse();
puzzles.three = puzzles.three.reverse();
puzzles.four = puzzles.four.reverse();

fs.writeFileSync(filename, JSON.stringify(puzzles, null, 2), 'utf8');
console.log(`output puzzle dataset for ${colors} colors and ${slices} slices and ${repeats} repeats to:\n${filename}`);
