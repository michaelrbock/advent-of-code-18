def process_input(polymer):
  min_len = float('inf')
  for i in range(ord('a'), ord('z') + 1):
    skip = chr(i)
    stack = []
    for char in polymer:
      if char.lower() == skip:
        continue
      elif not stack:
        stack.append(char)
      elif stack[-1].lower() == char.lower() and stack[-1] != char:
        stack.pop()
      else:
        stack.append(char)
    if len(stack) < min_len:
      min_len = len(stack)
  return min_len


if __name__ == '__main__':
  line = [line.rstrip('\n') for line in open('day-05.input')]
  print(process_input(line[0]))
