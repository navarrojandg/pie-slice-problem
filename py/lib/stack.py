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
    faces = {
      'face0': {},
      'face1': {},
      'face2': {}
    }
    for _slice in self:
      if f'{_slice[0]}' in faces[f'face{0}']:
        return False
      if f'{_slice[1]}' in faces[f'face{1}']:
        return False
      if f'{_slice[2]}' in faces[f'face{2}']:
        return False
      faces[f'face{0}'][f'{_slice[0]}'] = True
      faces[f'face{1}'][f'{_slice[1]}'] = True
      faces[f'face{2}'][f'{_slice[2]}'] = True
    return True

  
  def fromArray(self, arr):
    for s in arr:
      self.push(Slice(s))
    return self
  
  def reset(self):
    for s in self.slices:
      s.reset()
