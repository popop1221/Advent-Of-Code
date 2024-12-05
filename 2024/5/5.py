import sys

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

parsed = []
i = 1
for line in inputt:
    if line == '':
        break
    sp = line.split("|")
    parsed.append(sp)
    # parsed[sp[1]] = sp[0]
    i += 1
print(parsed)
result = 0
part2_data = []
for line in inputt[i:]:
    sp = line.split(",")
    valid = True
    printed = set()
    for i in range(len(sp)):
        for j in range(i + 1, len(sp)):
            if [sp[i], sp[j]] not in parsed:
                valid = False
                break
        for printedd in printed:
            if [printedd, sp[i]] not in parsed:
                valid = False
                break
        if not valid:
            break
        printed.add(sp[i])
    if valid:
        result += int(sp[len(sp) // 2])
    else:
        part2_data.append(sp)
    # break
print(result)

print("----- PART 2 -----")

print(part2_data)
result = 0
for line in part2_data:
    while True:
        valid = True
        printed = set()
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                if [line[i], line[j]] not in parsed:
                    line[j], line[i] = line[i], line[j]
                    valid = False
                    break
            for printedd in printed:
                if [line[printedd], line[i]] not in parsed:
                    line[printedd], line[i] = line[i], line[printedd]
                    valid = False
                    break
            if not valid:
                break
            printed.add(i)
        if valid:
            result += int(line[len(line) // 2])
            break
        #break
print(part2_data)
print(result)