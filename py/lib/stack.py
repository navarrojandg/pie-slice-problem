#array of slices
from typing import List
from typing import Dict
from lib.slice import Slice
import os
import json

class Stack:
  def __init__(self):
    self.slices: List[Slice] = []
  
  def __str__(self) -> str:
    return '\n'.join([str(s) for s in self.slices])
  
  def __len__(self) -> int:
    return self.slices.__len__()

  def __getitem__(self, i) -> Slice:
    return self.slices[i]
  
  def __delitem__(self, i):
    del self.slices[i]

  def __iter__(self):
    return self.slices.__iter__()

  def push(self, slice: Slice):
    self.slices.insert(0, slice)
  
  def pop(self) -> Slice:
    return self.slices.pop()

  def isValid(self) -> (bool, int):
    sides = [[], [], []]
    for _slice in self:
      for j, color in enumerate(_slice):
        if (color in sides[j]):
          return False, _slice.id
        sides[j].append(color)
    return True, None
  
  def fromArray(self, arr):
    for s in arr:
      self.push(Slice(s))
    return self

  def getSliceById(self, id) -> Slice:
    if(id is None): return None
    result = list(filter(lambda s: s.id == id, self.slices))
    if len(result) > 0:
      return result[0]
    else:
      return None
  
  def delSliceById(self, id):
    self.slices = list(filter(lambda s: s.id != id, self.slices))

def stacksFromFile(filename) -> Dict[str, Stack]:
  dirname = os.path.dirname(os.path.realpath('__file__'))
  filepath = os.path.join(dirname, filename)
  
  with open(filepath) as f:
    dataset = json.load(f)
    return {
      'puzzle1': Stack().fromArray(dataset['puzzle1']),
      'puzzle2': Stack().fromArray(dataset['puzzle2']),
      'puzzle3': Stack().fromArray(dataset['puzzle3']),
      'puzzle4': Stack().fromArray(dataset['puzzle4'])
    }

def stackSliceAndValidate(_slice:Slice, _stack:Stack):
  _stack.push(_slice)
  valid, badSliceIndex = _stack.isValid()

  if(not valid):
    s = _stack.getSliceById(badSliceIndex)
    while(s.rotations < 3 and not valid):
      valid, badSliceIndex = rotateSliceAndValidate(s, _stack)

  return valid, badSliceIndex
  
def rotateSliceAndValidate(_slice:Slice, _stack:Stack):
  _slice.rotate()
  return _stack.isValid()

def solve(stack: Stack) -> Stack:
  solutionStack = Stack()
  solutionStack.push(stack.pop())  

  while(not all(map(lambda s: s.checked, stack))):
    valid, badSliceIndex = stackSliceAndValidate(stack.pop(), solutionStack)
    if (not valid):
      _slice = solutionStack.getSliceById(badSliceIndex)
      _slice.checked = True
      solutionStack.delSliceById(_slice.id)
      stack.push(_slice)

  return solutionStack
