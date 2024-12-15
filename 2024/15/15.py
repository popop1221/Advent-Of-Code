import sys
from copy import copy

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

moves_dic = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}

"""step = 0
parsed = []
moves = ""
pos = (0, 0)
for line in inputt:
    if line == "":
        step += 1
    if step == 0:
        temp = []
        for char in line:
            temp.append(char)
        parsed.append(temp)
    if step == 1:
        moves += line

for i in range(len(parsed)):
    for j in range(len(parsed[0])):
        if parsed[i][j] == "@":
            pos = (i, j)
            break

print(parsed)
print(moves)
print(pos)


def can_move(block_pos, move_dir):
    new_pos = (block_pos[0] + move_dir[0], block_pos[1] + move_dir[1])
    if parsed[new_pos[0]][new_pos[1]] == '.':
        parsed[new_pos[0]][new_pos[1]] = "O"
        parsed[block_pos[0]][block_pos[1]] = "."
        return True
    if parsed[new_pos[0]][new_pos[1]] == "#":
        return False
    if can_move(new_pos, move_dir):
        parsed[new_pos[0]][new_pos[1]] = "O"
        parsed[block_pos[0]][block_pos[1]] = "."
        return True
    return False

for move in moves:
    new_pos = (pos[0] + moves_dic[move][0], pos[1] + moves_dic[move][1])
    if parsed[new_pos[0]][new_pos[1]] == "#":
        continue
    if parsed[new_pos[0]][new_pos[1]] == "O" and not can_move(new_pos, moves_dic[move]):
        continue
    print(f"{pos} {move} {new_pos}")
    parsed[new_pos[0]][new_pos[1]] = "@"
    parsed[pos[0]][pos[1]] = "."
    pos = new_pos
    for i in range(len(parsed)):
        line = ""
        for j in range(len(parsed[0])):
            line += parsed[i][j]
        print(line)

result = 0
for i in range(len(parsed)):
    for j in range(len(parsed[0])):
        if parsed[i][j] == "O":
            result += 100 * i + j
print(result)"""

print("----- PART 2 -----")

step = 0
parsed = []
moves = ""
pos = (0, 0)
for line in inputt:
    if line == "":
        step += 1
    if step == 0:
        temp = []
        for char in line:
            if char == "O":
                temp.append("[")
                temp.append("]")
                continue
            if char == "@":
                temp.append("@")
                temp.append(".")
                continue
            temp.append(char)
            temp.append(char)
        parsed.append(temp)
    if step == 1:
        moves += line

for i in range(len(parsed)):
    for j in range(len(parsed[0])):
        if parsed[i][j] == "@":
            pos = (i, j)
            break

print(parsed)
print(moves)
print(pos)

for i in range(len(parsed)):
    line = ""
    for j in range(len(parsed[0])):
        line += parsed[i][j]
    print(line)


def do_move(block_pos, move_dir):
    new_poss = [block_pos, (block_pos[0], block_pos[1] + 1)] if parsed[block_pos[0]][block_pos[1]] == "[" else [
        block_pos, (block_pos[0], block_pos[1] - 1)]
    old_pos = copy(new_poss)
    for ii in range(len(new_poss)):
        new_poss[ii] = (new_poss[ii][0] + move_dir[0], new_poss[ii][1] + move_dir[1])
        if parsed[new_poss[ii][0]][new_poss[ii][1]] == "#":
            return False
        if new_poss[ii] not in old_pos and parsed[new_poss[ii][0]][new_poss[ii][1]] in "[]" and not do_move(
                new_poss[ii], move_dir):
            return False
    for o_pos in old_pos:
        parsed[o_pos[0]][o_pos[1]] = "."
    parsed[new_poss[0][0]][new_poss[0][1]] = "[" if new_poss[1][1] - 1 == new_poss[0][1] else ']'
    parsed[new_poss[1][0]][new_poss[1][1]] = "]" if new_poss[1][1] - 1 == new_poss[0][1] else '['
    return True


def can_move_2(block_pos, move_dir):
    new_poss = [block_pos, (block_pos[0], block_pos[1] + 1)] if parsed[block_pos[0]][block_pos[1]] == "[" else [
        block_pos, (block_pos[0], block_pos[1] - 1)]
    old_pos = copy(new_poss)
    for ii in range(len(new_poss)):
        new_poss[ii] = (new_poss[ii][0] + move_dir[0], new_poss[ii][1] + move_dir[1])
        if parsed[new_poss[ii][0]][new_poss[ii][1]] == "#":
            return False
        if new_poss[ii] not in old_pos and parsed[new_poss[ii][0]][new_poss[ii][1]] in "[]" and not can_move_2(
                new_poss[ii], move_dir):
            return False
    return True


turn = 0
for move in moves:
    turn += 1
    new_pos = (pos[0] + moves_dic[move][0], pos[1] + moves_dic[move][1])
    if parsed[new_pos[0]][new_pos[1]] == "#":
        continue
    if (parsed[new_pos[0]][new_pos[1]] == "[" or parsed[new_pos[0]][new_pos[1]] == "]"):
        if not can_move_2(new_pos, moves_dic[move]):
            continue
        do_move(new_pos, moves_dic[move])
    print(f"{turn} : {pos} {move} {new_pos}")
    parsed[new_pos[0]][new_pos[1]] = "@"
    parsed[pos[0]][pos[1]] = "."
    pos = new_pos

result = 0
for i in range(len(parsed)):
    for j in range(len(parsed[0])):
        if parsed[i][j] == "[":
            result += 100 * i + j
print(result)

for i in range(len(parsed)):
    line = ""
    for j in range(len(parsed[0])):
        line += parsed[i][j]
    print(line)
