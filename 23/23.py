with open('input.txt') as f:
    lines = f.readlines()

with open('test_inputs') as f:
    test_input = f.readlines()

elfs = {}
elf_coords = set()
elf_id = 0
y = 0
#for line in lines:
for line in test_input:
    y += 1
    line = line.replace("\n", "")
    x = 0
    for char in line:
        x += 1
        if char == "#":
            elf_coords.add((y, x))
            #Je sais pas lire donc j'avais fait une gestion par elfe (ça fonctionne pour la partie 1 mais pas la 2)
            elfs[elf_id] = ((y, x), ["N", "S", "W", "E"])
            elf_id += 1

print(elf_coords)
print(elfs)

print(f"--------- Turn -1 ------------")
min_y = min([y for (x, y) in elf_coords])
max_y = max([y for (x, y) in elf_coords])
min_x = min([x for (x, y) in elf_coords])
max_x = max([x for (x, y) in elf_coords])
print(" ", end="")
for j in range(min_y, max_y + 1):
    print(j, end="")
print()
for i in range(min_y, max_y + 1):
    print(i, end="")
    for j in range(min_x, max_x + 1):
        if elf_coords.__contains__((j, i)):
            print("#", end="")
        else:
            print(".", end="")
    print()
print((max_x - min_x) * (max_y - min_y) - len(elfs))

around = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
dirs = {"S": ((0, 1), (1, 1), (-1, 1)), 'N': ((0, -1), (1, -1), (-1, -1)), 'W': ((-1, 0), (-1, 1), (-1, -1)),
        'E': ((1, 0), (1, 1), (1, -1))}
for acc in range(10):
    new_coords = []
    new_coords_by_elfs = {}
    for elf in elfs.keys():
        if elf == 7:
            print(elfs[elf])
        if not [1 for pos in around if (elfs[elf][0][0] + pos[1], elfs[elf][0][1] + pos[0]) in elf_coords]:
            if elf == 7:
                print("No need to move")
            continue
        for i in range(4):
            dir = elfs[elf][1][i]
            if [1 for pos in dirs[dir] if (elfs[elf][0][0] + pos[1], elfs[elf][0][1] + pos[0]) in elf_coords]:
                if elf == 7:
                    print(f"Dont move to {i}")
                continue
            new_coords.append((elfs[elf][0][0] + dirs[dir][0][0], elfs[elf][0][1] + dirs[dir][0][1]))
            new_coords_by_elfs[elf] = (elfs[elf][0][0] + dirs[dir][0][0], elfs[elf][0][1] + dirs[dir][0][1])
            elfs[elf][1].append(elfs[elf][1].pop(0))
            if elf == 7:
                print(f"move to {i}")
                print(new_coords_by_elfs[elf])
            break

    for elf in new_coords_by_elfs:
        if new_coords.count(new_coords_by_elfs[elf]) == 1:
            elfs[elf] = (new_coords_by_elfs[elf], elfs[elf][1])
    elf_coords = set()
    for elf in elfs:
        elf_coords.add(elfs[elf][0])

    print(f"--------- Turn {acc} ------------")
    print(elfs)
    min_y = min([y for (x, y) in elf_coords])
    max_y = max([y for (x, y) in elf_coords])
    min_x = min([x for (x, y) in elf_coords])
    max_x = max([x for (x, y) in elf_coords])
    print(" ", end="")
    for j in range(min_x, max_x + 1):
        print(j, end="")
    print()
    for i in range(min_y, max_y + 1):
        print(i, end="")
        for j in range(min_x, max_x + 1):
            if elfs[7][0] == (j,i):
                print("O", end="")
            elif elf_coords.__contains__((j, i)):
                print("#", end="")
            else:
                print(".", end="")
        print()
    print((max_x - min_x + 1) * (max_y - min_y + 1) - len(elfs))

print("----- PART 2 -----")

elfs = {}
elf_coords = set()
elf_id = 0
y = 0
for line in lines:
#for line in test_input:
    y += 1
    x = 0
    for char in line:
        x += 1
        if char == "#":
            elf_coords.add((x, y))
            elfs[elf_id] = (x, y)
            elf_id += 1

around = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
dirs = {1: ((0, 1), (1, 1), (-1, 1)), 0: ((0, -1), (1, -1), (-1, -1)), 2: ((-1, 0), (-1, 1), (-1, -1)),
        3: ((1, 0), (1, 1), (1, -1))}
turn = -1
while True:
    turn += 1
    has_move = False
    new_coords = []
    new_coords_by_elfs = {}
    for elf in elfs.keys():
        if not [1 for pos in around if (elfs[elf][0] + pos[0], elfs[elf][1] + pos[1]) in elf_coords]:
            continue
        for i in range(4):
            if [1 for pos in dirs[(turn + i) % 4] if (elfs[elf][0] + pos[0], elfs[elf][1] + pos[1]) in elf_coords]:
                continue
            new_coords.append((elfs[elf][0] + dirs[(turn + i) % 4][0][0], elfs[elf][1] + dirs[(turn + i) % 4][0][1]))
            new_coords_by_elfs[elf] = (elfs[elf][0] + dirs[(turn + i) % 4][0][0], elfs[elf][1] + dirs[(turn + i) % 4][0][1])
            break

    for elf in new_coords_by_elfs:
        if new_coords.count(new_coords_by_elfs[elf]) == 1:
            has_move = True
            elfs[elf] = new_coords_by_elfs[elf]
    elf_coords = set()
    for elf in elfs:
        elf_coords.add(elfs[elf])
    if not has_move:
        print(turn + 1)
        break
