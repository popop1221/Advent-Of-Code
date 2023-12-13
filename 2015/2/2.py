with open('input.txt') as f:
    real_input = f.readlines()

inputt = real_input

result = 0
for line in inputt:
    line = line.replace("\n", "")
    temp = [int(t) for t in line.split("x")]
    result += 2 * temp[0] * temp[1] + 2 * temp[1] * temp[2] + 2 * temp[2] * temp[0]
    result += min(temp[0] * temp[1], temp[1] * temp[2], temp[2] * temp[0])

print(result)

print("----- PART 2 -----")

result = 0
for line in inputt:
    line = line.replace("\n", "")
    temp = [int(t) for t in line.split("x")]
    temp.sort()
    result += temp[0] * temp[1] * temp[2]
    result += temp[0] * 2 + temp[1] * 2

print(result)
