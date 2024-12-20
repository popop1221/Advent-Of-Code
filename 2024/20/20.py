import heapq
import sys

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

queue = [(0, start)]
marked = set()
costs_res = []
costs = {}

while queue:  # day 16
    cost, pos = heapq.heappop(queue)
    if pos in marked:
        continue
    marked.add(pos)
    if inputt[pos[0]][pos[1]] == "#":
        continue
    if pos == end:
        costs_res.append(cost)
    costs[pos] = min(costs[pos], cost) if pos in costs.keys() else cost

    for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        heapq.heappush(queue, ((cost + 1), (pos[0] + dir[0], pos[1] + dir[1])))

default = min(costs_res)
print(f"Default value {default}")
"""
temp = []
for i in range(len(inputt)):
    for j in range(len(inputt[0])):
        if inputt[i][j] != '#':
            continue
        print(f"{i} {j}")
        queue = [(0, start)]
        marked = set()
        costs_res = []
        costs = {}

        while queue:  # day 16
            cost, pos = heapq.heappop(queue)
            if pos in marked:
                continue
            marked.add(pos)
            costs[pos] = min(costs[pos], cost) if pos in costs.keys() else cost
            if inputt[pos[0]][pos[1]] == "#" and (i, j) != pos:
                continue
            if pos == end:
                costs_res.append(cost)

            for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if pos[0] + dir[0] < 0 or pos[0] + dir[0] >= len(inputt) or pos[1] + dir[1] < 0 or pos[1] + dir[
                    1] >= len(
                        inputt[0]):
                    continue
                heapq.heappush(queue, ((cost + 1), (pos[0] + dir[0], pos[1] + dir[1])))
        if min(costs_res) != default:
            temp.append((min(costs_res), (i, j)))


print(temp)
print(len(temp))
result = [0 for _ in range(default)]
result2 = 0
for cheat in temp:
    result[default - cheat[0]] += 1
for i in range(len(result)):
    if result[i] != 0:
        print(f"{i} -> {result[i]}")
    if i >= 100:
        result2 += result[i]
print(result2)
"""

print("----- PART 2 -----")

print(costs)
print(len(costs))

result = set()
temp = [0 for _ in range(default + 1)]
for (i, j) in costs.keys():
    for (i2, j2) in costs.keys():
        if abs(i2 - i) + abs(j2 - j) > 20:
            continue
        if costs[(i, j)] - costs[(i2, j2)] - (abs(i2 - i) + abs(j2 - j)) >= 100:
            if ((i, j), (i2, j2)) not in result:
                temp[costs[(i, j)] - costs[(i2, j2)] - (abs(i2 - i) + abs(j2 - j))] += 1
            result.add(((i, j), (i2, j2)))

for i in range(len(temp)):
    if temp[i] == 0:
        continue
    print(f"{i} -> {temp[i]}")
print(result)
print(len(result))
