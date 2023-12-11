import sys
from matplotlib.path import Path

sys.setrecursionlimit(150000)

# Definitely need to redo this one in a cleaner way.

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()


inputt = real_input
parsed = []
x_start, y_start = 0, 0

y_temp = 0
for line in inputt:
    line = line.replace("\n", "")
    temp = [t for t in line]
    if 'S' in temp:
        y_start = y_temp
        x_start = temp.index('S')
    parsed.append(temp)
    y_temp += 1
print(f"Start : {x_start} {y_start}")

marked = [[False for _ in range(len(parsed[0]))] for _ in range(len(parsed))]
queue = [(x_start, y_start, 'S', 0)]
result = 0
while queue != []:
    elem = queue.pop(0)
    if marked[elem[1]][elem[0]]:
        continue
    marked[elem[1]][elem[0]] = True

    if parsed[elem[1]][elem[0]] == "S":
        if elem[1] > 0 and parsed[elem[1] - 1][elem[0]] in "F|7":
            queue.append((elem[0], elem[1] - 1, 'S', 1))
        if elem[1] < len(parsed) - 1 and parsed[elem[1] + 1][elem[0]] in "|LJ":
            queue.append((elem[0], elem[1] + 1, 'N', 1))
        if elem[0] > 0 and parsed[elem[1]][elem[0] - 1] in "-FL":
            queue.append((elem[0] - 1, elem[1], 'E', 1))
        if elem[0] < len(parsed[0]) - 1 and parsed[elem[1]][elem[0] + 1] in "-7J":
            queue.append((elem[0] + 1, elem[1], 'W', 1))

    if parsed[elem[1]][elem[0]] == "|":
        result = max(result, elem[3])
        if elem[2] == "N":
            queue.append((elem[0], elem[1] + 1, "N", elem[3] + 1))
        else:
            queue.append((elem[0], elem[1] - 1, "S", elem[3] + 1))

    if parsed[elem[1]][elem[0]] == "-":
        result = max(result, elem[3])
        if elem[2] == "W":
            queue.append((elem[0] + 1, elem[1], "W", elem[3] + 1))
        else:
            queue.append((elem[0] - 1, elem[1], "E", elem[3] + 1))

    if parsed[elem[1]][elem[0]] == "L":
        result = max(result, elem[3])
        if elem[2] == "N":
            queue.append((elem[0] + 1, elem[1], "W", elem[3] + 1))
        else:
            queue.append((elem[0], elem[1] - 1, "S", elem[3] + 1))

    if parsed[elem[1]][elem[0]] == "J":
        result = max(result, elem[3])
        if elem[2] == "N":
            queue.append((elem[0] - 1, elem[1], "E", elem[3] + 1))
        else:
            queue.append((elem[0], elem[1] - 1, "S", elem[3] + 1))

    if parsed[elem[1]][elem[0]] == "7":
        result = max(result, elem[3])
        if elem[2] == "S":
            queue.append((elem[0] - 1, elem[1], "E", elem[3] + 1))
        else:
            queue.append((elem[0], elem[1] + 1, "N", elem[3] + 1))
    if parsed[elem[1]][elem[0]] == "F":
        result = max(result, elem[3])
        if elem[2] == "S":
            queue.append((elem[0] + 1, elem[1], "W", elem[3] + 1))
        else:
            queue.append((elem[0], elem[1] + 1, "N", elem[3] + 1))
print(result)

print("----- PART 2 -----")
part2v2 = []
marked = [[False for _ in range(len(parsed[0]))] for _ in range(len(parsed))]
queue = [(x_start, y_start, 'S', 0)]
while queue != []:
    elem = queue.pop()
    if marked[elem[1]][elem[0]]:
        continue
    marked[elem[1]][elem[0]] = True
    part2v2.append((elem[0], elem[1]))

    if parsed[elem[1]][elem[0]] == "S":
        if elem[1] > 0 and parsed[elem[1] - 1][elem[0]] in "F|7":
            queue.append((elem[0], elem[1] - 1, 'S', 1))
        if elem[1] < len(parsed) - 1 and parsed[elem[1] + 1][elem[0]] in "|LJ":
            queue.append((elem[0], elem[1] + 1, 'N', 1))
        if elem[0] > 0 and parsed[elem[1]][elem[0] - 1] in "-FL":
            queue.append((elem[0] - 1, elem[1], 'E', 1))
        if elem[0] < len(parsed[0]) - 1 and parsed[elem[1]][elem[0] + 1] in "-7J":
            queue.append((elem[0] + 1, elem[1], 'W', 1))

    if parsed[elem[1]][elem[0]] == "|":
        result = max(result, elem[3])
        if elem[2] == "N":
            queue.append((elem[0], elem[1] + 1, "N", elem[3] + 1))
        else:
            queue.append((elem[0], elem[1] - 1, "S", elem[3] + 1))

    if parsed[elem[1]][elem[0]] == "-":
        result = max(result, elem[3])
        if elem[2] == "W":
            queue.append((elem[0] + 1, elem[1], "W", elem[3] + 1))
        else:
            queue.append((elem[0] - 1, elem[1], "E", elem[3] + 1))

    if parsed[elem[1]][elem[0]] == "L":
        result = max(result, elem[3])
        if elem[2] == "N":
            queue.append((elem[0] + 1, elem[1], "W", elem[3] + 1))
        else:
            queue.append((elem[0], elem[1] - 1, "S", elem[3] + 1))

    if parsed[elem[1]][elem[0]] == "J":
        result = max(result, elem[3])
        if elem[2] == "N":
            queue.append((elem[0] - 1, elem[1], "E", elem[3] + 1))
        else:
            queue.append((elem[0], elem[1] - 1, "S", elem[3] + 1))

    if parsed[elem[1]][elem[0]] == "7":
        result = max(result, elem[3])
        if elem[2] == "S":
            queue.append((elem[0] - 1, elem[1], "E", elem[3] + 1))
        else:
            queue.append((elem[0], elem[1] + 1, "N", elem[3] + 1))
    if parsed[elem[1]][elem[0]] == "F":
        result = max(result, elem[3])
        if elem[2] == "S":
            queue.append((elem[0] + 1, elem[1], "W", elem[3] + 1))
        else:
            queue.append((elem[0], elem[1] + 1, "N", elem[3] + 1))

poly = Path(part2v2)
result = 0
for y in range(len(marked)):
    for x in range(len(marked[0])):
        if not marked[y][x]:
            result += poly.contains_point((x, y))

print(f"part2 v2 result : {result}")


def evaluate(start_x, start_y, res):
    if start_x < 0 or start_y < 0 or start_x >= len(marked) or start_y >= len(marked):
        res[3] = True
        return
    if marked[start_y][start_x]:
        return
    res[2] += 1
    marked[start_y][start_x] = True
    evaluate(start_x - 1, start_y, res)
    evaluate(start_x + 1, start_y, res)
    evaluate(start_x, start_y - 1, res)
    evaluate(start_x, start_y + 1, res)


connexed = []
for y in range(len(marked)):
    for x in range(len(marked[0])):
        if marked[y][x]:
            continue
        res = [x, y, 0, False]
        evaluate(x, y, res)
        if res[2] == 0:
            continue
        connexed.append(res)

print(connexed)
result = 0
for conx in connexed:
    if not conx[3]:
        result += conx[2]
print(result)
