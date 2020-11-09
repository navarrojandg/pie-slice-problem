from lib.stack import Stack
from lib.slice import Slice

class TestStack:
  def test_constructs(self):
    s = Stack()
    s1 = Slice(1,2,3)
    s.push(s1)
    assert s[0] == s1
    assert isinstance(s[0], Slice)
    assert s[0].__str__() == '1,2,3 R0'
  
  def test_pop(self):
    s = Stack()
    s.push(Slice(1,2,3))
    assert s.pop().__str__() == '1,2,3 R0'
    assert s.__len__() == 0

  def test_validate(self):
    s = Stack()
    s.push(Slice(1,2,3))
    s.push(Slice(3,4,5))
    assert s.isValid()
  
  def test_iter(self):
    s = Stack()
    s.push(Slice(1,2,3))