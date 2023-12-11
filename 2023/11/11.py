import math

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input

parsed = []

for line in inputt:
    line = line.replace("\n", "")
    line = line.replace("\n", "")
    temp = [t for t in line]
    parsed.append(temp)
    if "#" not in line:
        parsed.append(temp)

x = 0
while x < len(parsed[0]):
    for y in range(len(parsed)):
        if parsed[y][x] == "#":
            break
    else:
        for y in range(len(parsed)):
            parsed[y].insert(x, ".")
        x += 1
    x += 1

galaxies = []
for y in range(len(parsed)):
    for x in range(len(parsed[y])):
        if parsed[y][x] == "#":
            galaxies.append((x, y))

result = 0
t = 0
for i in range(len(galaxies)):
    for j in range(i, len(galaxies)):
        t += 1
        temp = math.fabs(galaxies[i][0] - galaxies[j][0]) + math.fabs(galaxies[i][1] - galaxies[j][1])
        print(f"comb {t}  {galaxies[i]}  {galaxies[j]}   {temp}")
        result += temp

print(result)

print("----- PART 2 -----")
parsed = []

no_way_y = []
no_way_x = []

t = -1
for line in inputt:
    t += 1
    line = line.replace("\n", "")
    line = line.replace("\n", "")
    temp = [t for t in line]
    parsed.append(temp)
    if "#" not in line:
        no_way_y.append(t)

x = 0
while x < len(parsed[0]):
    for y in range(len(parsed)):
        if parsed[y][x] == "#":
            break
    else:
        no_way_x.append(x)
    x += 1

galaxies = []
for y in range(len(parsed)):
    for x in range(len(parsed[y])):
        if parsed[y][x] == "#":
            galaxies.append((x, y))

result = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        temp = 0
        for k in range(min(galaxies[i][0], galaxies[j][0]), max(galaxies[i][0], galaxies[j][0])):
            if k in no_way_x:
                temp += 1000000
            else:
                temp += 1
        for k in range(min(galaxies[i][1], galaxies[j][1]), max(galaxies[i][1], galaxies[j][1])):
            if k in no_way_y:
                temp += 1000000
            else:
                temp += 1
        result += temp

print(result)

