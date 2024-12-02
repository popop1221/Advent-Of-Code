import sys

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

result = 0
for line in inputt:
    linesp = [int(i) for i in line.split(" ")]
    if linesp[0] < linesp[1]:
        linesp.reverse()
    prev = linesp[0]
    print(linesp)
    for i in linesp[1::]:
        delta = prev - i
        prev = i
        if delta < 1 or delta > 3:
            print(f"not safe for {i}  : {prev}")
            break
    else:
        print("safe")
        result += 1

print(result)

print("----- PART 2 -----")

result = 0
for line in inputt:
    len_line = len(line.split(" "))
    for brute_force in range(len_line):
        linesp = [int(i) for i in line.split(" ")]
        if brute_force < len_line:
            linesp.pop(brute_force)
        if linesp[0] < linesp[1]:
            linesp.reverse()
        prev = linesp[0]
        print(linesp)
        for i in linesp[1::]:
            delta = prev - i
            prev = i
            if delta < 1 or delta > 3:
                print(f"unsafe for {i}  {delta}")
                break
        else:
            result += 1
            break

print(result)
