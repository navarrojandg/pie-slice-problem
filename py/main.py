from lib.stack import stacksFromFile
from lib.stack import solve
from lib.stack import Stack
from lib.slice import Slice
if __name__ == "__main__":
  puzzles = stacksFromFile('../dataset.txt')

  print(solve(puzzles['puzzle2']))
  print()
  print(puzzles['puzzle2'])