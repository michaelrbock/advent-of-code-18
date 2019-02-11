def freq(changes):
  total = 0
  for change in changes:
    total += change
  return total


lines = [line.rstrip('\n') for line in open('day-01.input')]
changes = [int(x) for x in lines]
print(freq(changes))
