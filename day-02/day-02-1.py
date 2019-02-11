from collections import Counter


def process_word(word):
  """Returns tuple of {0,1},{0,1} where the first number represents if there are
  any letters repeated exactly twice and the second if any letters are repeated
  exactly three times."""
  twice = 0
  thrice = 0
  for _, count in Counter(word).items():
    if count == 2:
      twice = 1
    elif count == 3:
      thrice = 1
  return twice, thrice


def process_input(lines):
  twices = 0
  thrices = 0
  for word in lines:
    result = process_word(word)
    twices += result[0]
    thrices += result[1]
  return twices * thrices


if __name__ == '__main__':
  lines = [line.rstrip('\n') for line in open('day-02.input')]
  print(process_input(lines))
