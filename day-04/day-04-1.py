from collections import defaultdict


def process_input(lines):
  lines.sort(key=lambda l: l.split(']'))

  sleep_total = defaultdict(int)  # guard: total sleep minutes
  sleep_by_min = {}  # guard: defaultdict(int) of 00:min to # of times asleep
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
      sleep_total[guard] += wake - sleep_start
      for i in range(sleep_start, wake):
        sleep_by_min[guard][i] += 1

  max_guard = None
  max_sleep_mins = 0
  for guard, sleep_mins in sleep_total.items():
    if sleep_mins > max_sleep_mins:
      max_sleep_mins = sleep_mins
      max_guard = guard

  # Find minute with most days.
  sleepiest_min = None
  max_days = 0
  for minute, days in sleep_by_min[max_guard].items():
    if days > max_days:
      max_days = days
      sleepiest_min = minute

  return int(max_guard[1:]) * sleepiest_min


if __name__ == '__main__':
  lines = [line.rstrip('\n') for line in open('day-04.input')]
  print(process_input(lines))