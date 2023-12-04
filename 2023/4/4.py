with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input

result = 0
card = 0
for line in inputt:
    card += 1
    line = line.replace("\n", "")
    temp = line.split("|")
    first = []
    second = []
    for elem in temp[0].split(" ")[2:]:
        if not elem.isnumeric():
            continue
        first.append(int(elem))
    for elem in temp[1].split(" "):
        if not elem.isnumeric():
            continue
        second.append(int(elem))

    temp2 = 0
    for second_elem in second:
        if second_elem in first:
            if temp2 == 0:
                temp2 = 1
            else:
                temp2 *= 2
    result += temp2

print(result)

print("----- PART 2 -----")
values = []
i_have = []
card = 0
for line in inputt:
    card += 1
    line = line.replace("\n", "")
    temp = line.split("|")
    first = []
    second = []
    for elem in temp[0].split(" ")[2:]:
        if not elem.isnumeric():
            continue
        first.append(int(elem))
    for elem in temp[1].split(" "):
        if not elem.isnumeric():
            continue
        second.append(int(elem))

    temp2 = 0
    number = 0
    for second_elem in second:
        if second_elem in first:
            number += 1
            if temp2 == 0:
                temp2 = 1
            else:
                temp2 *= 2
    values.append(temp2)
    for i in range(1, number + 1):
        for j in range(i_have.count(card) + 1):
            i_have.append(card + i)
    i_have.append(card)
    print(f"End of card {card} {len(i_have)}")

print(len(i_have))
