with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt][0]


def hash(name):
    curr = 0
    for char in name:
        curr += ord(char)
        curr *= 17
        curr %= 256
    return curr


result = 0
for line in inputt.split(","):
    result += hash(line)

print(result)
print(hash("HASH"))

print("----- PART 2 -----")
boxes = [[] for _ in range(256)]

for line in inputt.split(","):
    hash_value = hash(line.split("=")[0].replace("-", ""))
    if "-" in line:
        index = 0
        for t in range(len(boxes[hash_value])):
            if boxes[hash_value][t][0] == line.replace("-", ""):
                boxes[hash_value].pop(t)
                break
    else:
        for t in range(len(boxes[hash_value])):
            if boxes[hash_value][t][0] == line.split("=")[0]:
                boxes[hash_value][t][1] = line.split("=")[1]
                break
        else:
            boxes[hash_value].append(line.split("="))

print(boxes)
result = 0
for box in range(len(boxes)):
    for pos in range(len(boxes[box])):
        result += (box + 1) * (pos + 1) * int(boxes[box][pos][1])
print(result)
