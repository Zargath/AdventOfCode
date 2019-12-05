import math

def calculateFuel(mass):
  return math.floor(mass / 3) - 2

fuel = 0

i = open("./input.txt")
for mass in i:
  newFuel = calculateFuel(int(mass))
  fuelForFuel = newFuel
  while fuelForFuel > 0:
    fuelForFuel = calculateFuel(fuelForFuel)
    if fuelForFuel > 0:
      newFuel += fuelForFuel
  fuel += newFuel
i.close()

print(fuel)