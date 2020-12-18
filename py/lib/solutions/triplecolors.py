from lib.slice import Slice
from lib.stack import Stack
from lib.solutions import bruteforce
from lib.circulararray import CircularArray

def solve(arr: CircularArray, colorRound='c'):
  upperBound = len(arr)
  for i in range(upperBound):
    arr.startingIndex = i
    temp = Stack()
    temp.push(arr[0])
    a = temp[0][0]
    b = temp[0][1]
    c = temp[0][2]
    for j in range(1, upperBound):
      if colorRound == 'c':
        if arr[j].hasColor(a) > -1 or arr[j].hasColor(b) > -1 or arr[j].hasColor(c) > -1:
          temp.push(arr[j])
      elif colorRound == 'b':
        if arr[j].hasColor(a) > -1 or arr[j].hasColor(b) > -1:
          temp.push(arr[j])
      elif colorRound == 'a':
        if arr[j].hasColor(a) > -1:
          temp.push(arr[j])
    if bruteforce.solve(temp) is False:
      print(temp)
      print(f'{len(temp)} {colorRound}')
      print('\n')
      if upperBound > len(temp):
        newArr = CircularArray()
        newArr.fromStack(temp)
        solve(newArr, chr(ord(colorRound)-1))
