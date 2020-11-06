from collections import deque

class Slice:
  def __init__(self, *args):
    self.sides = None
    if (all(isinstance(i, int) for i in args) and len(args) == 3):
      self.sides = deque([int(s) for s in args])
    
    if (type(args[0]) == str):
      self.sides = deque([int(s) for s in args[0].split(',')])
  
  def __str__(self):
    return ','.join(str(i) for i in self.sides)
  
  def __len__(self):
    return len(self.sides)
  
  def __getitem__(self, i):
    return self.sides[i]

  def __iter__(self):
    return iter(self.sides)

  def rotate(self):
    self.sides.rotate(1)