with open('input.txt') as f:
    lines = f.readlines()


result = 0
for line in lines:
    line.replace("\n", "")
    part1 = line[: len(line)//2]
    part2 = line[len(line)//2:]

    for char in part1:
        if char in part2:
            if ord(char) >= 65 and ord(char) <= 90:
                result += ord(char) - 38
                break
            result += ord(char) - 96
            break

print(result)


print("--------- PART 2 -----------")

i = -3
result = 0
while (i+3) < len(lines):
    i += 3
    common = ""
    flist = lines[i]
    slist = lines[i+1]
    tlist = lines[i+2]

    for elem in flist:
        if elem in slist and elem in tlist:
            common = elem
            break

    if common != "":
        print(common)
        if ord(common) >= 65 and ord(common) <= 90:
            result += ord(common) - 38
            continue
        result += ord(common) - 96
        continue

    for elem in slist:
        if elem in flist and elem in tlist:
            common = elem
            break

    if common != "":
        print(common)
        if ord(common) >= 65 and ord(common) <= 90:
            result += ord(common) - 38
            continue
        result += ord(common) - 96
        continue

    for elem in tlist:
        if elem in flist and elem in slist:
            common = elem
            break

    if common != "":
        print(common)
        if ord(common) >= 65 and ord(common) <= 90:
            result += ord(common) - 38
            continue
        result += ord(common) - 96
        continue
    print("not found")

print(result)