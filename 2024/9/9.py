import sys

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt][0]

disk = []
id = 0
mod = 0
for char in inputt:
    if mod % 2 == 1:
        disk += int(char) * ['.']
    else:
        disk += int(char) * [id]
        id += 1
    mod += 1

print(disk)

i = 0
while i < len(disk):
    while i < len(disk) - 1 and disk[i] == '.':
        disk[i] = disk.pop()
    i += 1

print(disk)

result = 0
for i in range(len(disk)):
    if disk[i] == '.':
        continue
    result += i * disk[i]

print(result)

print("----- PART 2 -----")

disk = []
id = 0
mod = 0
for char in inputt:
    if mod % 2 == 1:
        disk.append((int(char), 0, 0))
    else:
        disk.append((int(char), id, 1))
        id += 1
    mod += 1

print(disk)

i = 0
while i < len(disk):
    print(len(disk) - i)
    if disk[i][2] == 0:
        j = len(disk) - 1
        while j > i and (disk[i][0] < disk[j][0] or disk[j][2] == 0):
            j -= 1

        if j != i:
            # print(f"{disk[i]} is now {disk[j]}   {i}   {j}")
            prev_size = disk[i][0]
            disk[i] = disk[j]
            disk[j] = (disk[j][0], 0, 0)
            disk.insert(i + 1, (prev_size - disk[i][0], 0, 0))
            # print(disk)
    i += 1

print(disk)
# count , id, file
result = 0
pos = 0
for i in range(len(disk)):
    for j in range(disk[i][0]):
        result += pos * disk[i][1]
        pos += 1

print(result)
