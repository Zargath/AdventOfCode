def getWireCords(directions):
  path = [(0, 0)]
  currentLoc = (0, 0)
  for direction in directions:
    orientation = direction[:1]
    distance = int(direction[1:])

    newLoc = None
    if (orientation == 'U'):
      newLoc = (currentLoc[0], currentLoc[1] + distance)
    elif (orientation == 'D'):
      newLoc = (currentLoc[0], currentLoc[1] - distance)
    elif (orientation == 'L'):
      newLoc = (currentLoc[0] - distance, currentLoc[1])
    elif (orientation == 'R'):
      newLoc = (currentLoc[0] + distance, currentLoc[1])

    if (newLoc != None):
      path.append(newLoc)
      currentLoc = newLoc
  
  return path

def intersection(line1, line2):
  (x1, y1), (x2, y2) = line1
  (x3, y3), (x4, y4) = line2

  denominator = (x2 - x2) * (y4 - y3) - (x4 - x3) * (y2 - y1)
  if (denominator == 0):
    return None

  intersectX = (x2 * y1 - x1 * y2) * (x4 - x3) - (x4 * y3 - x3 * y4) * (x2 - x1) / denominator
  intersectY = (x2 * y1 - x1 * y2) * (y4 - y3) - (x4 * y3 - x3 * y4) * (y2 - y1) / denominator

  return (intersectX, intersectY)

with open("input.txt") as i:
  wire1 = getWireCords(i.readline().split(','))
  wire2 = getWireCords(i.readline().split(','))

print(intersection(((10, 10), (-10, -10)), ((1, 1), (2, 1))))
