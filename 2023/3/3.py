with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input

parsed = []

for line in inputt:
    temp = []
    for char in line.replace("\n", ""):
        temp.append(char)
    parsed.append(temp)

result = 0

current = ["", False]
for y in range(len(parsed)):
    for x in range(len(parsed[0])):
        # print(f"Current is {x}  {y}   {current}")
        if parsed[y][x] == ".":
            # print("Current is point")
            if current[1] and current[0] != "":
                print(f"Work for : {current[0]}")
                result += int(current[0])
                # print(result)
            current = ["", False]
            continue

        if parsed[y][x] in "#*/@$%+-&=":
            if current[0] != "":
                current[1] = True
                print(f"Work2 for : {current[0]}")
                result += int(current[0])
                # print(result)
                current = ["", False]
            # print("current is special character")
            continue

        current[0] += parsed[y][x]
        # print("current ins number ")
        for new_x, new_y in [(x + 1, y - 1), (x + 1, y), (x + 1, y + 1), (x, y - 1), (x, y + 1), (x - 1, y - 1),
                             (x - 1, y), (x - 1, y + 1)]:
            # print(f"Test diag {new_x}  {new_y}")
            if new_x >= 0 and new_y >= 0 and new_x < len(parsed[0]) and new_y < len(parsed):
                # print(f"Coord valid {parsed[y][x]}")
                if parsed[new_y][new_x] in "#*/@$%+-&=":
                    # print("Current is diag ok")
                    current[1] = True
                    continue

print(result)

print("----- PART 2 -----")

result = 0

current = [[], False]
for y in range(len(parsed)):
    for x in range(len(parsed[0])):
        if parsed[y][x] == "*":
            adj = []
            for new_x, new_y in [(x + 1, y - 1), (x + 1, y), (x + 1, y + 1), (x, y - 1), (x, y + 1), (x - 1, y - 1),
                                 (x - 1, y), (x - 1, y + 1)]:
                if new_x >= 0 and new_y >= 0 and new_x < len(parsed[0]) and new_y < len(parsed):
                    if parsed[new_y][new_x] not in "0123456789":
                        continue
                    temp = parsed[new_y][new_x]
                    for i in range(1, 4):
                        if new_x - i >= 0 and new_y >= 0 and new_x < len(parsed[0]) and new_y < len(parsed):
                            if parsed[new_y][new_x - i] in "0123456789":
                                temp = parsed[new_y][new_x - i] + temp
                            else:
                                break
                    for i in range(1, 4):
                        if new_x >= 0 and new_y >= 0 and new_x + i < len(parsed[0]) and new_y < len(parsed):
                            if parsed[new_y][new_x + i] in "0123456789":
                                temp += parsed[new_y][new_x + i]
                            else:
                                break
                    if temp not in adj:
                        adj.append(temp)
            print(adj)
            if len(adj) == 2:
                result += int(adj[0]) * int(adj[1])

print(result)
