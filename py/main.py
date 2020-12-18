from lib.stack import Stack
from lib.slice import Slice
from lib.solutions import triplecolors
from lib.solutions import bruteforce
from lib.circulararray import CircularArray
if __name__ == "__main__":
  # puzzleSet = Stack.stacksFromFile('../dataset.txt')
  # triplecolors.run(puzzleSet['two'])
  puzzleSet = CircularArray.fromFile('../dataset.txt')
  triplecolors.solve(puzzleSet['one'])