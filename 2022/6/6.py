with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    line.replace("\n", "")
    # line = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    result = 4
    recent = [line[3], line[2], line[1], line[0]]
    while 1 in [(1 if recent.count(i) != 1 else 0) for i in recent]:
        recent.pop()
        recent = [line[result]] + recent
        result += 1
    print(result)

print("----- PART 2 -----")
for line in lines:
    line.replace("\n", "")
    result = 14
    recent = [line[13], line[12], line[11], line[10], line[9], line[8], line[7], line[6], line[5], line[4], line[3],
              line[2], line[1], line[0]]
    while 1 in [(1 if recent.count(i) != 1 else 0) for i in recent]:
        recent.pop()
        recent = [line[result]] + recent
        result += 1
    print(result)
