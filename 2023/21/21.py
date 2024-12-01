import sys

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

parsed = []
start = (0, 0)
y = -1
for line in inputt:
    y += 1
    parsed.append([char for char in line])
    if "S" in line:
        start = (line.index("S"), y)

print(parsed)
print(start)

seen = set()


def evaluate(pos, step, result):
    if (pos, step) in seen:
        return

    seen.add((pos, step))

    if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(parsed[1]) or pos[1] >= len(parsed):
        return

    if parsed[pos[1]][pos[0]] == "#":
        return

    if step == 64:
        result.add(pos)
        return

    evaluate((pos[0] - 1, pos[1]), step + 1, result)
    evaluate((pos[0] + 1, pos[1]), step + 1, result)
    evaluate((pos[0], pos[1] - 1), step + 1, result)
    evaluate((pos[0], pos[1] + 1), step + 1, result)


result = set()
evaluate(start, 0, result)
print(result)
print(len(result))

print("----- PART 2 -----")

values = []
for i in [65, 196, 327]:
    seen = set()
    result = set()
    stack = [(start, 0)]
    while stack:
        elem = stack.pop()
        if elem in seen:
            continue

        seen.add(elem)

        if parsed[elem[0][1] % len(parsed)][elem[0][0] % len(parsed[1])] == "#":
            continue

        if elem[1] == i:
            result.add(elem[0])
            continue

        stack.append(((elem[0][0] - 1, elem[0][1]), elem[1] + 1))
        stack.append(((elem[0][0] + 1, elem[0][1]), elem[1] + 1))
        stack.append(((elem[0][0], elem[0][1] - 1), elem[1] + 1))
        stack.append(((elem[0][0], elem[0][1] + 1), elem[1] + 1))
    values.append(len(result))
    print(f"{i} : {len(result)}")
print(values)

# By hand and WolframAlpha after that
