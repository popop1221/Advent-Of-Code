import sys
import re

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

pattern = r"mul\(\d+,\d+\)"
result = 0
for line in inputt:
    for mul in re.findall(pattern, line):
        mul = mul.replace("mul(", "")
        mul = mul.replace(")", "")
        sp = mul.split(",")
        result += int(sp[0]) * int(sp[1])

print(result)

print("----- PART 2 -----")

pattern = r"(mul\(\d+,\d+\)|do\(\)|don\'t\(\))"
result = 0
activate = True
for line in inputt:
    for mul in re.findall(pattern, line):
        print(mul)
        if mul == "do()":
            activate = True
            continue
        if mul == "don't()":
            activate = False
            continue
        if not activate:
            continue
        mul = mul.replace("mul(", "")
        mul = mul.replace(")", "")
        sp = mul.split(",")
        result += int(sp[0]) * int(sp[1])

print(result)
