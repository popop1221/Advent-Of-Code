import sys
sys.setrecursionlimit(15000)

with open('input.txt') as f:
    lines = f.readlines()

with open('test_inputs') as f:
    test_input = f.readlines()

cubes = set()
for line in lines:
#for line in test_input:
    line = line.replace("\n", "")
    coord = line.split(",")
    cubes.add((int(coord[0]), int(coord[1]), int(coord[2])))

result = 0
for cube in cubes:
    adjacs = [(cube[0] - 1, cube[1], cube[2]), (cube[0], cube[1] - 1, cube[2]), (cube[0] + 1, cube[1], cube[2]),
              (cube[0], cube[1] + 1, cube[2]), (cube[0], cube[1], cube[2] - 1), (cube[0], cube[1], cube[2] + 1)]
    for adja in adjacs:
        if adja not in cubes:
            result += 1

print(result)

print("----- PART 2 -----")


def is_exterior(x, y, z, checked):
    if x > 23 or x < 0 or y < 0 or y > 23 or z > 23 or z < 0:
        return True
    checked.add((x, y, z))
    if (x, y, z) in cubes:
        return False

    adjacs = [(x - 1, y, z), (x, y - 1, z), (x + 1, y, z),
              (x, y + 1, z), (x, y, z - 1), (x, y, z + 1)]

    for adja in adjacs:
        if adja not in checked:
            if is_exterior(adja[0], adja[1], adja[2], checked):
                return True
    return False


result = 0
for cube in cubes:
    adjacs = [(cube[0] - 1, cube[1], cube[2]), (cube[0], cube[1] - 1, cube[2]), (cube[0] + 1, cube[1], cube[2]),
              (cube[0], cube[1] + 1, cube[2]), (cube[0], cube[1], cube[2] - 1), (cube[0], cube[1], cube[2] + 1)]
    for adja in adjacs:
        if adja not in cubes and is_exterior(adja[0], adja[1], adja[2], set()):
            result += 1

print(result)
