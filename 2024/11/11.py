import sys

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt][0]

stones = inputt.split(" ")
for step in range(25):
    print(step)
    new_stones = []
    for i in range(len(stones)):
        if stones[i] == "0":
            new_stones.append("1")
            continue
        if len(stones[i]) % 2 == 0:
            new_stones.append(stones[i][:len(stones[i]) // 2])
            new_stones.append(str(int(stones[i][len(stones[i]) // 2:])))
            continue
        new_stones.append(str(2024 * int(stones[i])))
    stones = new_stones
    # print(new_stones)

print(stones)
print(len(stones))

print("----- PART 2 -----")

qcm8 = {}


def evaluate(stone, turn):
    if (stone, turn) in qcm8.keys():
        return qcm8[(stone, turn)]

    if turn == 76:
        return 1

    if stone == "0":
        res = evaluate("1", turn + 1)
        qcm8[(stone, turn)] = res
        return res

    if len(stone) % 2 == 0:
        res = evaluate(stone[:len(stone) // 2], turn + 1)
        res += evaluate(str(int(stone[len(stone) // 2:])), turn + 1)
        qcm8[(stone, turn)] = res
        return res

    res = evaluate(str(2024 * int(stone)), turn + 1)
    qcm8[(stone, turn)] = res
    return res


result = 0
stones = inputt.split(" ")
for stone in stones:
    result += evaluate(stone, 1)
print(result)
