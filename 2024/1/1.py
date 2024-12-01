import sys

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

list1 = []
list2 = []
for line in inputt:
    linesplited = line.split(" ")
    print(linesplited)
    list1.append(int(linesplited[0]))
    list2.append(int(linesplited[3]))
list1.sort()
list2.sort()
result = 0
for i in range(len(list1)):
    result += abs(list1[i] - list2[i])
print(result)
print("----- PART 2 -----")

result = 0
for elem in list1:
    result += list2.count(elem) * elem
print(result)
