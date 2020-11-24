#array of slices
from typing import List
from lib.slice import Slice

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
