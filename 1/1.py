with open('input.txt') as f:
    lines = f.readlines()

elfs = []
total = 0
for line in lines:
    if line == "\n":
        elfs.append(total)
        total = 0
        continue
    total += int(line[:-1])

result = 0
for i in range(3):
    result += max(elfs)
    elfs.pop(elfs.index(max(elfs)))

print(result)