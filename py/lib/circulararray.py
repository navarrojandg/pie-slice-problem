from typing import List
from lib.slice import Slice

class CircularArray:
  def __init__(self, startingIndex=0):
    self.slices: List[Slice] = []
    self.startingIndex = startingIndex
  
  def __len__(self):
    return self.slices.__len__()
  
  def __getitem__(self, i):
    return self.slices[(self.startingIndex + i) % self.__len__()]

  def fromArray(self, arr):
    for s in arr:
      self.slices.append(Slice(s))
    return self
  
  def toArray(self) -> List[Slice]:
    return [self[i] for i in range(self.__len__())]