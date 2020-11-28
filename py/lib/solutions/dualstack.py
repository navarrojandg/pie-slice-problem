from lib.slice import Slice
from lib.stack import Stack
from typing import Dict
import os
import json

def stacksFromFile(filename) -> Dict[str, Stack]:
  dirname = os.path.dirname(os.path.realpath('__file__'))
  filepath = os.path.join(dirname, filename)
  
  with open(filepath) as f:
    dataset = json.load(f)
    return {
      'one': Stack().fromArray(dataset['one']),
      'two': Stack().fromArray(dataset['two']),
      'three': Stack().fromArray(dataset['three']),
      'four': Stack().fromArray(dataset['four'])
    }

def stackSliceAndValidate(_slice: Slice, _stack: Stack):
  _stack.push(_slice)
  validStack = _stack.validate()

  while(_slice.rotations < 3 and not validStack):
    validStack = rotateSliceAndValidate(_slice, _stack)
  
  return validStack
  
def rotateSliceAndValidate(_slice:Slice, _stack:Stack):
  _slice.rotate()
  return _stack.validate()

def allOfStackChecked(stack: Stack):
  return all(map(lambda s: s.checked, stack))

def solve(stack: Stack) -> Stack:
  solutionStack = Stack()
  solutionStack.push(stack.pop())

  while(not allOfStackChecked(stack)):
    validStack = stackSliceAndValidate(stack.pop(), solutionStack)
    if not validStack:
      _slice = solutionStack.pop(0)
      _slice.checked = True
      stack.push(_slice)

  print('Dual Stack Solution')
  print(solutionStack)
  print('\nDual Stack Obstacles')
  print(stack)
  print('\n')