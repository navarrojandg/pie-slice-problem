from typing import List
from lib.slice import Slice
import os
import json

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
  
  def fromStack(self, stack):
    for s in stack:
      self.slices.append(s)
  
  def toArray(self) -> List[Slice]:
    return [self[i] for i in range(self.__len__())]
  
  @staticmethod
  def fromFile(filename):
    dirname = os.path.dirname(os.path.realpath('__file__'))
    filepath = os.path.join(dirname, filename)
    with open(filepath) as f:
      dataset = json.load(f)
      c1 = CircularArray().fromArray(dataset['one'])
      c2 = CircularArray(1).fromArray(dataset['two'])
      c3 = CircularArray().fromArray(dataset['three'])
      c4 = CircularArray().fromArray(dataset['four'])

      return {
        'one': c1,
        'two': c2,
        'three': c3,
        'four': c4
      }