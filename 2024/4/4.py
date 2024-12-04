import sys

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

letters = ['X', 'M', 'A', 'S']


def evaluate(pos, dir, last_letter):
    if last_letter == 'S':
        return 1
    new_pos = (pos[0] + dir[0], pos[1] + dir[1])
    if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= len(inputt) or new_pos[1] >= len(inputt[1]):
        return 0
    if letters.index(last_letter) + 1 == letters.index(inputt[new_pos[0]][new_pos[1]]):
        return evaluate(new_pos, dir, inputt[new_pos[0]][new_pos[1]])
    return 0


result = 0
parsed = []
dirs = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1)]
for i in range(len(inputt)):
    for j in range(len(inputt[i])):
        if inputt[i][j] != 'X':
            continue
        for dir in dirs:
            result += evaluate((i, j), dir, 'X')

print(result)

print("----- PART 2 -----")

result = 0
for i in range(len(inputt)):
    for j in range(len(inputt[i])):
        if inputt[i][j] != 'A':
            continue
        if i <= 0 or j <= 0 or i + 1 >= len(inputt) or j + 1 >= len(inputt):
            continue
        result += inputt[i - 1][j - 1] == 'M' and inputt[i - 1][j + 1] == 'S' and inputt[i + 1][j - 1] == 'M' and \
                  inputt[i + 1][j + 1] == 'S'
        # TL and  TR and BL and BR
        result += inputt[i - 1][j - 1] == 'S' and inputt[i - 1][j + 1] == 'M' and inputt[i + 1][j - 1] == 'S' and \
                  inputt[i + 1][j + 1] == 'M'

        result += inputt[i - 1][j - 1] == 'M' and inputt[i - 1][j + 1] == 'M' and inputt[i + 1][j - 1] == 'S' and \
                  inputt[i + 1][j + 1] == 'S'

        result += inputt[i - 1][j - 1] == 'S' and inputt[i - 1][j + 1] == 'S' and inputt[i + 1][j - 1] == 'M' and \
                  inputt[i + 1][j + 1] == 'M'

print(result)
