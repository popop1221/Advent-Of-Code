with open('input.txt') as f:
    lines = f.readlines()

with open('test_inputs.txt') as f:
    test_inputs = f.readlines()

monkeys = {}

monkey_id = 0
line_id = 0
monkey_temp = {"inspect" : 0}
for line in lines:
#for line in test_inputs:
    line = line.replace("\n", "")

    if line == "":
        monkeys[monkey_id] = monkey_temp
        monkey_id += 1
        monkey_temp = {"inspect" : 0}
        line_id = 0
        continue

    if line_id == 1:
        monkey_temp["items"] = [int(i) for i in line.replace(",", "").split(" ")[4:]]

    if line_id == 2:
        operation = line.split(" ")
        monkey_temp["operation"] = operation

    if line_id == 3:
        monkey_temp["divisible_by"] = int(line.split(" ")[5])
    if line_id == 4:
        monkey_temp["true"] = int(line.split(" ")[9])
    if line_id == 5:
        monkey_temp["false"] = int(line.split(" ")[9])
    line_id += 1

for i in range(20):
    for mon in monkeys:
        operation = monkeys[mon]["operation"]
        if operation[6] == "*":
            ope = lambda a: ((a if (operation[5]) == "old" else int(operation[5])) * (a if operation[7] == "old" else int(operation[7])))
        else:
            ope = lambda a: ((a if operation[5] == "old" else int(operation[5])) + (
                a if operation[7] == "old" else int(operation[7])))

        while len(monkeys[mon]["items"]) != 0:
            monkeys[mon]["inspect"] += 1
            item = monkeys[mon]["items"].pop(0)
            item = ope(item)
            item //= 3
            if item % monkeys[mon]["divisible_by"] == 0:
                monkeys[monkeys[mon]["true"]]["items"].append(item)
            else:
                monkeys[monkeys[mon]["false"]]["items"].append(item)

final = []
for mon in monkeys:
    final.append(monkeys[mon]["inspect"])

temp = max(final)
final.pop(final.index(temp))
print(max(final) * temp)

print("----- PART 2 -----")
monkeys = {}

monkey_id = 0
line_id = 0
monkey_temp = {"inspect" : 0}
for line in lines:
#for line in test_inputs:
    line = line.replace("\n", "")

    if line == "":
        monkeys[monkey_id] = monkey_temp
        monkey_id += 1
        monkey_temp = {"inspect" : 0}
        line_id = 0
        continue

    if line_id == 1:
        monkey_temp["items"] = [int(i) for i in line.replace(",", "").split(" ")[4:]]

    if line_id == 2:
        operation = line.split(" ")
        monkey_temp["operation"] = operation

    if line_id == 3:
        monkey_temp["divisible_by"] = int(line.split(" ")[5])
    if line_id == 4:
        monkey_temp["true"] = int(line.split(" ")[9])
    if line_id == 5:
        monkey_temp["false"] = int(line.split(" ")[9])
    line_id += 1

for i in range(10000):
    for mon in monkeys:
        operation = monkeys[mon]["operation"]
        if operation[6] == "*":
            ope = lambda a: ((a if (operation[5]) == "old" else int(operation[5])) * (a if operation[7] == "old" else int(operation[7])))
        else:
            ope = lambda a: ((a if operation[5] == "old" else int(operation[5])) + (
                a if operation[7] == "old" else int(operation[7])))

        while len(monkeys[mon]["items"]) != 0:
            monkeys[mon]["inspect"] += 1
            item = monkeys[mon]["items"].pop(0)
            item = ope(item)
            item = item % 9699690
            if item % monkeys[mon]["divisible_by"] == 0:
                monkeys[monkeys[mon]["true"]]["items"].append(item)
            else:
                monkeys[monkeys[mon]["false"]]["items"].append(item)

final = []
for mon in monkeys:
    final.append(monkeys[mon]["inspect"])

temp = max(final)
final.pop(final.index(temp))
print(max(final) * temp)