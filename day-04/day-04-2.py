from collections import defaultdict


def process_input(lines):
  lines.sort(key=lambda l: l.split(']'))

  sleep_by_min = {}  # guard: defaultdict(int) of 00:min to # of days asleep
  guard = None
  sleep_start = None
  for line in lines:
    time, action = line[1:].split('] ')
    if action[0] == 'G':
      guard = action.split(' ')[1]
      if guard not in sleep_by_min:
        sleep_by_min[guard] = defaultdict(int)
    elif action[0] == 'f':
      sleep_start = int(time[-2:])
    elif action[0] == 'w':
      wake = int(time[-2:])
      for i in range(sleep_start, wake):
        sleep_by_min[guard][i] += 1

  # Find minute across all guards with most days asleep.
  max_guard = None
  sleepiest_min = None
  max_days = 0
  for guard, min_to_days in sleep_by_min.items():
    for minute, days in min_to_days.items():
      if days > max_days:
        max_days = days
        sleepiest_min = minute
        max_guard = guard

  return int(max_guard[1:]) * sleepiest_min


if __name__ == '__main__':
  lines = [line.rstrip('\n') for line in open('day-04.input')]
  print(process_input(lines))
