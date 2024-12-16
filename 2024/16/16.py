import heapq
import sys
from copy import copy

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

start = (0, 0)
end = (0, 0)
for i in range(len(inputt)):
    for j in range(len(inputt[0])):
        if inputt[i][j] == "S":
            start = (i, j)
        if inputt[i][j] == "E":
            end = (i, j)

print(start)
print(end)

queue = [(0, start, (0, 1), [])]
marked = set()
costs_res = []
costs = {}

while queue:  # 2023, day 17
    cost, pos, dir, path = heapq.heappop(queue)
    if (pos, dir) in marked:
        continue
    marked.add((pos, dir))
    costs[(pos, dir)] = min(costs[(pos, dir)], cost) if (pos, dir) in costs.keys() else cost
    if inputt[pos[0]][pos[1]] == "#":
        continue
    if pos == end:
        costs_res.append(cost)

    path.append(pos)
    heapq.heappush(queue, ((cost + 1), (pos[0] + dir[0], pos[1] + dir[1]), dir, copy(path)))

    if dir == (0, 1):
        temp = [(1000, (1, 0)), (1000, (-1, 0)), (2000, (0, -1))]
    elif dir == (0, -1):
        temp = [(1000, (1, 0)), (1000, (-1, 0)), (2000, (0, 1))]
    elif dir == (1, 0):
        temp = [(2000, (-1, 0)), (1000, (0, 1)), (1000, (0, -1))]
    else:  # dir == (-1, 0)
        temp = [(2000, (1, 0)), (1000, (0, 1)), (1000, (0, -1))]

    for to_test in temp:
        heapq.heappush(queue, (cost + to_test[0], pos, to_test[1], copy(path)))

print(min(costs_res))

print("----- PART 2 -----")

part1 = min(costs_res)
result = set()
queue = [temp for temp in costs.keys() if costs[temp] == part1 and temp[0] == end]
while queue:
    pos, dir = queue.pop(0)
    cost = costs[(pos, dir)]
    next_pos = (pos[0] - dir[0], pos[1] - dir[1])
    if inputt[next_pos[0]][next_pos[1]] != "#":
        if (next_pos, dir) in marked and costs[(next_pos, dir)] == cost - 1 and (next_pos, dir) not in result:
            result.add(next_pos)
            queue.append((next_pos, dir))
    if dir == (0, 1):
        temp = [(1000, (1, 0)), (1000, (-1, 0)), (2000, (0, -1))]
    elif dir == (0, -1):
        temp = [(1000, (1, 0)), (1000, (-1, 0)), (2000, (0, 1))]
    elif dir == (1, 0):
        temp = [(2000, (-1, 0)), (1000, (0, 1)), (1000, (0, -1))]
    else:  # dir == (-1, 0)
        temp = [(2000, (1, 0)), (1000, (0, 1)), (1000, (0, -1))]
    for new_dir in temp:
        if (pos, new_dir[1]) in marked and costs[(pos, new_dir[1])] == cost - new_dir[0] and (pos, new_dir[1]) not in result:
            print(f"Enqueue new dir {(pos, new_dir[1])}")
            result.add(pos)
            queue.append((pos, new_dir[1]))

print(result)
for i in range(len(inputt)):
    line = ""
    for j in range(len(inputt)):
        if (i, j) in result:
            line += "O"
        else:
            line += inputt[i][j]
    print(line)

print(len(result) + 1)
