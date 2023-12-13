with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

patterns = [[]]
patterns_t = []
for line in inputt:
    if line == "":
        patterns_t.append([list(row) for row in zip(*patterns[-1])])
        patterns.append([])
        continue
    patterns[-1].append([char for char in line])
patterns_t.append([list(row) for row in zip(*patterns[-1])])

print(len(patterns))
print(len(patterns[-1]))


def evaluate(pattern, i):
    for j in range(len(pattern)):
        if 0 <= 2 * i - j - 1 < len(pattern) and pattern[j] != pattern[2 * i - j - 1]:
            return False
    return True


patterns_sym = {}
for pattern in range(len(patterns)):
    patterns_sym[pattern] = []

for pattern in patterns:
    for i in range(1, len(pattern)):
        if evaluate(pattern, i):
            patterns_sym[patterns.index(pattern)].append((i, "H"))
            print(f"Horizontal point at {i} for pattern {patterns.index(pattern)}")

for pattern in patterns_t:
    for i in range(1, len(pattern)):
        if evaluate(pattern, i):
            patterns_sym[patterns_t.index(pattern)].append((i, "V"))
            print(f"Vertical point in transpose at {i} for pattern {patterns_t.index(pattern)}")

result = 0
for i in patterns_sym.keys():
    temp = patterns_sym[i]
    if temp == []:
        print(f"no way for {i}")
        continue
    print(temp)

    if temp[0][1] == "H":
        result += 100 * temp[0][0]
    else:
        result += temp[0][0]

print(result)

print("----- PART 2 -----")


def evaluate_diff(pattern, i):
    diff = 0
    for j in range(len(pattern)):
        if 0 <= 2 * i - j + 1 < len(pattern) and pattern[j] != pattern[2 * i - j + 1]:
            for t in range(len(pattern[j])):
                if pattern[j][t] != pattern[2 * i - j + 1][t]:
                    diff += 1
    return diff / 2


patterns_sym = {}
for pattern in range(len(patterns)):
    patterns_sym[pattern] = []

for pattern in patterns:
    for i in range(len(pattern) - 1):
        if evaluate_diff(pattern, i) == 1:
            patterns_sym[patterns.index(pattern)].append((i + 1, "H"))

for pattern in patterns_t:
    for i in range(len(pattern) - 1):
        if evaluate_diff(pattern, i) == 1:
            patterns_sym[patterns_t.index(pattern)].append((i + 1, "V"))

result = 0
for i in patterns_sym.keys():
    temp = patterns_sym[i]

    if temp[0][1] == "H":
        result += 100 * temp[0][0]
    else:
        result += temp[0][0]

print(result)
