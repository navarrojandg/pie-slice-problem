from collections import deque

class Slice:
  count = 0
  def __init__(self, *args):
    self.sides = None
    if (all(isinstance(i, int) for i in args) and len(args) == 3):
      self.sides = deque([int(s) for s in args])
    
    if (type(args[0]) == str):
      self.sides = deque([int(s) for s in args[0].split(',')])
    Slice.count += 1
    self.id = str(Slice.count)
    self.rotations = 0
    self.checked = False
  
  def __str__(self):
    return f'id[{self.id}]\t\t' + '\t'.join(str(i) for i in self.sides) + f'\tR{self.rotations}'
  
  def __len__(self):
    return len(self.sides)
  
  def __getitem__(self, i):
    return self.sides[i]

  def __iter__(self):
    return iter(self.sides)

  def rotate(self):
    self.sides.rotate(1)
    self.rotations += 1
  
  def reset(self):
    self.checked = False
    while(self.rotations % 3 != 0):
      self.rotate()
    self.rotations = 0