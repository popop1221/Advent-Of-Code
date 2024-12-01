import sys
from matplotlib.path import Path

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

passed = []
start = (0, 0)
dirs = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
min_x = 0
max_x = 0
min_y = 0
max_y = 0
for line in inputt:
    temp = line.split(" ")
    for i in range(int(temp[1])):
        start = (start[0] + dirs[temp[0]][0], start[1] + dirs[temp[0]][1])
        if start not in passed:
            passed.append(start)
            min_x = min(start[0], min_x)
            min_y = min(start[1], min_y)
            max_x = max(start[0], max_x)
            max_y = max(start[1], max_y)

"""print(passed)
result = 0
poly = Path(passed)
print(f"{min_x}  {max_x}  y: {min_y}  {max_y}")
for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        if poly.contains_point((x, y)) and (x, y) not in passed:
            passed.append((x, y))
print(len(passed))"""

print("----- PART 2 -----")


dirs = {"0": (1, 0), "2": (-1, 0), "3": (0, -1), "1": (0, 1), "R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}

passed = [(0, 0)]
start = (0, 0)

dists = []
perimeter = 0
for line in inputt:
    temp = line.split(" ")[2]
    # print(int(temp[2:-2], 16))
    dists.append(int(temp[2:-2], 16))
    start = (start[0] + dirs[temp[-2]][0] * dists[-1], start[1] + dirs[temp[-2]][1] * dists[-1])
    perimeter += dists[-1]
    passed.append(start)

print(perimeter)

x, y = passed[0]
result = 0
for i in range(1, len(passed)):
    new_x, new_y = passed[i]
    result += x * new_y - y * new_x
    x = new_x
    y = new_y
result += x * passed[0][1] - y * new_x

print(abs(result) / 2.0 + perimeter // 2 + 1)