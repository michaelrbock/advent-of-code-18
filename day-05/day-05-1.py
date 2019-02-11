def process_input(polymer):
  stack = []
  for char in polymer:
    if not stack:
      stack.append(char)
    elif stack[-1].lower() == char.lower() and stack[-1] != char:
      stack.pop()
    else:
      stack.append(char)
  return len(stack)


if __name__ == '__main__':
  line = [line.rstrip('\n') for line in open('day-05.input')]
  print(process_input(line[0]))
