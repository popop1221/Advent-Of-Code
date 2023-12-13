with open('input.txt') as f:
    real_input = f.readlines()

inputt = real_input[0].replace("\n", "")

result = 0
for char in inputt:
    if char == "(":
        result += 1
    else:
        result -= 1

print(result)

print("----- PART 2 -----")
result = 0
pos = 0
for char in inputt:
    pos += 1
    if char == "(":
        result += 1
    else:
        result -= 1

    if result < 0:
        print(pos)
        break
