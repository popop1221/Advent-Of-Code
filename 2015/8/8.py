with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input

result = 0
for line in inputt:
    line = line.replace("\n", "")
    result += len(line) - len(eval(line))

print(result)

print("----- PART 2 -----")

result2 = 0
for line in inputt:
    line = line.replace("\n", "")
    result2 += len(line) + line.count("\"") + line.count("\\") + 2
    result2 -= len(eval(line))

print(result2 - result)
