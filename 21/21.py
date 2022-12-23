with open('input.txt') as f:
    lines = f.readlines()

with open('test_inputs') as f:
    test_input = f.readlines()


monkeys = {}
for line in lines:
#for line in test_input:
    line = line.replace("\n", "")
    temp = line.split(" ")
    if len(temp) == 2:
        monkeys[temp[0].replace(":", "")] = int(temp[1])
    else:
        monkeys[temp[0].replace(":", "")] = [temp[1], temp[2], temp[3]]

know = {}
while type(monkeys["root"]) is not int and type(monkeys["root"]) is not float:
    for monkey in monkeys.keys():
        if type(monkeys[monkey]) is int or type(monkeys[monkey]) is float:
            know[monkey] = monkeys[monkey]
            continue
        temp = monkeys[monkey]
        if temp[0] in know.keys() and temp[2] in know.keys():
            value = 0
            if temp[1] == "+":
                value = know[temp[0]] + know[temp[2]]
            elif temp[1] == "-":
                value = know[temp[0]] - know[temp[2]]
            elif temp[1] == "/":
                value = know[temp[0]] / know[temp[2]]
            else:
                value = know[temp[0]] * know[temp[2]]
            know[monkey] = value
            monkeys[monkey] = value

print(monkeys["root"])

print("----- PART 2 -----")
x = 0
last_left = -1
while True:
    monkeys = {}
    for line in lines:
    #for line in test_input:
        line = line.replace("\n", "")
        temp = line.split(" ")
        if len(temp) == 2:
            if temp[0] == "humn:":
                monkeys["humn"] = x
            else:
                monkeys[temp[0].replace(":", "")] = int(temp[1])
        else:
            if temp[0] == "root:":
                to_compare = (temp[1], temp[3])
            monkeys[temp[0].replace(":", "")] = [temp[1], temp[2], temp[3]]

    know = {}
    while type(monkeys["root"]) is not int and type(monkeys["root"]) is not float:
        for monkey in monkeys.keys():
            if type(monkeys[monkey]) is int or type(monkeys[monkey]) is float:
                know[monkey] = monkeys[monkey]
                continue
            temp = monkeys[monkey]
            if temp[0] in know.keys() and temp[2] in know.keys():
                value = 0
                if temp[1] == "+":
                    value = know[temp[0]] + know[temp[2]]
                elif temp[1] == "-":
                    value = know[temp[0]] - know[temp[2]]
                elif temp[1] == "/":
                    value = know[temp[0]] / know[temp[2]]
                else:
                    value = know[temp[0]] * know[temp[2]]
                know[monkey] = value
                monkeys[monkey] = value
    if last_left != -1:
        diff = last_left - monkeys[to_compare[0]]
        if diff != 0.0:
            x += (monkeys[to_compare[0]] - monkeys[to_compare[1]]) // diff

    last_left = monkeys[to_compare[0]]
    if monkeys[to_compare[0]] == monkeys[to_compare[1]]:
        break
    x += 1

print(monkeys["humn"])
