from copy import copy

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input

map = []
for line in inputt:
    line = line.replace("\n", "")
    map.append([char for char in line])

for i in range(len(map)):
    for j in range(len(map[i])):
        i_copy = i
        j_copy = j
        print(f"{i}  {j}  {map[i][j]}")
        if map[i_copy][j_copy] != "O":
            continue
        map[i_copy][j_copy] = "."
        while i_copy > 0 and map[i_copy - 1][j_copy] not in "#E":
            i_copy -= 1
        map[i_copy][j_copy] = "E"

print(map)

result = 0
res2 = 0
for i in range(len(map)):
    print(map[i].count("E"))
    res2 += (len(map) - i) * map[i].count("E")
    for j in range(len(map[i])):
        if map[i][j] == "E":
            result += len(map) - i
print(result)
print(res2)

print("----- PART 2 -----")


def reset_map(maps):
    for i in range(len(maps)):
        for j in range(len(map[0])):
            if maps[i][j] == "E":
                maps[i][j] = "O"


map = []
for line in inputt:
    line = line.replace("\n", "")
    map.append([char for char in line])

cycles = []
index = 0
while index < 1000000000:
    print(f"Process {index}")
    for k in [(-1, 0, 0, len(map), 1), (0, -1, 0, len(map), 1), (1, 0, len(map) - 1, -1, -1),
              (0, 1, len(map) - 1, -1, -1)]:
        while any(["O" in row for row in map]):
            for i in range(k[2], k[3], k[4]):
                for j in range(k[2], k[3], k[4]):
                    i_copy = i
                    j_copy = j
                    if map[i_copy][j_copy] != "O":
                        continue
                    map[i_copy][j_copy] = "."
                    while 0 <= i_copy + k[0] < len(map) and 0 <= j_copy + k[1] < len(map[0]) and map[i_copy + k[0]][
                        j_copy + k[1]] not in "#EO":
                        i_copy += k[0]
                        j_copy += k[1]
                    map[i_copy][j_copy] = "E"
        reset_map(map)
    if map in cycles:
        print(f"cycle : {index} {cycles.index(map)}")
        temp = index - cycles.index(map)
        print()
        for i in range(len(map)):
            print(map[i])
        index += temp * (1000000000 // temp)
        while index >= 1000000000:
            index -= temp
        cycles = []
    cycles.append([copy(row) for row in map])
    index += 1

result = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "O":
            result += len(map) - i
print(result)
