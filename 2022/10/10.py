with open('input.txt') as f:
    lines = f.readlines()

test_inputs = ["addx 15",
               "addx -11",
               "addx 6",
               "addx -3",
               "addx 5",
               "addx -1",
               "addx -8",
               "addx 13",
               "addx 4",
               "noop",
               "addx -1",
               "addx 5",
               "addx -1",
               "addx 5",
               "addx -1",
               "addx 5",
               "addx -1",
               "addx 5",
               "addx -1",
               "addx -35",
               "addx 1",
               "addx 24",
               "addx -19",
               "addx 1",
               "addx 16",
               "addx -11",
               "noop",
               "noop",
               "addx 21",
               "addx -15",
               "noop",
               "noop",
               "addx -3",
               "addx 9",
               "addx 1",
               "addx -3",
               "addx 8",
               "addx 1",
               "addx 5",
               "noop",
               "noop",
               "noop",
               "noop",
               "noop",
               "addx -36",
               "noop",
               "addx 1",
               "addx 7",
               "noop",
               "noop",
               "noop",
               "addx 2",
               "addx 6",
               "noop",
               "noop",
               "noop",
               "noop",
               "noop",
               "addx 1",
               "noop",
               "noop",
               "addx 7",
               "addx 1",
               "noop",
               "addx -13",
               "addx 13",
               "addx 7",
               "noop",
               "addx 1",
               "addx -33",
               "noop",
               "noop",
               "noop",
               "addx 2",
               "noop",
               "noop",
               "noop",
               "addx 8",
               "noop",
               "addx -1",
               "addx 2",
               "addx 1",
               "noop",
               "addx 17",
               "addx -9",
               "addx 1",
               "addx 1",
               "addx -3",
               "addx 11",
               "noop",
               "noop",
               "addx 1",
               "noop",
               "addx 1",
               "noop",
               "noop",
               "addx -13",
               "addx -19",
               "addx 1",
               "addx 3",
               "addx 26",
               "addx -30",
               "addx 12",
               "addx -1",
               "addx 3",
               "addx 1",
               "noop",
               "noop",
               "noop",
               "addx -9",
               "addx 18",
               "addx 1",
               "addx 2",
               "noop",
               "noop",
               "addx 9",
               "noop",
               "noop",
               "noop",
               "addx -1",
               "addx 2",
               "addx -37",
               "addx 1",
               "addx 3",
               "noop",
               "addx 15",
               "addx -21",
               "addx 22",
               "addx -6",
               "addx 1",
               "noop",
               "addx 2",
               "addx 1",
               "noop",
               "addx -10",
               "noop",
               "noop",
               "addx 20",
               "addx 1",
               "addx 2",
               "addx 2",
               "addx -6",
               "addx -11",
               "noop",
               "noop",
               "noop", ]

# test_inputs = ["noop", "addx 3", "addx -5"]


x = 1
cycle = 0

result = 0
for line in lines:
    # for line in test_inputs:
    line.replace("\n", "")
    cycle += 1
    if cycle in [20, 60, 100, 140, 180, 220]:
        result += (cycle * x)
    if line.startswith("addx"):
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            result += (cycle * x)
        x += int(line.split(" ")[1])

print(result)

print("----- PART 2 -----")
x = 1
cycle = 0
pos = 0
for line in lines:
#for line in test_inputs:
    line.replace("\n", "")
    cycle += 1
    if cycle in [40, 80, 120, 160, 200, 240]:
        print("#" if (x - 1) <= pos <= (x + 1) else " ")
        pos = 0
    else:
        print("#" if (x - 1) <= pos <= (x + 1) else " ", end=f'')
    pos += 1
    if line.startswith("addx"):
        cycle += 1
        x += int(line.split(" ")[1])
        if cycle in [40, 80, 120, 160, 200, 240]:
            print("#" if (x - 1) <= pos <= (x + 1) else " ")
            pos = 0
        else:
            print("#" if (x - 1) <= pos <= (x + 1) else " ", end='')
        pos += 1
