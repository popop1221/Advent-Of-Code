with open('input.txt') as f:
    lines = f.readlines()

with open('test_inputs') as f:
    test_input = f.readlines()

resultDec = 0
convMap = {"0": 0, "1": 1, "2": 2, "-": -1, "=": -2, 0: "0", 1: "1", 2: "2", -1: "-", -2: "="}
for line in lines:
#for line in test_input:
    line = line.replace("\n", "")

    temp = 0
    power5 = 1
    for char in reversed(line):
        temp += power5 * convMap[char]
        power5 *= 5
    resultDec += temp
print(resultDec)

inBase5 = ""
while resultDec != 0:
    inBase5 = str(resultDec % 5) + inBase5
    resultDec //= 5
resultDec = int(inBase5)

broch = {0: ("0", 0), 1: ("1", 0), 2: ("2", 0), 3: ("=", 1), 4: ("-", 1), 5: ("0", 1), 6: ("1", 1), 7: ("1", 1),
         8: ("=", 2), 9: ("-", 2), 10: ("2", 0)}
result = ""
temp = 0
while resultDec != 0:
    toAdd = resultDec % 10 + temp
    resultDec //= 10
    temp = broch[toAdd][1]
    result = broch[toAdd][0] + result
if temp != 0:
    result = broch[temp][0] + result

print(result)

print("----- PART 2 -----")
