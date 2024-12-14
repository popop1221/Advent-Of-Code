import sys
from copy import copy

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

parsed = []
for line in inputt:
    sp = line.split(" ")
    sp0 = sp[0].split(",")
    sp1 = sp[1].split(",")
    parsed.append([(int(sp0[0].replace("p=", "")), int(sp0[1])), (int(sp1[0].replace("v=", "")), int(sp1[1]))])

print(parsed)
parsed2 = [copy(par) for par in parsed]

size_x = 103 #7
size_y = 101 #11
"""
for _ in range(100):
    for par in parsed:
        par[0] = ((par[0][0] + par[1][0]) % size_y, (par[0][1] + par[1][1]) % size_x)

for i in range(size_x):
    line = ""
    for j in range(size_y):
        count = 0
        for par in parsed:
            if (j, i) == par[0]:
                count += 1
        line += "." if count == 0 else str(count)
    print(line)

result = 0
for i in range(size_x//2):
    for j in range(size_y//2):
        for par in parsed:
            if (j, i) == par[0]:
                result += 1
print(f"First : {result}")

temp = 0
for i in range(size_x//2 + 1, size_x):
    for j in range(size_y//2 + 1, size_y):
        for par in parsed:
            if (j, i) == par[0]:
                temp += 1

print(f"{temp}")
result *= temp

temp = 0
for i in range(size_x//2):
    for j in range(size_y//2 + 1, size_y):
        for par in parsed:
            if (j, i) == par[0]:
                temp += 1
result *= temp
print(temp)

temp = 0
for i in range(size_x//2 + 1, size_x):
    for j in range(size_y//2):
        for par in parsed:
            if (j, i) == par[0]:
                print(f"{j}  {i}")
                temp += 1
result *= temp
print(temp)

print(result)"""

print("----- PART 2 -----")

print(parsed2)

image = False
turn = 0
while not image:
    pos = set()
    image = True
    for par in parsed:
        par[0] = ((par[0][0] + par[1][0]) % size_y, (par[0][1] + par[1][1]) % size_x)
        if par[0] in pos:
            image = False
        pos.add(par[0])
    turn += 1

print(turn)
for i in range(size_x):
    line = ""
    for j in range(size_y):
        count = 0
        for par in parsed:
            if (j, i) == par[0]:
                count += 1
        line += "." if count == 0 else str(count)
    print(line)
