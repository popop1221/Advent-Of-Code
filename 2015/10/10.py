def conway(old):
    result = ""
    prev = "0"
    count = 0
    for char in old:
        if char != prev and count != 0:
            result += str(count) + prev
            count = 0
        prev = char
        count += 1
    result += str(count) + prev
    return result

inputt = "1321131112"

for _ in range(40):
    inputt = conway(inputt)

print(len(inputt))

print("----- PART 2 -----")


for _ in range(10):
    inputt = conway(inputt)

print(len(inputt))
