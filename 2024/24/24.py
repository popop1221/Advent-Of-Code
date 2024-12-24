import sys
from copy import copy
from itertools import combinations, permutations

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

system = {}
step = 0
for line in inputt:
    if line == "":
        step += 1
        continue
    if step == 0:
        sp = line.split(": ")
        system[sp[0]] = int(sp[1])
        continue
    sp = line.split(" ")
    system[sp[4]] = (sp[0], sp[1], sp[2])


def evaluate(system):
    change = True
    while change:
        change = False
        for elem in copy(system):
            if type(system[elem]) == int:
                continue
            to_eval = system[elem]
            if to_eval[0] in system and type(system[to_eval[0]]) == int and to_eval[2] in system and type(
                    system[to_eval[2]]) == int:
                change = True
                if to_eval[1] == "AND":
                    system[elem] = system[to_eval[0]] & system[to_eval[2]]
                elif to_eval[1] == "OR":
                    system[elem] = system[to_eval[0]] | system[to_eval[2]]
                else:
                    system[elem] = system[to_eval[0]] ^ system[to_eval[2]]


evaluate(system)
print(system)
result = 0
for elem in system:
    if elem.startswith("z") and system[elem] == 1:
        result = result | (1 << int(elem.replace("z", "")))

print(f"Res part 1 : {result}")
val_x = 0
val_y = 0
for elem in system:
    if elem.startswith("x") and system[elem] == 1:
        val_x = val_x | (1 << int(elem.replace("x", "")))
    if elem.startswith("y") and system[elem] == 1:
        val_y = val_y | (1 << int(elem.replace("y", "")))

print(f"x : {val_x}    y : {val_y}")
print(f"bin x :  {bin(val_x)}")
print(f"bin y :  {bin(val_y)}")
print(f"res + : {bin(result)}")
print(f"excep : {bin(val_y + val_x)}")

print("----- PART 2 -----")

system2 = {}
step = 0
to_change = {"fdv": "dbp", "dbp": "fdv", "z23": "kdf", "kdf": "z23", "z39": "rpp", "rpp": "z39", "z15": "ckj",
             "ckj": "z15"}
print(to_change.keys())
for line in inputt:
    if line == "":
        step += 1
        continue
    if step == 0:
        sp = line.split(": ")
        system2[sp[0]] = int(sp[1])
        continue
    sp = line.split(" ")
    if sp[4] in to_change:
        print(sp[4])
    system2[sp[4] if sp[4] not in to_change else to_change[sp[4]]] = (sp[0], sp[1], sp[2])

print(system2)
evaluate(system2)
print(system2)
val_x = 0
val_y = 0
result = 0
for elem in system2:
    if elem.startswith("x") and system2[elem] == 1:
        val_x = val_x | (1 << int(elem.replace("x", "")))
    if elem.startswith("y") and system2[elem] == 1:
        val_y = val_y | (1 << int(elem.replace("y", "")))
    if elem.startswith("z") and system2[elem] == 1:
        result = result | (1 << int(elem.replace("z", "")))

print(f"x : {val_x}    y : {val_y}")
print(f"bin x :  {bin(val_x)}")
print(f"bin y :  {bin(val_y)}")
print(f"res + : {bin(result)}  {result}")
print(f"excep : {bin(val_y + val_x)}  {val_x + val_y}")
print(sorted(to_change.keys()))

with open('input.txt') as f:
    with open('input2.txt', "w") as f2:
        real_input = f.readlines()
        todo_later = []
        modified = {}
        for line in real_input:
            if ":" in line or line == "\n":
                f2.write(line)
                continue
            sp = line.split(" ")
            if sp[0][0] not in "xy" or sp[0][0] == sp[2][0]:
                todo_later.append(line)
                continue
            f2.write(f"{sp[0]} {sp[1]} {sp[2]} {sp[3]} {sp[1]}{sp[0][1:]}\n")
            modified[sp[4].replace("\n", "")] = f"{sp[1]}{sp[0][1:]}"
        print(modified)
        for todo in todo_later:
            sp = todo.split(" ")
            f2.write(
                f"{sp[0] if sp[0] not in modified else modified[sp[0]]} {sp[1]} {sp[2] if sp[2] not in modified else modified[sp[2]]} {sp[3]} {sp[4] if sp[4] not in modified else modified[sp[4]]}")
