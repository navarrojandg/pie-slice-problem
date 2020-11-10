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
  
  def pop(self, i=-1) -> Slice:
    return self.slices.pop(i)

  def validate(self) -> bool:
    sides = [[], [], []]
    for _slice in self:
      for j, color in enumerate(_slice):
        if (color in sides[j]):
          return False
        sides[j].append(color)
    return True
  
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
  
  def reset(self):
    for s in self.slices:
      s.reset()

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

def stackSliceAndValidate(_slice: Slice, _stack: Stack):
  _stack.push(_slice)
  valid = _stack.validate()

  while(_slice.rotations < 3 and not valid):
    valid = rotateSliceAndValidate(_slice, _stack)
  
  return valid
  
def rotateSliceAndValidate(_slice:Slice, _stack:Stack):
  _slice.rotate()
  return _stack.validate()

def allStackChecked(stack: Stack):
  return all(map(lambda s: s.checked, stack))

def solve(stack: Stack) -> Stack:
  solutionStack = Stack()
  solutionStack.push(stack.pop())

  while(not allStackChecked(stack)):
    valid = stackSliceAndValidate(stack.pop(), solutionStack)
    if not valid:
      _slice = solutionStack.pop(0)
      if _slice.rotations == 3:
        _slice.checked = True
      stack.push(_slice)

  return solutionStack
