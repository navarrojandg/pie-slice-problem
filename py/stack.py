#array of slices
from typing import List
from slice import Slice

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
    self.slices.append(slice)
  
  def pop(self) -> Slice:
    return self.slices.pop()

  def isValid(self) -> (bool, int):
    sides = [[], [], []]
    for i, _slice in enumerate(self):
      for j, color in enumerate(_slice):
        if (color in sides[j]):
          return False, i
        sides[j].append(color)
    return True, None
  
  def print(self):
    for key, value in enumerate(self):
      print(f'[{key}] {value}')