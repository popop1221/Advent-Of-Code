import sys

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

parsed = inputt[0].split(", ")
parsed.sort(reverse=True)
print(parsed)

memo = {}
def evaluate(word):
    if word in memo.keys():
        return memo[word]
    for first in parsed:
        if word.startswith(first):
            if word[len(first):] == "":
                return True
            if evaluate(word[len(first):]):
                memo[word] = True
                return True
    memo[word] = False
    return False

result = 0
for line in inputt[2:]:
    result += evaluate(line)

print(result)

print("----- PART 2 -----")

memo2 = {}
def evaluate2(word):
    if word in memo2.keys():
        return memo2[word]
    res = 0
    for first in parsed:
        if word.startswith(first):
            if word[len(first):] == "":
                res += 1
            else:
                res += evaluate2(word[len(first):])
    memo2[word] = res
    return res

result = 0
for line in inputt[2:]:
    result += evaluate2(line)

print(result)
