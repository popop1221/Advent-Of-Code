with open('input.txt') as f:
    lines = f.readlines()

test_input = ["30373",
              "25512",
              "65332",
              "33549",
              "35390"]

inputs = []


def test_visibility(map, x, y):
    maxv = map[x][y]
    visible = True
    currentx = x
    while (currentx - 1) >= 0:
        currentx -= 1
        if map[currentx][y] >= maxv:
            visible = False
            break
    if visible:
        return 1

    visible = True
    currentx = x
    while (currentx + 1) < len(map):
        currentx += 1
        if map[currentx][y] >= maxv:
            visible = False
            break
    if visible:
        return 1

    visible = True
    currenty = y
    while (currenty - 1) >= 0:
        currenty -= 1
        if map[x][currenty] >= maxv:
            visible = False
            break
    if visible:
        return 1

    visible = True
    currenty = y
    while (currenty + 1) < len(map[0]):
        currenty += 1
        if map[x][currenty] >= maxv:
            visible = False
            break
    if visible:
        return 1
    return 0


result = []
for line in lines:
    # for line in test_input:
    temp = []
    line.replace("\n", "")
    for char in line:
        if char.replace("\n", "") != "":
            temp.append(int(char.replace("\n", "")))
    inputs.append(temp)

for x in range(len(inputs)):
    temp = []
    for y in range(len(inputs[x])):
        temp.append(test_visibility(inputs, x, y))
    result.append(temp)

result1 = 0
for tab in result:
    result1 += tab.count(1)
print(result1)

print("----- PART 2 -----")

test_input = ["30373",
              "25512",
              "65332",
              "33549",
              "35390"]

inputs = []


def test_visibility2(map, x, y):
    score = 1

    maxv = map[x][y]
    currentx = x
    tempscore = 0
    while (currentx - 1) >= 0:
        currentx -= 1
        tempscore += 1
        if map[currentx][y] >= maxv:
            break
    score *= tempscore

    currentx = x
    tempscore = 0
    while (currentx + 1) < len(map):
        currentx += 1
        tempscore += 1
        if map[currentx][y] >= maxv:
            break
    score *= tempscore

    currenty = y
    tempscore = 0
    while (currenty - 1) >= 0:
        currenty -= 1
        tempscore += 1
        if map[x][currenty] >= maxv:
            break
    score *= tempscore

    currenty = y
    tempscore = 0
    while (currenty + 1) < len(map[0]):
        currenty += 1
        tempscore += 1
        if map[x][currenty] >= maxv:
            break
    score *= tempscore
    return score if score > 0 else 1


result = []
for line in lines:
    # for line in test_input:
    temp = []
    line.replace("\n", "")
    for char in line:
        if char.replace("\n", "") != "":
            temp.append(int(char.replace("\n", "")))
    inputs.append(temp)

for x in range(len(inputs)):
    temp = []
    for y in range(len(inputs[x])):
        temp.append(test_visibility2(inputs, x, y))
    result.append(temp)

result1 = 0
for tab in result:
    result1 = max([result1] + tab)
print(result1)
