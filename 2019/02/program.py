import copy

i = open("input.txt")
program = i.readline().split(',')
i.close()

program = [int(i) for i in program]
memory = copy.copy(program)

address = 0
while address < len(memory):
  opcode = memory[address]
  
  if opcode == 99:
    print(memory[0])
    break

  param1 = memory[memory[address+1]]
  param2 = memory[memory[address+2]]

  if opcode == 1:
    memory[memory[address+3]] = param1 + param2
  
  if opcode == 2:
    memory[memory[address+3]] = param1 * param2
  
  address += 4