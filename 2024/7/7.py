import sys

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]


def evaluate(needed, act, pos, numbs):
    if act == needed:
        return True
    if act > needed or pos >= len(numbs):
        return False
    return evaluate(needed, act + numbs[pos], pos + 1, numbs) or evaluate(needed, act * numbs[pos], pos + 1, numbs)


result = 0
for line in inputt:
    sp = line.split(": ")
    print(sp)
    needed = int(sp[0].replace(":", ""))
    numbers = [int(num) for num in sp[1].split(" ")]
    print(numbers)
    if evaluate(needed, numbers[0], 1, numbers):
        result += needed
print(result)

print("----- PART 2 -----")


def evaluate_2(needed, act, pos, numbs):
    if act == needed:
        return True
    if act > needed or pos >= len(numbs):
        return False

    return evaluate_2(needed, act + numbs[pos], pos + 1, numbs) \
           or evaluate_2(needed, int(str(act) + str(numbs[pos])), pos + 1, numbs) \
           or evaluate_2(needed, act * numbs[pos], pos + 1, numbs)


result = 0
for line in inputt:
    sp = line.split(": ")
    needed = int(sp[0].replace(":", ""))
    numbers = [int(num) for num in sp[1].split(" ")]
    if evaluate_2(needed, numbers[0], 1, numbers):
        result += needed
print(result)
