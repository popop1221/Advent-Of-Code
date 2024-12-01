import math

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

modules = {}
for line in inputt:
    name = "broadcaster" if line.startswith("broadcaster") else line[1:3]
    childs = line.split(">")[1].replace(" ", "").split(",")
    type = 0 if name == "broadcaster" else 1 if line.startswith("%") else 2
    modules[name] = [childs, type]

print(modules)
for module in modules:
    modules[module].append([False for i in range(1 if modules[module][1] == 1 else 0)])
    if modules[module][1] == 2:
        modules[module].append([])

for module in modules:
    for child in modules[module][0]:
        if child not in modules:
            continue

        if modules[child][1] == 2:
            modules[child][2].append(module)
            modules[child][3].append(False)
print(modules)

result1 = 0
result2 = 0
for _ in range(1000):
    queue = []  # node, pulse_is_high, parent
    queue.append(("broadcaster", False, None))
    while queue:
        elem = queue.pop(0)
        print(f"{elem[2]} -{elem[1]}> {elem[0]}")
        if elem[1]:
            result1 += 1
        else:
            result2 += 1

        if elem[0] not in modules:
            continue

        if modules[elem[0]][1] == 0:
            for child in modules[elem[0]][0]:
                queue.append((child, elem[1], elem[0]))
            continue

        if modules[elem[0]][1] == 1:
            if elem[1]:
                continue

            modules[elem[0]][2][0] = not modules[elem[0]][2][0]
            for child in modules[elem[0]][0]:
                queue.append((child, modules[elem[0]][2][0], elem[0]))
            continue

        modules[elem[0]][3][modules[elem[0]][2].index(elem[2])] = elem[1]
        new_pulse = len(["1" for t in modules[elem[0]][3] if not t]) != 0
        for child in modules[elem[0]][0]:
            queue.append((child, new_pulse, elem[0]))

print(result1)
print(result2)
print(result1 * result2)

print("----- PART 2 -----")


def modules_reset():
    modules = {}
    for line in inputt:
        name = "broadcaster" if line.startswith("broadcaster") else line[1:3]
        childs = line.split(">")[1].replace(" ", "").split(",")
        type = 0 if name == "broadcaster" else 1 if line.startswith("%") else 2
        modules[name] = [childs, type]

    for module in modules:
        modules[module].append([False for i in range(1 if modules[module][1] == 1 else 0)])
        if modules[module][1] == 2:
            modules[module].append([])

    for module in modules:
        for child in modules[module][0]:
            if child not in modules:
                continue

            if modules[child][1] == 2:
                modules[child][2].append(module)
                modules[child][3].append(False)
    print(modules)
    return modules


"""
&rs -> rx
'rs': [['rx'], 2, ['bt', 'dl', 'fr', 'rv'], [False, False, False, False]]
"""


def evaluate(node):
    result = 0
    while True:
        result += 1
        queue = []  # node, pulse_is_high, parent
        queue.append(("broadcaster", False, None))
        while queue:
            elem = queue.pop(0)

            if elem[0] not in modules:
                continue

            if modules[elem[0]][1] == 0:
                for child in modules[elem[0]][0]:
                    queue.append((child, elem[1], elem[0]))
                continue

            if modules[elem[0]][1] == 1:
                if elem[1]:
                    continue

                modules[elem[0]][2][0] = not modules[elem[0]][2][0]
                for child in modules[elem[0]][0]:
                    queue.append((child, modules[elem[0]][2][0], elem[0]))
                continue

            modules[elem[0]][3][modules[elem[0]][2].index(elem[2])] = elem[1]
            new_pulse = len(["1" for t in modules[elem[0]][3] if not t]) != 0
            if new_pulse and elem[0] == node:
                print(result)
                return result
            for child in modules[elem[0]][0]:
                queue.append((child, new_pulse, elem[0]))

        if not modules[node][3][0]:
            return result


modules = modules_reset()
print(evaluate("dl"))
modules = modules_reset()
print(evaluate("bt"))
modules = modules_reset()
print(evaluate("fr"))
modules = modules_reset()
print(evaluate("rv"))
print(math.lcm(4001, 3739, 3943, 3821))
