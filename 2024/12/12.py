import sys

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

parsed = []
for line in inputt:
    temp = []
    for char in line:
        temp.append(char)
    parsed.append(temp)

next_dir = (1, 0)


def evaluate(i, j, id, marked, borders):
    if i < 0 or j < 0 or i >= len(parsed) or j >= len(parsed[0]) or parsed[i][j] != id:
        if (i, j) in marked:
            return (0, 0)
        borders.append((i, j))
        return (0, 1)
    parsed[i][j] = '.'
    marked.append((i, j))
    values = [evaluate(i + dx, j + dy, id, marked, borders) for (dx, dy) in [(-1, 0), (0, -1), (1, 0), (0, 1)]]
    area = 1 + values[0][0] + values[1][0] + values[2][0] + values[3][0]
    perimeter = values[0][1] + values[1][1] + values[2][1] + values[3][1]
    return area, perimeter


result = 0
groups = []
for i in range(len(parsed)):
    for j in range(len(parsed[0])):
        if parsed[i][j] == '.':
            continue
        marked = []
        borders = []
        print(f"Eval : {parsed[i][j]}")
        temp = evaluate(i, j, parsed[i][j], marked, borders)
        groups.append(marked)
        if temp != 0:
            print(temp)
            """
            for ii in range(len(parsed) + 1):
                for jj in range(len(parsed[0]) + 1):
                    if (ii -1, jj-1) in debug:
                        print("#", end='')
                    else:
                        print("." if i == 0 or jj == 0 else parsed[ii - 1][jj - 1], end='')
                print()"""
        print(borders)
        result += temp[0] * temp[1]
        # result2 += temp[0] * len(part2)

print(result)

print("----- PART 2 -----")

result = 0
for group in groups:
    sides = 0
    print(group)
    for mark in group:
        for (dx, dy) in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
            if (mark[0] + dx, mark[1] + dy) in group and (mark[0] + dx, mark[1]) in group and (
            mark[0], mark[1] + dy) in group:
                continue
            if (mark[0] + dx, mark[1]) in group and (mark[0], mark[1] + dy) in group:
                print(f"From {mark} 1 with {dx}  {dy}")
                sides += 1
            if (mark[0] + dx, mark[1]) not in group and (mark[0], mark[1] + dy) not in group:
                print(f"From {mark} 2 with {dx}  {dy}")
                sides += 1
    print(sides)
    result += sides * len(group)

print(result)
