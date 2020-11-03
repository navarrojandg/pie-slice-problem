const fs = require('fs');
const path = require('path');
const yargs = require('yargs/yargs');
const argv = yargs(process.argv).argv;
const { colors, slices, repeats } = argv;
const {generator1} = require('./lib/generators/one');
const {generator2} = require('./lib/generators/two');
const {generator3} = require('./lib/generators/three');
const {generator4} = require('./lib/generators/four');

const filename = path.join(__dirname, 'dataset.txt'); 
const puzzles = {
  puzzle1: [],
  puzzle2: [],
  puzzle3: [],
  puzzle4: [],
};

for (let i = 1; i <= colors; i++) {
  if (i % 3 == 1) {
    puzzles.puzzle1.unshift([generator1(i)]);
    puzzles.puzzle2.unshift([generator2(i)]);
    puzzles.puzzle3.unshift([generator3(i)]);
    puzzles.puzzle4.unshift([generator4(i)]);
  } else {
    puzzles.puzzle1[0].push(generator1(i));
    puzzles.puzzle2[0].push(generator2(i));
    puzzles.puzzle3[0].push(generator3(i));
    puzzles.puzzle4[0].push(generator4(i));
  };
  if (i % 3 == 0) {
    // take the previous value and transform to string
    puzzles.puzzle1[0] = puzzles.puzzle1[0].join(',');
    puzzles.puzzle2[0] = puzzles.puzzle2[0].join(',');
    puzzles.puzzle3[0] = puzzles.puzzle3[0].join(',');
    puzzles.puzzle4[0] = puzzles.puzzle4[0].join(',');
  };
};

fs.writeFileSync(filename, JSON.stringify(puzzles, null, 2), 'utf8');
console.log(`output puzzle dataset for ${colors} colors and ${slices} slices and ${repeats} repeats to:\n${filename}`);
