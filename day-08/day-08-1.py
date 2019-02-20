from collections import deque


def process_input(line):
  nums = list(map(int, line.split()))
  metadata_sum = [0]

  def process_tree_rec(index=0):
    num_children = nums[index]
    num_metadatas = nums[index + 1]

    last_index = index + 2
    for _ in range(num_children):
      last_index = process_tree_rec(last_index)

    for _ in range(num_metadatas):
      metadata_sum[0] += nums[last_index]
      last_index += 1

    return last_index

  process_tree_rec()
  return metadata_sum[0]


if __name__ == '__main__':
  line = [line.rstrip('\n') for line in open('day-08.input')]
  print(process_input(line[0]))
