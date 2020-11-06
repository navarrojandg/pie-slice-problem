from stack import Stack
from slice import Slice

def solve(stack: Stack):
  valid, badIndex = stack.isValid()
  if (not valid):
    for i in range(3):
      stack[badIndex].rotate()
      valid, badIndex = stack.isValid()
      if (valid):
        return solve(stack)
      else:
        if (i == 2):
          print(f'Invalid slice:\n [{badIndex}] {stack[badIndex]}')
          del stack[badIndex]
          return solve(stack)
  stack.print()

if __name__ == "__main__":
  solutionStack = Stack()
  solutionStack.push(Slice(1,2,3))
  solutionStack.push(Slice(1,2,3))
  solutionStack.push(Slice(1,2,3))
  solutionStack.push(Slice(2,1,3))
  solve(solutionStack)
