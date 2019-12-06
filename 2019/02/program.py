from copy import copy

def readProgram():
  i = open("input.txt")
  program = i.readline().split(',')
  i.close()

  return [int(i) for i in program]

def run(input):
  address = 0
  while address < len(memory):
    opcode = memory[address]
    
    if opcode == 99:
      return memory[0]

    param1 = memory[memory[address+1]]
    param2 = memory[memory[address+2]]

    if opcode == 1:
      memory[memory[address+3]] = param1 + param2
    
    if opcode == 2:
      memory[memory[address+3]] = param1 * param2
    
    address += 4

program = readProgram()
memory = copy(program)

print(run(memory))

for param1 in range(0, 100):
  for param2 in range(0, 100):
    memory[1] = param1
    memory[2] = param2
    try:
      result = run(memory)
    except:
      result = 0

    if result == 19690720:
      print(f'Found! -- Param1: {param1} Param2: {param2}')
    else: 
      memory = copy(program)