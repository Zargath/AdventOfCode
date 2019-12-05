import math

fuel = 0

i = open("./input.txt")
for mass in i:
  fuel += math.floor(int(mass) / 3) - 2
i.close()

print(fuel)