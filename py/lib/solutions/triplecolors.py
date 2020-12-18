from lib.slice import Slice
from lib.stack import Stack
from lib.solutions import bruteforce

def run(stack: Stack) -> Stack:
  for i in range(len(stack)):
    copy = stack.copy()
    tempStack = Stack()
    tempStack.push(copy.pop(i))
    a = tempStack[0][0]
    for j in range(len(copy)):
      if copy[j].hasColor(a) > -1:
        tempStack.push(copy[j])
    if bruteforce.solve(tempStack) is False:
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
      print(tempStack)
      print(len(tempStack))
      print('\n')

    