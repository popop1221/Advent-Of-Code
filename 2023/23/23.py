import sys
from copy import copy

sys.setrecursionlimit(5000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

parsed = []
for line in inputt:
    parsed.append([char for char in line])

parsed[0][1] = "#"
print(parsed)
print(len(parsed))
print(len(parsed[0]))

no_way = {"v": (0, -1), "^": (0, 1), ">": (-1, 0), "<": (1, 0)}
all_paths = []


def evaluate(pos, step_count, delta, path):
    if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(parsed[0]) or pos[0] >= len(parsed[1]):
        return 0, path

    if parsed[pos[1]][pos[0]] == "#":
        return 0, path

    if pos[1] == len(parsed) - 1 and pos[0] == len(parsed[0]) - 2:
        all_paths.append(step_count)
        print(max(all_paths))
        return step_count, path

    if pos in path:
        return 0, path

    if parsed[pos[1]][pos[0]] in "v^<>":
        if delta == no_way[parsed[pos[1]][pos[0]]]:
            return 0, path

    path.append(pos)

    return sorted([evaluate((pos[0] - 1, pos[1]), step_count + 1, (-1, 0), copy(path)),
                   evaluate((pos[0] + 1, pos[1]), step_count + 1, (1, 0), copy(path)),
                   evaluate((pos[0], pos[1] - 1), step_count + 1, (0, -1), copy(path)),
                   evaluate((pos[0], pos[1] + 1), step_count + 1, (0, 1), copy(path))], reverse=True)[0]


"""
start = (1, 1)
result, path = evaluate(start, 1, (0, 1), [])
print(result)

for pos in path:
    if parsed[pos[1]][pos[0]] == ".":
        parsed[pos[1]][pos[0]] = "O"

for line in parsed:
    print(line)

print(all_paths)
print(max(all_paths))"""

print("----- PART 2 -----")

for y in range(len(parsed)):
    for x in range(len(parsed)):
        if parsed[y][x] in "<>^v":
            parsed[y][x] = "."

graph = {}
for y in range(len(parsed)):
    for x in range(len(parsed[0])):
        if parsed[y][x] == "#":
            continue

        graph[(x, y)] = []

        for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 < dx + x < len(parsed[0]) and 0 < dy + y < len(parsed) and parsed[dy + y][dx + x] != "#":
                graph[(x, y)].append((dx + x, dy + y, 1))

print(graph)

while True:
    for node in graph:
        if len(graph[node]) == 2:
            prev = graph[node][0]
            next = graph[node][1]
            graph[(prev[0], prev[1])].append((next[0], next[1], next[2] + prev[2]))
            graph[(prev[0], prev[1])].remove((node[0], node[1], prev[2]))
            graph[(next[0], next[1])].append((prev[0], prev[1], prev[2] + next[2]))
            graph[(next[0], next[1])].remove((node[0], node[1], next[2]))
            graph.pop(node)
            break
    else:
        break

print(graph)
print(len(graph))

all_paths = []


def evaluate2(pos, step_count, path):
    if pos[1] == len(parsed) - 1 and pos[0] == len(parsed[0]) - 2:
        all_paths.append(step_count)
        print(max(all_paths))
        return step_count

    if pos in path:
        return 0

    path.append(pos)

    result = 0
    for next in graph[pos]:
        result = max(result, evaluate2((next[0], next[1]), step_count + next[2], copy(path)))
    return result


print(evaluate2((1, 1), 1, []))
