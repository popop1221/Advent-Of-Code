with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input


def generate_paths(cities):
    if len(cities) == 1:
        return [cities]

    result = []
    for i in range(len(cities)):
        curr = cities[i]
        other = cities[:i] + cities[i + 1:]
        for permutation in generate_paths(other):
            result.append([curr] + permutation)
    return result


labels = []
graph = []
for line in inputt:
    line = line.replace("\n", "")
    temp = line.split(" ")
    print(temp)
    if temp[0] not in labels:
        labels.append(temp[0])
        graph.append([])
    if temp[2] not in labels:
        labels.append(temp[2])
        graph.append([])
    graph[labels.index(temp[0])].append((temp[2], int(temp[4])))
    graph[labels.index(temp[2])].append((temp[0], int(temp[4])))

print(labels)
print(graph)
print(generate_paths(labels))

result = 9999999999
result2 = 0
for path in generate_paths(labels):
    temp = 0
    for i in range(1, len(path)):
        index = labels.index(path[i - 1])
        for j in range(len(path) - 1):
            if graph[index][j][0] == path[i]:
                temp += graph[index][j][1]
                break
    result = min(result, temp)
    result2 = max(result2, temp)
    print(f"{path} = {temp}")

print(result)

print("----- PART 2 -----")

print(result2)
