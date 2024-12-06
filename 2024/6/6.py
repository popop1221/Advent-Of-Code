import sys
from copy import copy

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

parsed = []
guard_start = (0, 0)
for i in range(len(inputt)):
    parse = []
    for j in range(len(inputt)):
        if inputt[i][j] == '^':
            guard_start = (i, j)
            parse.append(['.', []])
        else:
            parse.append([inputt[i][j], []])
    parsed.append(parse)

print(parsed)
print(guard_start)
print("-----")

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
next_move = (-1, 0)
guard = guard_start
while next_move not in parsed[guard[0]][guard[1]][1]:
    if guard[0] + next_move[0] < 0 or guard[1] + next_move[1] < 0 or guard[0] + next_move[0] >= len(parsed) or guard[
        1] + next_move[1] >= len(parsed[0]):
        print("exit map")
        parsed[guard[0]][guard[1]][1].append(next_move)
        break
    if parsed[guard[0] + next_move[0]][guard[1] + next_move[1]][0] == '#':
        print("if")
        next_move = moves[(moves.index(next_move) + 1) % 4]
        print(f"next move is now {next_move}")
        continue
    print(f"{guard}   next is {parsed[guard[0] + next_move[0]][guard[1] + next_move[1]]}")
    parsed[guard[0]][guard[1]][1].append(next_move)
    guard = (guard[0] + next_move[0], guard[1] + next_move[1])
print(f"exit while {next_move} {parsed[guard[0]][guard[1]]}")
print(parsed)

result = 0
for line in parsed:
    for pos in line:
        if pos[1]:
            result += 1

print(result)

print("----- PART 2 -----")


def evaluate(new_o):
    visited = []
    for _ in range(len(parsed)):
        line = []
        for _ in range(len(parsed[0])):
            line.append([])
        visited.append(line)
    next_move = (-1, 0)
    guard = guard_start
    while True:
        if next_move in visited[guard[0]][guard[1]]:
            return True

        if guard[0] + next_move[0] < 0 or guard[1] + next_move[1] < 0 or guard[0] + next_move[0] >= len(parsed) or \
                guard[1] + next_move[1] >= len(parsed[0]):
            return False

        if parsed[guard[0] + next_move[0]][guard[1] + next_move[1]][0] == '#' or (
                guard[0] + next_move[0], guard[1] + next_move[1]) == new_o:
            next_move = moves[(moves.index(next_move) + 1) % 4]
            continue

        if next_move in visited[guard[0]][guard[1]]:
            return True
        visited[guard[0]][guard[1]].append(next_move)
        guard = (guard[0] + next_move[0], guard[1] + next_move[1])


print(evaluate((0, 0)))
print(evaluate((6, 4)))
to_test = result
result = set()
for i in range(len(parsed)):
    print(i)
    for j in range(len(parsed)):
        if not parsed[i][j][1]:
            continue
        if evaluate((i, j)):
            result.add((i, j))
print(result)
print(len(result))
