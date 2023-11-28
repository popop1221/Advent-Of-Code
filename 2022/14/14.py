with open('input.txt') as f:
    lines = f.readlines()

with open('test_inputs') as f:
    test_input = f.readlines()

map = [["." for i in range(1000)] for j in range(1000)]
map[500][0] = "+"
yPos = []

for line in lines:
#for line in test_input:
    line = line.replace("\n", "")
    temp = line.split(" -> ")
    for i in range(len(temp) - 1):
        pos1, pos2 = temp[i], temp[i+1]
        pos1x, pos1y, pos2x, pos2y = int(pos1.split(",")[0]), int(pos1.split(",")[1]), int(pos2.split(",")[0]), int(pos2.split(",")[1])
        yPos.append(pos1y)
        yPos.append(pos2y)
        if pos1x == pos2x:
            if pos1y > pos2y:
                pos1y, pos2y = pos2y, pos1y

            while pos1y != pos2y + 1:
                map[pos1x][pos1y] = "#"
                #print(f"print rock in {pos1x}     {pos1y}")
                pos1y += 1
            continue
        else:
            if pos1x > pos2x:
                pos1x, pos2x = pos2x, pos1x

            while pos1x != pos2x + 1:
                map[pos1x][pos1y] = "#"
                #print(f"print rock in {pos1x}     {pos1y}")
                pos1x += 1

TheSandIsFalling = False
sandRest = 0
sandInProgress = False
sandLoc = (500, 0)

while not TheSandIsFalling:
    if not sandInProgress:
        sandLoc = (500, 0)
        sandInProgress = True
        map[500][0] = "S"
        continue

    if sandLoc[1] >= 999:
        TheSandIsFalling = True
        break

    if map[sandLoc[0]][sandLoc[1] + 1] == ".":
        map[sandLoc[0]][sandLoc[1]] = "."
        map[sandLoc[0]][sandLoc[1]+1] = "S"
        sandLoc = (sandLoc[0], sandLoc[1]+1)
        continue

    elif map[sandLoc[0]-1][sandLoc[1] + 1] == ".":
        map[sandLoc[0]][sandLoc[1]] = "."
        map[sandLoc[0]-1][sandLoc[1]+1] = "S"
        sandLoc = (sandLoc[0]-1, sandLoc[1] + 1)
        continue

    elif map[sandLoc[0]+1][sandLoc[1] + 1] == ".":
        map[sandLoc[0]][sandLoc[1]] = "."
        map[sandLoc[0]+1][sandLoc[1]+1] = "S"
        sandLoc = (sandLoc[0]+1, sandLoc[1] + 1)
        continue

    else :
        #print(f"Sand stop at : {sandLoc}")
        if sandLoc == (500, 0):
            print("Problem")
            break
        sandRest += 1
        sandInProgress = False

print(sandRest)

print("----- PART 2 -----")

TheSandIsFalling = False
sandInProgress = False
sandLoc = (500, 0)
floor = max(yPos) + 1

while not TheSandIsFalling:
    if not sandInProgress:
        sandLoc = (500, 0)
        sandInProgress = True
        map[500][0] = "S"
        continue

    if sandLoc[1] >= floor:
        print(f"Sand stop at : {sandLoc}")
        sandRest += 1
        sandInProgress = False
        continue

    if map[sandLoc[0]][sandLoc[1] + 1] == ".":
        map[sandLoc[0]][sandLoc[1]] = "."
        map[sandLoc[0]][sandLoc[1]+1] = "S"
        sandLoc = (sandLoc[0], sandLoc[1]+1)
        continue

    elif map[sandLoc[0]-1][sandLoc[1] + 1] == ".":
        map[sandLoc[0]][sandLoc[1]] = "."
        map[sandLoc[0]-1][sandLoc[1]+1] = "S"
        sandLoc = (sandLoc[0]-1, sandLoc[1] + 1)
        continue

    elif map[sandLoc[0]+1][sandLoc[1] + 1] == ".":
        map[sandLoc[0]][sandLoc[1]] = "."
        map[sandLoc[0]+1][sandLoc[1]+1] = "S"
        sandLoc = (sandLoc[0]+1, sandLoc[1] + 1)
        continue

    else:
        sandRest += 1
        if sandLoc == (500, 0):
            break
        sandInProgress = False

print(sandRest)
