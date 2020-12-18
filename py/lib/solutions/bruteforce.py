from lib.slice import Slice
from lib.stack import Stack 

permutationArrayCache = {}

def solve(stack: Stack):
  permutationArray = getPermArray(len(stack))
  for p in permutationArray:
    stack.configure(p)
    if stack.validate() is True:
      return True
  return False

def getPermArray(stackLength):
  if str(stackLength) in permutationArrayCache: 
    return permutationArrayCache[str(stackLength)]
  permuations = []
  for i in range(3**stackLength):
    for j in range(stackLength):
      if j % stackLength == 0:
        permuations.append([int(i/3**j % 3)])
      else:
        permuations[-1].append(int(i/3**j % 3))
  permutationArrayCache[str(stackLength)] = permuations
  return permuations