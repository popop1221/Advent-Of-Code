with open('input.txt') as f:
    inputt = f.readlines()

parsed = []
for line in inputt:
    line = line.replace("\n", "")
    temp = line.split(" ")
    parsed.append((int(temp[3]), int(temp[6]), int(temp[13])))

print(parsed)

result = []
for test in parsed:
    temp = 0
    i = 0
    j = 0
    while i <= 2503:
        if j != test[1]:
            j += 1
            i += 1
            temp += test[0]
        else:
            j = 0
            i += test[2]
    result.append(temp)

print(result)

print("----- PART 2 -----")

points = [0 for _ in range(len(parsed))]
result = [[0, 0] for _ in range(len(parsed))]
for _ in range(2503):
    for i in range(len(parsed)):
        if result[i][1] == parsed[i][1]:
            result[i][1] = -parsed[i][2]
        if result[i][1] >= 0:
            result[i][0] += parsed[i][0]
        result[i][1] += 1
    temp = max([t[0] for t in result])
    for i in range(len(parsed)):
        if result[i][0] == temp:
            points[i] += 1

print(result)
print(points)
