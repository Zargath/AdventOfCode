limits = (147981, 691423)
#limits = (100, 120)
pwds = []
for pwd in range(*limits):
  hasPair = False
  isInc = True
  spwd = str(pwd)
  for i, d in enumerate(spwd):
    if i + 1 < len(spwd):
      if spwd[i + 1] == spwd[i]:
        hasPair = True

      if int(spwd[i + 1]) < int(spwd[i]):
        isInc = False
    
  if hasPair and isInc:
    pwds.append(pwd)

print(len(pwds))