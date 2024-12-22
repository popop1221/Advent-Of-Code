import sys
from copy import copy

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

def evaluate(secret):
    secret = (secret ^ (secret * 64)) % 16777216
    secret = (secret ^ ((secret // 32) % 2**64)) % 16777216
    secret = (secret ^ (secret * 2048)) % 16777216
    return secret

result = 0
for line in inputt:
    temp = int(line)
    for _ in range(2000):
        temp = evaluate(temp)
    result += temp

print(result)

print("----- PART 2 -----")

deltas = [copy([]) for _ in range(len(inputt))]
deltas_dic = [copy({}) for _ in range(len(inputt))]

for line in inputt:
    print(f"Part 2 : {line} - {inputt.index(line)}")
    temp = int(line)
    temp3 = temp % 10
    for i in range(2000):
        temp2 = evaluate(temp)
        deltas[inputt.index(line)].append(-(temp3 - (temp2 % 10)))
        temp = temp2
        temp3 = temp % 10

        if i >= 4:
            temp4 = deltas[inputt.index(line)][-4:]
            if (temp4[0], temp4[1], temp4[2], temp4[3]) not in deltas_dic[inputt.index(line)].keys():
                deltas_dic[inputt.index(line)][(temp4[0], temp4[1], temp4[2], temp4[3])] = temp3

#print(deltas)
#print(deltas_dic)

result = 0
best_slice = []
for i in range(len(deltas_dic)):
    print(f"Part 2-2 : {i}")
    for slice in deltas_dic[i].keys():
        temp = 0
        for j in range(len(deltas_dic)):
            if slice in deltas_dic[j].keys():
                temp += deltas_dic[j][slice]
        if temp > result:
            result = temp
            best_slice = slice
            print(result)
            print(best_slice)

print(result)
print(best_slice)