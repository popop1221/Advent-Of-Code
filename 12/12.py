with open('input.txt') as f:
    lines = f.readlines()

with open('test_inputs') as f:
    test_inputs = f.readlines()


def bfs(map, start):
    queue, visited = [], set()
    queue.append({"coord": start, "cost": 0})

    while queue:
        node = queue.pop(0)

        if node.get("coord") in visited:
            continue
        visited.add(node.get("coord"))

        x, y = node.get("coord")
        if map[x][y] == "E":
            return node.get("cost")

        elev = ord(map[x][y]) - 96 if 97 <= ord(map[x][y]) <= 122 else (26 if map[x][y] == "E" else 1)
        for next in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
            if 0 <= next[0] < len(map) and 0 <= next[1] < len(map[0]):
                next_elev = ord(map[next[0]][next[1]]) - 96 if 97 <= ord(map[next[0]][next[1]]) <= 122 else (
                    26 if map[next[0]][next[1]] == "E" else 1)
                if next_elev <= (elev + 1):
                    succ_node = {"coord": next, "cost": node.get("cost") + 1}
                    queue.append(succ_node)

    return 999999


map = []
start_pose = (0, 0)
x = 0
y = 0
for line in lines:
    # for line in test_inputs:
    line = line.replace("\n", "")
    temp = []
    for char in line:
        if char == "S":
            start_pose = (y, x)
        temp.append(char)
        x += 1
    x = 0
    map.append(temp)
    y += 1

print(bfs(map, start_pose))

print("----- PART 2 -----")
map = []
possible_start = []
x = 0
y = 0
for line in lines:
    # for line in test_inputs:
    line = line.replace("\n", "")
    temp = []
    for char in line:
        if char == "S" or char == "a":
            possible_start.append((y, x))
        temp.append(char)
        x += 1
    x = 0
    map.append(temp)
    y += 1

results = []
for pos in possible_start:
    results.append(bfs(map, pos))
print(min(results))
