with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input

result = 0

for line in inputt:
    res = []
    for char in line:
        if '0' <= char <= '9':
            res.append(int(char))
    if len(res) == 0:
        continue
    if len(res) == 1:
        result += int(str(res[0]) + str(res[0]))
    else:
        result += int(str(res[0]) + str(res[len(res) - 1]))

print(result)

print("----- PART 2 -----")

result = 0
for line in inputt:
    res = []
    for i in range(len(line)):
        char = line[i]
        if char >= '0' and char <= '9':
            res.append(int(char))
            i += 1
            continue
        for number, st in [(1, "one"), (2, "two"), (3, "three"), (4, "four"), (5, "five"), (6, "six"), (7, "seven"),
                           (8, "eight"), (9, "nine")]:
            if i + len(st) - 1 < len(line) and line[i: i + len(st)] == st:
                res.append(number)
                i += len(st) - 1
                break
        i += 1

    if len(res) == 1:
        result += int(str(res[0]) + str(res[0]))
    else:
        result += int(str(res[0]) + str(res[len(res) - 1]))

print(result)
