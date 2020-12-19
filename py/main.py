from lib.slice import Slice
from lib.solutions import triplecolors
from lib.solutions import bruteforce
from lib.circulararray import CircularArray

if __name__ == "__main__":
  puzzleSet = CircularArray.fromFile('../dataset.txt')
  for name, puzzle in puzzleSet.items():
    print(f'Puzzle{name.capitalize()}')
    print('Obstacles')
    triplecolors.solve(puzzle)
    print('\n')