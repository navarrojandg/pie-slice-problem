from lib.slice import Slice
from lib.solutions import bruteforce
from lib.circulararray import CircularArray

colorSubset = {
  'a': [
    [1,0,0]
  ],
  'ab': [
    [1,0,0],
    [0,1,0],
    [1,1,0],
  ],
  'abc': [
    [1,0,0],
    [0,1,0],
    [1,1,0],
    [0,0,1],
    [1,0,1],
    [0,1,1],
    [1,1,1],
  ]
}

taskQueue = []

def solve(arr: CircularArray):
  getAndEnqueueSubset('abc', arr)
  processQueue()

def getAndEnqueueSubset(subset, arr: CircularArray):
  for i in range(len(arr)):
    arr.startingIndex = i
    temp = getSubsetFromArray(subset, arr)
    if temp is not None:
      taskQueue.append((subset, temp))

def processQueue():
  while len(taskQueue) > 0:
    task = taskQueue.pop()
    currRound = task[0]
    currArr = task[1]
    if bruteforce.solve(currArr) is False:
      if currRound == 'abc':
        getAndEnqueueSubset('ab', currArr)
      if currRound == 'ab':
        print(currArr)
        print(f'{len(currArr)} {currRound}\n')
        getAndEnqueueSubset('a', currArr)
      if currRound == 'a':
        print(currArr)
        print(f'{len(currArr)} {currRound}\n')

def getSubsetFromArray(subset, arr: CircularArray) -> CircularArray:
  upperBound = len(arr)
  a = arr[0][0]
  b = arr[0][1]
  c = arr[0][2]
  temp = CircularArray()
  temp.append(arr[0])
  for j in range(1, upperBound):
    for p in colorSubset[subset]:
      n = [
        p[0] * a,
        p[1] * b,
        p[2] * c,
      ]
      if arr[j].hasColorConfig(n):
        temp.append(arr[j])
        break
  if len(temp) < upperBound:
    return temp