from slice import Slice

class TestSlice:
  def test_constructWithString(self):
    s = Slice('1,2,3')
    assert s.__len__() == 3
    assert s.__str__() == '1,2,3'

  def test_constructWithInt(self):
    s = Slice(1,2,3)
    assert s.__len__() == 3
    assert s.__str__() == '1,2,3'
  
  def test_rotate(self):
    s = Slice(1,2,3)
    s.rotate()
    assert s.__str__() == '3,1,2'
    s.rotate()
    assert s.__str__() == '2,3,1'
  
  def test_getitem(self):
    s = Slice(1,2,3)
    assert s[0] == 1
    assert s[1] == 2
    assert s[2] == 3
    s.rotate()
    assert s[0] == 3
    assert s[1] == 1
    assert s[2] == 2