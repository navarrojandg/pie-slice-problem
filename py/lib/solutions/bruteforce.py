from lib.slice import Slice
from lib.stack import Stack 

def solve(stack: Stack):
  permutationArray = getPermArray(len(stack))
  hasSolution = False
  for p in permutationArray:
    stack.configure(p)
    if stack.validate() is True:
      hasSolution = True
      break
  return hasSolution

def getPermArray(stackLength):
  permuations = []
  for i in range(3**stackLength):
    for j in range(stackLength):
      if j % stackLength == 0:
        permuations.append([int(i/3**j % 3)])
      else:
        permuations[-1].append(int(i/3**j % 3))
  return permuations