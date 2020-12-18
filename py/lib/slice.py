from collections import deque

class Slice:
  count = 0
  def __init__(self, *args):
    self.sides = deque([0,0,0])
    if (all(isinstance(i, int) for i in args) and len(args) == 3):
      self.sides = deque([int(s) for s in args])
    
    if (type(args[0]) == str):
      self.sides = deque([int(s) for s in args[0].split(',')])
    Slice.count += 1
    self.id = str(Slice.count)
    self.rotations = 0
    self.checked = False
    self.sidesCache = self.sides
  
  def __str__(self):
    return f'id[{self.id}]\t\t' + '\t'.join(str(i) for i in self.sides) + f'\tR{self.rotations}'
  
  def __len__(self):
    return len(self.sides)
  
  def __getitem__(self, i):
    return self.sides[i]

  def __iter__(self):
    return iter(self.sides)

  def rotate(self, count=1):
    self.sides.rotate(count)
    self.rotations += count
  
  def reset(self):
    self.checked = False
    self.sides = self.sidesCache
    self.rotations = 0

  def hasColor(self, color):
    if self[0] == color:
      return 0
    if self[1] == color:
      return 1
    if self[2] == color:
      return 2
    return -1
  
  def isInColorRange(self, start, end):
    bounds = range(start, end+1)
    if self[0] not in bounds:
      return False
    if self[1] not in bounds:
      return False
    if self[2] not in bounds:
      return False
    return True