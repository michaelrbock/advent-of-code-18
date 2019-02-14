from collections import defaultdict
import heapq


def process_line(incoming, outgoing, line):
  first, second = line.split()[1], line.split()[7]
  incoming[second].add(first)
  outgoing[first].append(second)


def process_input(lines):
  """Topological sort."""
  incoming = defaultdict(set)  # Node: set{Nodes incoming}
  outgoing = defaultdict(list) # Node: [Nodes outgoing]
  for line in lines:
    process_line(incoming, outgoing, line)

  result = []

  # Find nodes with no incoming, add to priority queue.
  pq = []
  for node in outgoing:
    if node not in incoming:
      heapq.heappush(pq, node)

  while pq:
    curr = heapq.heappop(pq)
    result.append(curr)
    for child in outgoing[curr]:
      incoming[child].remove(curr)
      if len(incoming[child]) == 0:
        heapq.heappush(pq, child)

  return ''.join(result)


if __name__ == '__main__':
  lines = [line.rstrip('\n') for line in open('day-06.input')]
  print(process_input(lines))
