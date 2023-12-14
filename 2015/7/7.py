with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input

to_process = []
for line in inputt:
    line = line.replace("\n", "")
    to_process.append(line.split(" "))


def evaluate(to_process):
    wires = {}
    while to_process:
        for i in range(len(to_process)):
            elem = to_process[i]
            if len(elem) == 3:
                if elem[0].isnumeric():
                    wires[elem[2]] = int(elem[0])
                    to_process.remove(elem)
                    break

                if elem[0] in wires.keys():
                    wires[elem[2]] = wires[elem[0]]
                    to_process.remove(elem)
                    break

            if len(elem) == 4 and (elem[1].isnumeric() or elem[1] in wires.keys()):
                temp = int(elem[1]) if elem[1].isnumeric() else wires[elem[1]]
                wires[elem[3]] = ~(temp & 0xFFFF) & 0xFFFF
                to_process.remove(elem)
                break

            if len(elem) == 5:
                if (elem[0].isnumeric() or elem[0] in wires.keys()) and (
                        elem[2].isnumeric() or elem[2] in wires.keys()):
                    elem1 = int(elem[0]) if elem[0].isnumeric() else wires[elem[0]]
                    elem2 = int(elem[2]) if elem[2].isnumeric() else wires[elem[2]]
                    if elem[1] == "OR":
                        wires[elem[4]] = (elem1 | elem2) & 0xFFFF
                    elif elem[1] == "AND":
                        wires[elem[4]] = (elem1 & elem2) & 0xFFFF
                    elif elem[1] == "RSHIFT":
                        wires[elem[4]] = (elem1 >> elem2) & 0xFFFF
                    elif elem[1] == "LSHIFT":
                        wires[elem[4]] = (elem1 << elem2) & 0xFFFF
                    to_process.remove(elem)
                    break
    return wires


wires = evaluate(to_process)
print(wires)
result = wires["a"]
print(result)

print("----- PART 2 -----")

to_process = []
for line in inputt:
    line = line.replace("\n", "")
    to_process.append(line.split(" "))

to_process.remove(["14146", "->", "b"])
to_process.append([str(result), "->", "b"])

wires = evaluate(to_process)
print(wires)
result = wires["a"]
print(result)
