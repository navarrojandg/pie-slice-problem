from lib.solver import stacksFromFile
from lib.solver import solve
from lib.stack import Stack
from lib.slice import Slice
if __name__ == "__main__":
  puzzles = stacksFromFile('../dataset.txt')
  puzzleSet = puzzles['one']
  # puzzleSet = puzzles['two']
  # puzzleSet = puzzles['three']
  # puzzleSet = puzzles['four']

  print('solution')
  print(solve(puzzleSet))
  print('\n')

  print('obstacles')
  print(puzzleSet)
