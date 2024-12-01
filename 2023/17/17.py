import sys
from copy import copy
import heapq

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

parsed = []
for line in inputt:
    parsed.append([int(char) for char in line])

end = (len(parsed[0]) - 1, len(parsed) - 1)
queue = [(0, (0, 0), (0, 0))]
passed = set()
costs = {}
while queue:
    cost, pos, old_dir = heapq.heappop(queue)
    if (pos, old_dir) in passed:
        continue

    passed.add((pos, old_dir))

    if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(parsed[0]) or pos[1] >= len(parsed):
        continue

    if pos == end:
        print(cost)

    dir_to_test = [(0, 1), (0, -1)] if abs(old_dir[0]) == 1 else [(1, 0), (-1, 0)]
    if old_dir == (0, 0):
        dir_to_test = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for new_dir in dir_to_test:
        new_cost = cost
        for dist in range(1, 4):
            new_pos = (pos[0] + new_dir[0] * dist, pos[1] + new_dir[1] * dist)
            if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= len(parsed[0]) or new_pos[1] >= len(parsed):
                break

            new_cost += parsed[new_pos[1]][new_pos[0]]

            if new_cost >= costs.get((new_pos[0], new_pos[1], new_dir), 99999999):
                continue

            costs[(new_pos[0], new_pos[1], new_dir)] = new_cost
            heapq.heappush(queue, (new_cost, new_pos, new_dir))

print("----- PART 2 -----")

queue = [(0, (0, 0), (0, 0))]
passed = set()
costs = {}
while queue:
    cost, pos, old_dir = heapq.heappop(queue)
    if (pos, old_dir) in passed:
        continue

    passed.add((pos, old_dir))

    if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(parsed[0]) or pos[1] >= len(parsed):
        continue

    if pos == end:
        print(cost)

    dir_to_test = [(0, 1), (0, -1)] if abs(old_dir[0]) == 1 else [(1, 0), (-1, 0)]
    if old_dir == (0, 0):
        dir_to_test = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for new_dir in dir_to_test:
        new_cost = cost
        for dist in range(1, 11):
            new_pos = (pos[0] + new_dir[0] * dist, pos[1] + new_dir[1] * dist)
            if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= len(parsed[0]) or new_pos[1] >= len(parsed):
                break

            new_cost += parsed[new_pos[1]][new_pos[0]]

            if dist < 4:
                continue

            if new_cost >= costs.get((new_pos[0], new_pos[1], new_dir), 99999999):
                continue

            costs[(new_pos[0], new_pos[1], new_dir)] = new_cost
            heapq.heappush(queue, (new_cost, new_pos, new_dir))
