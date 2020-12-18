from lib.slice import Slice
from lib.stack import Stack
from lib.solutions import bruteforce
from lib.circulararray import CircularArray

def solve(arr: CircularArray, colorRound='c') -> CircularArray:
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

def run(stack: Stack) -> Stack:
  upperBound = len(stack)
  for i in range(len(stack)):
    copy = stack.copy()
    tempStack = Stack()
    tempStack.push(copy.pop(i))
    a = tempStack[0][0]
    for j in range(len(copy)):
      if copy[j].hasColor(a) > -1:
        tempStack.push(copy[j])
    if bruteforce.solve(tempStack) is False:
      if upperBound > len(tempStack):
        run(tempStack)
      else:
        print(tempStack)
        print(len(tempStack))
        print('\n')
  
  for i in range(len(stack)):
    copy = stack.copy()
    tempStack = Stack()
    tempStack.push(copy.pop(i))
    a = tempStack[0][0]
    b = tempStack[0][1]
    for j in range(len(copy)):
      if copy[j].hasColor(a) > -1 or copy[j].hasColor(b) > -1:
        tempStack.push(copy[j])
    if bruteforce.solve(tempStack) is False:
      if upperBound > len(tempStack):
        run(tempStack)
      else:
        print(tempStack)
        print(len(tempStack))
        print('\n')

  for i in range(len(stack)):
    copy = stack.copy()
    tempStack = Stack()
    tempStack.push(copy.pop(i))
    a = tempStack[0][0]
    b = tempStack[0][1]
    c = tempStack[0][2]
    for j in range(len(copy)):
      if copy[j].hasColor(a) > -1 or \
         copy[j].hasColor(b) > -1 or \
         copy[j].hasColor(c) > -1:
        tempStack.push(copy[j])
    if bruteforce.solve(tempStack) is False:
      if upperBound > len(tempStack):
        run(tempStack)
      else:
        print(tempStack)
        print(len(tempStack))
        print('\n')

    