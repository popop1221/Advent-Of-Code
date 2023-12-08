import math

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input

network = {}
way = ""
step = 0
for line in inputt:
    line = line.replace("\n", "")
    if step == 0:
        step += 1
        way = line
        continue
    if step == 1:
        step += 1
        continue
    temp = line.split(" ")

    network[temp[0]] = (temp[2].replace("(", "").replace(",", ""), temp[3].replace(")", ""))

print(network)
print(way)


def evaluaute(node, i):
    print(f"We are at {node} {i} {way[i % len(way)]}")
    if node == "ZZZ":
        return i
    if way[i % len(way)] == "R":
        return evaluaute(network[node][1], i + 1)
    else:
        return evaluaute(network[node][0], i + 1)


# print(evaluaute("AAA", 0))

print("----- PART 2 -----")

def evaluaute_2(node, i):
    while True:
        if node.endswith("Z"):
            return i
        if way[i % len(way)] == "R":
            node = network[node][1]
            i += 1
        else:
            node = network[node][0]
            i += 1


nodes = [node for node in network.keys() if node.endswith("A")]
temp = []
for node in nodes:
    temp.append(evaluaute_2(node, 0))
print(math.lcm(*temp))
