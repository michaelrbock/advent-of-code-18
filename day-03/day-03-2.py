from collections import defaultdict


def add_to(grid, col, row, width, height, claim):
  for r in range(row, row + height):
    for c in range(col, col + width):
      grid[r][c].add(claim)


def process_input(lines):
  grid = [[set() for _ in range(1000)] for _ in range(1000)]
  for line in lines:
    claim, data = line.split('@ ')
    coords, size = data.split(': ')
    col, row = map(int, coords.split(','))
    width, height = map(int, size.split('x'))
    add_to(grid, col, row, width, height, claim)

  shares = defaultdict(int)  # claim id to how many it shares with
  for row in grid:
    for cell in row:
      for claim in cell:
        shares[claim] += len(cell) - 1

  for claim, count in shares.items():
    if count == 0:
      return claim


if __name__ == '__main__':
  lines = [line.rstrip('\n') for line in open('day-03.input')]
  print(process_input(lines))
