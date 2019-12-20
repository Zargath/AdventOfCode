def getWireCords(directions):
  x = 0
  y = 0
  steps = 0
  path = {}
  dx = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
  dy = {'L': 0, 'R': 0, 'U': 1, 'D': -1}
  for direction in directions:
    cmd = direction[:1]
    distance = int(direction[1:])
    assert cmd in ['L', 'R', 'U', 'D']
    for _ in range(distance):
      steps += 1
      x += dx[cmd]
      y += dy[cmd]
      if (x ,y) not in path:
        path[(x, y)] = steps
  
  return path

with open("input.txt") as i:
  a, b, _ = i.read().split('\n')
  a, b = [x.split(',') for x in [a, b]]

  pathA = getWireCords(a)
  pathB = getWireCords(b)

  #both = pathA & pathB
  #print(f'Part 1: {min([x + y for (x, y) in both])}')

  both = pathA.keys() & pathB.keys()
  print(f'Part 1: {min([pathA[k] + pathB[k] for k in both])}')