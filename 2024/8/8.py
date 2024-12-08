import math
import sys

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

antennas = {}
for i in range(len(inputt)):
    for j in range(len(inputt)):
        if inputt[i][j] == '.':
            continue
        if inputt[i][j] in antennas.keys():
            antennas[inputt[i][j]].add(((i, j)))
        else:
            antennas[inputt[i][j]] = {(i, j)}

print(antennas)

result = set()
for freq in antennas.keys():
    for an1 in antennas[freq]:
        for an2 in antennas[freq]:
            if an1 == an2:
                continue  # (1, 3) AND (7, 6)
            dx = an2[0] - an1[0]
            dy = an2[1] - an1[1]
            dist = math.sqrt(dx ** 2 + dy ** 2)
            print(f"{an1}  {an2}  -> {dx}   {dy}  {dist}")
            if 0 <= an1[0] - dx < len(inputt) and 0 <= an1[1] - dy < len(inputt[0]):
                result.add((an1[0] - dx, an1[1] - dy))

for i in range(len(inputt)):
    to_print = ""
    for j in range(len(inputt[0])):
        if (i, j) in result:
            to_print += "#"
        else:
            to_print += inputt[i][j]
    print(to_print)

print(result)
print(len(result))

print("----- PART 2 -----")

result = set()
for freq in antennas.keys():
    for an1 in antennas[freq]:
        for an2 in antennas[freq]:
            if an1 == an2:
                continue  # (1, 3) AND (7, 6)
            dx = an2[0] - an1[0]
            dy = an2[1] - an1[1]
            dist = math.sqrt(dx ** 2 + dy ** 2)

            new_pos_x = an1[0]
            new_pos_y = an1[1]
            result.add((new_pos_x, new_pos_y))
            while 0 <= new_pos_x - dx < len(inputt) and 0 <= new_pos_y - dy < len(inputt[0]):
                new_pos_x -= dx
                new_pos_y -= dy
                result.add((new_pos_x, new_pos_y))

for i in range(len(inputt)):
    to_print = ""
    for j in range(len(inputt[0])):
        if (i, j) in result:
            to_print += "#"
        else:
            to_print += inputt[i][j]
    print(to_print)

print(result)
print(len(result))
