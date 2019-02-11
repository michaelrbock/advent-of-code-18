def first_dupe(changes):
  seen = set()
  total = 0
  while True:
    for change in changes:
      total += change
      if total in seen:
        return total
      seen.add(total)


lines = [line.rstrip('\n') for line in open('day-01.input')]
changes = [int(x) for x in lines]
print(first_dupe(changes))
