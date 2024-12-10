import sys

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def evaluate(marked, x, y):
    # print(f"eval rec {x} {y}")

    if (x, y) not in marked and inputt[x][y] == "9":
        print(f"valid at {x} {y}")
        marked.append((x, y))
        return 1
    res = 0
    marked.append((x, y))
    for next_pos in dir:
        if x + next_pos[0] < 0 or y + next_pos[1] < 0 or x + next_pos[0] >= len(inputt) or y + next_pos[1] >= len(
                inputt):
            continue
        if (x + next_pos[0], y + next_pos[1]) in marked:
            continue
        if inputt[x + next_pos[0]][y + next_pos[1]] == "." or int(inputt[x + next_pos[0]][y + next_pos[1]]) != int(
                inputt[x][y]) + 1:
            continue
        res += evaluate(marked, x + next_pos[0], y + next_pos[1])
    return res


result = 0
for i in range(len(inputt)):
    for j in range(len(inputt[0])):
        if inputt[i][j] == "0":
            result += evaluate([], i, j)

print(result)

print("----- PART 2 -----")


def evaluate_2(x, y):
    if inputt[x][y] == "9":
        return 1
    res = 0
    for next_pos in dir:
        if x + next_pos[0] < 0 or y + next_pos[1] < 0 or x + next_pos[0] >= len(inputt) or y + next_pos[1] >= len(
                inputt):
            continue
        if inputt[x + next_pos[0]][y + next_pos[1]] == "." or int(inputt[x + next_pos[0]][y + next_pos[1]]) != int(
                inputt[x][y]) + 1:
            continue
        res += evaluate_2(x + next_pos[0], y + next_pos[1])
    return res


result = 0
for i in range(len(inputt)):
    for j in range(len(inputt[0])):
        if inputt[i][j] == "0":
            result += evaluate_2(i, j)

print(result)
