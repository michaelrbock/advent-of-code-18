def add_to(grid, col, row, width, height):
  for r in range(row, row + height):
    for c in range(col, col + width):
      grid[r][c] += 1


def process_input(lines):
  grid = [[0] * 1000 for _ in range(1000)]
  for line in lines:
    _, data = line.split('@ ')
    coords, size = data.split(': ')
    col, row = map(int, coords.split(','))
    width, height = map(int, size.split('x'))
    add_to(grid, col, row, width, height)

  count = 0
  for row in grid:
    for cell in row:
      if cell >= 2:
        count += 1
  return count


if __name__ == '__main__':
  lines = [line.rstrip('\n') for line in open('day-03.input')]
  print(process_input(lines))
