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
    parsed.append([t for t in line])

print(parsed)

passed = set()


def evaluate(dir, pos, grid, marked):
    if pos[1] < 0 or pos[0] < 0 or pos[1] >= len(grid) or pos[0] >= len(grid[0]):
        return

    if (dir[0], dir[1], pos[0], pos[1]) in passed:
        return

    passed.add((dir[0], dir[1], pos[0], pos[1]))
    marked[pos[1]][pos[0]] = True

    if grid[pos[1]][pos[0]] == ".":
        evaluate(dir, [pos[0] + dir[0], pos[1] + dir[1]], grid, marked)
        return

    if grid[pos[1]][pos[0]] == "/":
        if dir == (0, 1):
            evaluate((-1, 0), [pos[0] - 1, pos[1]], grid, marked)
        elif dir == (0, -1):
            evaluate((1, 0), [pos[0] + 1, pos[1]], grid, marked)
        elif dir == (1, 0):
            evaluate((0, -1), [pos[0], pos[1] - 1], grid, marked)
        elif dir == (-1, 0):
            evaluate((0, 1), [pos[0], pos[1] + 1], grid, marked)

    if grid[pos[1]][pos[0]] == "\\":
        if dir == (0, 1):
            evaluate((1, 0), [pos[0] + 1, pos[1]], grid, marked)
        elif dir == (0, -1):
            evaluate((-1, 0), [pos[0] - 1, pos[1]], grid, marked)
        elif dir == (1, 0):
            evaluate((0, 1), [pos[0], pos[1] + 1], grid, marked)
        elif dir == (-1, 0):
            evaluate((0, -1), [pos[0], pos[1] - 1], grid, marked)

    if grid[pos[1]][pos[0]] == "-":
        if dir == (0, 1) or dir == (0, -1):
            evaluate((1, 0), [pos[0] + 1, pos[1]], grid, marked)
            evaluate((-1, 0), [pos[0] - 1, pos[1]], grid, marked)
        else:
            evaluate(dir, [pos[0] + dir[0], pos[1] + dir[1]], grid, marked)

    if grid[pos[1]][pos[0]] == "|":
        if dir == (1, 0) or dir == (-1, 0):
            evaluate((0, 1), [pos[0], pos[1] + 1], grid, marked)
            evaluate((0, -1), [pos[0], pos[1] - 1], grid, marked)
        else:
            evaluate(dir, [pos[0] + dir[0], pos[1] + dir[1]], grid, marked)


marked = [[False for _ in range(len(parsed[0]))] for _ in range(len(parsed))]
evaluate((1, 0), [0, 0], parsed, marked)
print(marked)

result = 0
for line in marked:
    for elem in line:
        if elem:
            result += 1
print(result)

print("----- PART 2 -----")

result = 0
tested = set()
for i in range(len(parsed)):
    for dir_x, dir_y, start_x, start_y in [(1, 0, 0, i), (-1, 0, len(parsed) - 1, i), (0, 1, i, 0),
                                           (0, -1, i, len(parsed) - 1)]:
        tested.add((dir_x, dir_y, start_x, start_y))
        marked = [[False for _ in range(len(parsed[0]))] for _ in range(len(parsed))]
        passed = set()
        evaluate((dir_x, dir_y), [start_x, start_y], parsed, marked)
        temp = 0
        for line in marked:
            for elem in line:
                if elem:
                    temp += 1
        result = max(result, temp)

print(len(tested))
print(result)
