from lib.stack import Stack
from lib.slice import Slice
import lib.solutions.dualstack as dualstack
from lib.circulararray import CircularArray 

import os
import json
def circularArraysFromFile(filename):
  dirname = os.path.dirname(os.path.realpath('__file__'))
  filepath = os.path.join(dirname, filename)
  
  with open(filepath) as f:
    dataset = json.load(f)
    c1 = CircularArray(31).fromArray(dataset['one'])
    c2 = CircularArray().fromArray(dataset['two'])
    c3 = CircularArray().fromArray(dataset['three'])
    c4 = CircularArray().fromArray(dataset['four'])

    return {
      'one': c1.toArray(),
      'two': c2.toArray(),
      'three': c3.toArray(),
      'four': c4.toArray()
    }
if __name__ == "__main__":
  for name, puzzle in dualstack.stacksFromFile('../dataset.txt').items():
    print(f'Puzzle {name.capitalize()}')
    dualstack.solve(puzzle)