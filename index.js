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
  puzzle1: [],
  puzzle2: [],
  puzzle3: [],
  puzzle4: [],
};

for (let i = 1; i <= colors; i++) {
  if (i % 3 == 1) {
    puzzles.puzzle1.unshift([generator1.generate()]);
    puzzles.puzzle2.unshift([generator2.generate()]);
    puzzles.puzzle3.unshift([generator3.generate()]);
    puzzles.puzzle4.unshift([generator4.generate()]);
  } else {
    puzzles.puzzle1[0].push(generator1.generate());
    puzzles.puzzle2[0].push(generator2.generate());
    puzzles.puzzle3[0].push(generator3.generate());
    puzzles.puzzle4[0].push(generator4.generate());
  };
  if (i % 3 == 0) {
    // take the previous value and transform to string
    puzzles.puzzle1[0] = puzzles.puzzle1[0].join(',');
    puzzles.puzzle2[0] = puzzles.puzzle2[0].join(',');
    puzzles.puzzle3[0] = puzzles.puzzle3[0].join(',');
    puzzles.puzzle4[0] = puzzles.puzzle4[0].join(',');
  };
};

// reverse the order of the puzzles
puzzles.puzzle1 = puzzles.puzzle1.reverse();
puzzles.puzzle2 = puzzles.puzzle2.reverse();
puzzles.puzzle3 = puzzles.puzzle3.reverse();
puzzles.puzzle4 = puzzles.puzzle4.reverse();

fs.writeFileSync(filename, JSON.stringify(puzzles, null, 2), 'utf8');
console.log(`output puzzle dataset for ${colors} colors and ${slices} slices and ${repeats} repeats to:\n${filename}`);
