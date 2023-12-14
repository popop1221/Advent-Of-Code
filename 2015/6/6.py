with open('input.txt') as f:
    real_input = f.readlines()

inputt = real_input

map = [[False for _ in range(1000)] for _ in range(1000)]

for line in inputt:
    line = line.replace("\n", "")
    temp = line.split(",")
    for i in range(int(temp[0].split(" ")[-1]), int(temp[1].split(" ")[-1]) + 1):
        for j in range(int(temp[1].split(" ")[0]), int(temp[2]) + 1):
            if line.startswith("toggle"):
                map[i][j] = not map[i][j]
            else:
                map[i][j] = line.startswith("turn on")

result = 0
for i in range(len(map)):
    for j in range(len(map[0])):
        result += map[i][j]
print(result)

print("----- PART 2 -----")

map = [[0 for _ in range(1000)] for _ in range(1000)]

for line in inputt:
    line = line.replace("\n", "")
    temp = line.split(",")
    for i in range(int(temp[0].split(" ")[-1]), int(temp[1].split(" ")[-1]) + 1):
        for j in range(int(temp[1].split(" ")[0]), int(temp[2]) + 1):
            if line.startswith("toggle"):
                map[i][j] += 2
            elif line.startswith("turn on"):
                map[i][j] += 1
            elif map[i][j] != 0:
                map[i][j] -= 1

result = 0
for i in range(len(map)):
    for j in range(len(map[0])):
        result += map[i][j]
print(result)
