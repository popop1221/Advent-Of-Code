import sys

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input

data = {"children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1}

for line in inputt:
    line = line.replace("\n", "")
    valid = True
    for val in line.split(","):
        temp = [strr.replace(" ", "") for strr in val.split(": ")]
        if len(temp) == 3:
            temp.pop(0)
        if data[temp[0]] != int(temp[1]):
            valid = False
            break
    if valid:
        print(line)

print("----- PART 2 -----")

for line in inputt:
    line = line.replace("\n", "")
    valid = True
    for val in line.split(","):
        temp = [strr.replace(" ", "") for strr in val.split(": ")]
        if len(temp) == 3:
            temp.pop(0)
        if temp[0] in ["cats", "trees"]:
            if data[temp[0]] >= int(temp[1]):
                valid = False
                break
        elif temp[0] in ["pomeranians", "goldfish"]:
            if data[temp[0]] <= int(temp[1]):
                valid = False
                break
        elif data[temp[0]] != int(temp[1]):
            valid = False
            break
    if valid:
        print(line)
