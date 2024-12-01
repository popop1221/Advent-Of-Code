import sys
sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()


inputt = real_input

result = 0
for line in inputt:
    line = line.replace("\n", "")
    queue = [eval(line)]

    while queue:
        elem = queue.pop()
        if type(elem) is dict:
            for key in elem:
                queue.append(elem[key])

        if type(elem) is int:
            result += elem

        if type(elem) is list:
            for e in elem:
                queue.append(e)


print(result)

print("----- PART 2 -----")
result = 0
for line in inputt:
    line = line.replace("\n", "")
    queue = [eval(line)]

    while queue:
        elem = queue.pop()
        if type(elem) is dict and "red" not in [elem[t] for t in elem.keys()]:
            for key in elem:
                queue.append(elem[key])

        if type(elem) is int:
            result += elem

        if type(elem) is list:
            for e in elem:
                queue.append(e)


print(result)

