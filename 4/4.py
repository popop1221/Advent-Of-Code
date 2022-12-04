with open('input.txt') as f:
    lines = f.readlines()

test_input = [
"2-4,6-8",
"2-3,4-5",
"5-7,7-9",
"2-8,3-7",
"6-6,4-6",
"2-6,4-8"
]

result = 0
for line in lines:
    line.replace("\n", "")
    elf = line.split(",")
    list1 = elf[0].split("-")
    list2 = elf[1].split("-")
    list1 = [i for i in range(int(list1[0]), int(list1[1])+1)]
    list2 = [i for i in range(int(list2[0]), int(list2[1])+1)]

    if all(elem in list1 for elem in list2):
        result += 1
        continue
    if all(elem in list2 for elem in list1):
        result += 1

print(result)

print("----- PART 2 -----")
result = 0
for line in lines:
    line.replace("\n", "")
    elf = line.split(",")
    list1 = elf[0].split("-")
    list2 = elf[1].split("-")
    list1 = [i for i in range(int(list1[0]), int(list1[1])+1)]
    list2 = [i for i in range(int(list2[0]), int(list2[1])+1)]

    temp = result
    for elem in list1:
        if elem in list2:
            result += 1
            break
    if temp != result:
        continue

    for elem in list2:
        if elem in list1:
            result += 1
            break

print(result)