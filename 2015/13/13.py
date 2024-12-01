with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input

parsed = {}
for line in inputt:
    line = line.replace("\n", "")
    temp = line.split(" ")

    if temp[0] not in parsed:
        parsed[temp[0]] = {}

    parsed[temp[0]][temp[10].replace(".", "")] = int(temp[3]) if temp[2] == "gain" else -int(temp[3])

print(parsed)


def generate_tables(peoples):
    if len(peoples) == 1:
        return [peoples]

    result = []
    for i in range(len(peoples)):
        curr = peoples[i]
        other = peoples[:i] + peoples[i + 1:]
        for permutation in generate_tables(other):
            result.append([curr] + permutation)
    return result


def evaluate(perm):
    result = 0
    for i in range(len(perm)):
        result += parsed[perm[i]][perm[i - 1]]
        result += parsed[perm[i]][perm[(i + 1) % len(perm)]]

    return result


result = 0
for perm in generate_tables(list(parsed.keys())):
    result = max(evaluate(perm), result)

print(result)

print("----- PART 2 -----")

parsed["Popop12"] = {}
for key in parsed.keys():
    parsed["Popop12"][key] = 0
    parsed[key]["Popop12"] = 0

result = 0
for perm in generate_tables(list(parsed.keys())):
    result = max(evaluate(perm), result)

print(result)
