with open('input.txt') as f:
    lines = f.readlines()

stackOne = ["Z", "J", "N", "W", "P", "S"]
stack2 = ["G", "S", "T"]
stack3 = ["V", "Q", "R", "L", "H"]
stack4 = ["V", "S", "T", "D"]
stack5 = ["Q", "Z", "T", "D", "B", "M", "J", ]
stack6 = ["M", "W", "T", "J", "D", "C", "Z", "L"]
stack7 = ["L", "P", "M", "W", "G", "T", "J"]
stack8 = ["N", "G", "M", "T", "B", "F", "Q", "H"]
stack9 = ["R", "D", "G", "C", "P", "B", "Q", "W"]
stacks = [[], stackOne, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

for line in lines:
    temp = line.replace("\n", "").split(" ")
    for i in range(int(temp[1])):
        stacks[int(temp[5])].append(stacks[int(temp[3])].pop(-1))

print(
    f"{stackOne[-1]},    {stack2[-1]},    {stack3[-1]},    {stack4[-1]},    {stack5[-1]},    {stack6[-1]},    {stack7[-1]},    {stack8[-1]},    {stack9[-1]}")

print("----- PART 2 -----")

stackOne = ["Z", "J", "N", "W", "P", "S"]
stack2 = ["G", "S", "T"]
stack3 = ["V", "Q", "R", "L", "H"]
stack4 = ["V", "S", "T", "D"]
stack5 = ["Q", "Z", "T", "D", "B", "M", "J", ]
stack6 = ["M", "W", "T", "J", "D", "C", "Z", "L"]
stack7 = ["L", "P", "M", "W", "G", "T", "J"]
stack8 = ["N", "G", "M", "T", "B", "F", "Q", "H"]
stack9 = ["R", "D", "G", "C", "P", "B", "Q", "W"]
stacks = [[], stackOne, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

print(stacks)
for line in lines:
    temp = line.replace("\n", "").split(" ")

    stacks[int(temp[5])] += (stacks[int(temp[3])][-(int(temp[1])):])
    for i in range(int(temp[1])):
        stacks[int(temp[3])].pop()

print(
    f"{stackOne[-1]},    {stack2[-1]},    {stack3[-1]},    {stack4[-1]},    {stack5[-1]},    {stack6[-1]},    {stack7[-1]},    {stack8[-1]},    {stack9[-1]}")
