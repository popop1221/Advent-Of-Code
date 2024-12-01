import sys
import z3
import numpy as np

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

lines = []
for line in inputt:
    temp = line.split("@")
    temp1 = temp[0].split(",")
    temp2 = temp[1].split(",")

    lines.append(((int(temp1[0]), int(temp1[1]), int(temp1[2])),
                  (int(temp1[0]) + int(temp2[0]), int(temp1[1]) + int(temp2[1]), int(temp1[1]) + int(temp2[1])),
                  (int(temp2[0]), int(temp2[1]), int(temp2[2]))))


def find_intersection(line1, line2):
    x1, y1, z1 = line1[0]
    x2, y2, z2 = line1[1]
    x3, y3, z3 = line2[0]
    x4, y4, z4 = line2[1]

    m1 = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else float('inf')
    m2 = (y4 - y3) / (x4 - x3) if (x4 - x3) != 0 else float('inf')

    b1 = y1 - m1 * x1 if m1 != float('inf') else None
    b2 = y3 - m2 * x3 if m2 != float('inf') else None

    if m1 == m2:
        return None

    if m1 == float('inf'):
        x = x1
        y = m2 * x + b2
    elif m2 == float('inf'):
        x = x3
        y = m1 * x + b1
    else:
        x = (b2 - b1) / (m1 - m2)
        y = m1 * x + b1

    return x, y


print(lines)
result = 0
for line1 in lines:
    for line2 in lines:
        if line1 == line2:
            continue

        pos = find_intersection(line1, line2)
        if pos is None:
            continue

        if 200000000000000 < pos[0] < 400000000000000 and 200000000000000 < pos[1] < 400000000000000:
            if ((line1[2][0] > 0 and pos[0] >= line1[0][0]) or (line1[2][0] <= 0 and pos[0] <= line1[0][0])) and \
                    ((line2[2][0] > 0 and pos[0] >= line2[0][0]) or (line2[2][0] <= 0 and pos[0] <= line2[0][0])) and \
                    ((line1[2][1] > 0 and pos[1] >= line1[0][1]) or (line1[2][1] <= 0 and pos[1] <= line1[0][1])) and \
                    ((line2[2][1] > 0 and pos[1] >= line2[0][1]) or (line2[2][1] <= 0 and pos[1] <= line2[0][1])):
                result += 1

print(result // 2)

print("----- PART 2 -----")

print(lines[:3])
"""
19-1*t1 = x+dx*t1;
13+1*t1 = y+dy*t1;
30-2*t1 = z+dz*t1;

18-1*t2 = x+dx*t2;
19-1*t2 = y+dy*t2;
22-2*t2 = z+dz*t2;

20-2*t3 = x+dx*t3;
25-2*t3 = y+dy*t3;
34-4*t3 = z+dz*t3;

t1 > 0;
t2 > 0;
t3 > 0;
"""


solver = z3.Solver()
i = 0
x = z3.Int("x")
y = z3.Int("y")
z = z3.Int("z")
dx = z3.Int("vx")
dy = z3.Int("vy")
dz = z3.Int("vz")
for line in lines[:3]:
    i += 1
    t = z3.Int(f"t{i}")
    solver.add(line[0][0] + line[2][0] * t == x + dx * t)
    solver.add(line[0][1] + line[2][1] * t == y + dy * t)
    solver.add(line[0][2] + line[2][2] * t == z + dz * t)
    solver.add(t > 0)
solver.check()
print(solver.model())

print(463222539161932 + 273997500449219 + 239756157786030)

