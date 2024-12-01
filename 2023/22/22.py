import sys
import heapq

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

queue = []
for line in inputt:
    temp = line.replace("~", ",").split(",")
    print(f"{int(temp[0])}")
    brick = set(
        [(x, y, z) for x in range(int(temp[0]), int(temp[3]) + 1) for y in range(int(temp[1]), int(temp[4]) + 1) for z
         in range(int(temp[2]), int(temp[5]) + 1)])
    heapq.heappush(queue, (min(int(temp[2]), (int(temp[5]))), brick))

bricks = []
depends = {}
max_z = 1
i = 0
while queue:
    i += 1
    brick = heapq.heappop(queue)[1]
    min_z = min(*[coord[2] for coord in brick]) if len(brick) != 1 else [coord[2] for coord in brick][0]
    new_brick = set()
    for coord in brick:
        new_brick.add((coord[0], coord[1], coord[2] + max_z - min_z))
    brick = new_brick

    print(f"N°{i}")

    while brick not in bricks:
        for coord in brick:
            if coord[2] <= 1:
                if brick not in bricks:
                    max_z = max(max_z - 1, *[coord[2] for coord in brick]) + 1
                    bricks.append(brick)
                break

            for brick2 in bricks:
                if brick == brick2:
                    continue
                if (coord[0], coord[1], coord[2] - 1) in brick2:
                    max_z = max(max_z - 1, *[coord[2] for coord in brick]) + 1
                    if brick not in bricks:
                        bricks.append(brick)
                    if frozenset(brick) in depends:
                        if brick2 not in depends[frozenset(brick)]:
                            depends[frozenset(brick)].append(brick2)
                    else:
                        depends[frozenset(brick)] = [brick2]
        if brick in bricks:
            break

        new_brick = set()
        for coord in brick:
            new_brick.add((coord[0], coord[1], coord[2] - 1))
        brick = new_brick

print(bricks)
print("Depends : ")
result = len(bricks)
for brick in bricks:
    if frozenset(brick) in depends:
        print(f"{brick} : {depends[frozenset(brick)]}")
    else:
        print(f"{brick} : Nothing")

    for brick2 in bricks:
        if frozenset(brick2) in depends and depends[frozenset(brick2)] == [brick]:
            result -= 1
            break

print(result)

print("----- PART 2 -----")


def evaluate(brick, removed=None):
    if removed is None:
        removed = []

    removed.append(brick)
    result = 0
    for brick2 in bricks:
        if brick2 in removed:
            continue

        if frozenset(brick2) not in depends:
            continue

        if len(["t" for depend in depends[frozenset(brick2)] if depend not in removed]) == 0:
            result += 1 + evaluate(brick2, removed)
    return result


result = 0
i = 0
for brick in bricks:
    i += 1
    result += evaluate(brick)
    print(f"After N°{i}  {brick} : {result}")
print(result)
