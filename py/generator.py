import math

checker_list = []
puzzle_1_list = []

def generator_1(n):
  return int(1 + (math.floor(n * math.pi**11) % 30))

def isInvalidColor(color):
  count = len(filter(lambda cached: (True if cached == color else False), checker_list))
  return (True if count >= 3 else False)

for i in range(1, 91):
  n = i
  color = generator_1(n)
  while (isInvalidColor(color)):
    n += 1
    color = generator_1(n)
  checker_list.append(color)
  puzzle_1_list.append(color)

print(puzzle_1_list)