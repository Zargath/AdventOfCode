i = open("input.txt")
program = i.readline().split(',')
i.close()

program = [int(i) for i in program]

index = 0
while index < len(program):
  instruction = program[index]
  
  if instruction == 99:
    print(program[0])
    break

  val1 = program[program[index+1]]
  val2 = program[program[index+2]]

  if instruction == 1:
    program[program[index+3]] = val1 + val2
  
  if instruction == 2:
    program[program[index+3]] = val1 * val2
  
  index += 4