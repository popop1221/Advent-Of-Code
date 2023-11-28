with open('input.txt') as f:
    lines = f.readlines()

with open('test_inputs') as f:
    test_input = f.readlines()

numbers = []
for line in lines:
#for line in test_input:
    line = line.replace("\n", "")
    numbers.append(int(line))

numbers_index = [i for i in range(len(numbers))]

for i in range(len(numbers)):
    index = numbers_index.index(i)
    numbers_index.pop(index)
    value = numbers.pop(index)
    new_index = (index + value) % (len(numbers))

    numbers.insert(new_index, value)
    numbers_index.insert(new_index, i)

zero_index = numbers.index(0)
print(numbers[zero_index+1000] + numbers[zero_index+2000] + numbers[zero_index+3000])

print("----- PART 2 -----")
numbers = []
for line in lines:
#for line in test_input:
    line = line.replace("\n", "")
    numbers.append(int(line) * 811589153)

numbers_index = [i for i in range(len(numbers))]

for j in range(10):
    for i in range(len(numbers)):
        index = numbers_index.index(i)
        numbers_index.pop(index)
        value = numbers.pop(index)
        new_index = (index + value) % (len(numbers))

        numbers.insert(new_index, value)
        numbers_index.insert(new_index, i)

zero_index = numbers.index(0)
print(numbers[zero_index+1000] + numbers[zero_index+2000] + numbers[zero_index+3000])
