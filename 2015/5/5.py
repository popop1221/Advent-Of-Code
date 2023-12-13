with open('input.txt') as f:
    real_input = f.readlines()

inputt = real_input

result = 0
for line in inputt:
    line = line.replace("\n", "")

    if "ab" in line or "cd" in line or "pq" in line or "xy" in line:
        continue

    count = 0
    two = False
    for i in range(len(line)):
        letter = line[i]
        if letter in "aeiou":
            count += 1
        if i > 0 and line[i] == line[i - 1]:
            two = True

    if two and count >= 3:
        result += 1

print(result)

print("----- PART 2 -----")

result = 0
for line in inputt:
    valid = False
    for i in range(len(line)):
        if i > 1 and line[i] == line[i - 2]:
            valid = True
            break

    if not valid:
        continue

    for i in range(len(line)):
        if i > 0 and line.count(line[i - 1] + line[i]) >= 2:
            result += 1
            break

print(result)
