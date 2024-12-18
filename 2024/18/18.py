import sys

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

max_coord = 71
to_fall = 1024

parsed = set()
for i in range(to_fall):
    sp = inputt[i].split(",")
    parsed.add((int(sp[0]), int(sp[1])))

for i in range(max_coord):
    line = ""
    for j in range(max_coord):
        if (j, i) in parsed:
            line += "#"
        else:
            line += "."
    print(line)

queue = [((0, 0), 0)]
marked = []
while queue:
    elem = queue.pop(0)
    if elem[0] == (max_coord - 1, max_coord - 1):
        print(elem)
        break
    for (dx, dy) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_pos = (elem[0][0] + dx, elem[0][1] + dy)
        if new_pos not in marked and new_pos[0] >= 0 and new_pos[1] >= 0 and new_pos[0] < max_coord and new_pos[
            1] < max_coord and new_pos not in parsed:
            marked.append(new_pos)
            queue.append((new_pos, elem[1] + 1))

print("----- PART 2 -----")

for i in range(1024, len(inputt)):
    print(f"Add {i}")
    sp = inputt[i].split(",")
    parsed.add((int(sp[0]), int(sp[1])))

    queue = [((0, 0), 0)]
    marked = []
    found = False
    while queue:
        elem = queue.pop(0)
        if elem[0] == (max_coord - 1, max_coord - 1):
            found = True
            break
        for (dx, dy) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_pos = (elem[0][0] + dx, elem[0][1] + dy)
            if new_pos not in marked and new_pos[0] >= 0 and new_pos[1] >= 0 and new_pos[0] < max_coord and new_pos[
                1] < max_coord and new_pos not in parsed:
                marked.append(new_pos)
                queue.append((new_pos, elem[1] + 1))
    if not found:
        print("--------------")
        print(inputt[i])
        print("--------------")