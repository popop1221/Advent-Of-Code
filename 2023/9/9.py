with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input

result = 0
for line in inputt:
    line = line.replace("\n", "")
    temp = [int(value) for value in line.split(" ")]

    stages = [temp]
    while len(set(stages[-1])) != 1:
        new = []
        for i in range(len(stages[-1])-1):
            new.append(stages[-1][i+1] - stages[-1][i])

        stages.append(new)
    stages[-1].append(stages[-1][-1])
    for i in range(len(stages)-1):
        stages[len(stages)-2-i].append(stages[len(stages)-2-i][-1] + stages[len(stages)-2-i+1][-1])
    result += stages[0][-1]

print(result)

print("----- PART 2 -----")
result = 0
for line in inputt:
    line = line.replace("\n", "")
    temp = [int(value) for value in line.split(" ")]

    stages = [temp]
    while len(set(stages[-1])) != 1:
        print(stages)
        new = []
        for i in range(len(stages[-1])-1):
            new.append(stages[-1][i+1] - stages[-1][i])

        stages.append(new)
    print(stages)
    stages[-1].insert(0, stages[-1][0])
    for i in range(len(stages)-1):
        print(f"{i}       {len(stages)-2-i}  {len(stages)-2-i+1}")
        stages[len(stages)-2-i].insert(0, stages[len(stages)-2-i][0] - stages[len(stages)-2-i+1][0])
    print(stages)
    print(f"Result temp : {stages[0][-1]}")
    result += stages[0][0]

print(result)