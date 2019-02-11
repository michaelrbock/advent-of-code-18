from collections import Counter


def diff_words(word1, word2):
  diff = 0
  res = []
  for i in range(len(word1)):
    if word1[i] != word2[i]:
      diff += 1
      if diff > 1:
        return
    else:
      res.append(word1[i])
  return ''.join(res)


def process_input(lines):
  for i, word1 in enumerate(lines):
    for j, word2 in enumerate(lines):
      if i == j:
        continue
      res = diff_words(word1, word2)
      if res:
        return res


if __name__ == '__main__':
  lines = [line.rstrip('\n') for line in open('day-02.input')]
  print(process_input(lines))
