from lib.slice import Slice
from lib.circulararray import CircularArray

permutationArrayCache = {}

def solve(arr: CircularArray):
  permutationArray = getPermArray(len(arr))
  for p in permutationArray:
    arr.configure(p)
    if arr.validate() is True:
      return True
  return False

def getPermArray(size):
  if str(size) in permutationArrayCache:
    return permutationArrayCache[str(size)]
  permuations = []
  for i in range(3**size):
    for j in range(size):
      if j % size == 0:
        permuations.append([int(i/3**j % 3)])
      else:
        permuations[-1].append(int(i/3**j % 3))
  permutationArrayCache[str(size)] = permuations
  return permuations