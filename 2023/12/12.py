with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input


def replaceJ(input, i, result):
    if i == len(input):
        result.append(input)
        return

    if input[i] == '?':
        for rep in '.#':
            replaceJ(input[:i] + rep + input[i + 1:], i + 1, result)
        return
    replaceJ(input, i + 1, result)


def evaluate(way, to_have):
    temp = way.split(".")
    if len(to_have) != len([te for te in temp if te != ""]):
        return 0
    i = 0
    for t in [te for te in temp if te != ""]:
        if len(t) != int(to_have[i]):
            return 0
        i += 1
    return 1


result = 0
for line in inputt:
    line = line.replace("\n", "")
    print(f"{line}  {result}")
    temp = line.split(" ")
    to_test = []
    replaceJ(temp[0], 0, to_test)
    for test in to_test:
        result += evaluate(test, temp[1].split(","))

print(result)

print("----- PART 2 -----")


def evaluate_2(linee, to_have, pos, pos_to_have, passed, memo):
    if (pos, pos_to_have, passed) in memo:
        return memo[(pos, pos_to_have, passed)]

    if pos >= len(linee) and pos_to_have >= len(to_have):
        return 1

    if pos >= len(linee):
        return 0

    if linee[pos] == "?":
        temp = evaluate_2(linee, to_have, pos + 1, pos_to_have, passed + 1, memo)
        if pos_to_have < len(to_have) and to_have[pos_to_have] == passed:
            temp += evaluate_2(linee, to_have, pos + 1, pos_to_have + 1, 0, memo)
        if passed == 0:
            temp += evaluate_2(linee, to_have, pos + 1, pos_to_have, 0, memo)
        memo[(pos, pos_to_have, passed)] = temp
        return temp

    if linee[pos] == "#":
        temp = evaluate_2(linee, to_have, pos + 1, pos_to_have, passed + 1, memo)
        memo[(pos, pos_to_have, passed)] = temp
        return temp

    # dot
    if pos_to_have < len(to_have) and to_have[pos_to_have] == passed:
        temp = evaluate_2(linee, to_have, pos + 1, pos_to_have + 1, 0, memo)
        memo[(pos, pos_to_have, passed)] = temp
        return temp

    if passed != 0:
        return 0

    temp = evaluate_2(linee, to_have, pos + 1, pos_to_have, 0, memo)
    memo[(pos, pos_to_have, passed)] = temp
    return temp


result = 0
i = 0
for line in inputt:
    i += 1
    line = line.replace("\n", "")
    print(f"{i} {line}  {result}")
    temp = line.split(" ")
    old = line.split(" ")
    for _ in range(4):
        temp[1] += "," + old[1]
        temp[0] += "?" + old[0]
    print(f"New : {i} {temp}  {result}")
    result += evaluate_2(temp[0] + ".", [int(t) for t in temp[1].split(",")], 0, 0, 0, {})

print(result)
