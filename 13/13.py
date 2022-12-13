import functools

with open('input.txt') as f:
    lines = f.readlines()

with open('test_inputs') as f:
    test_input = f.readlines()


def compare_rec(left, right):
    if type(left) is int and type(right) is int:
        if left == right:
            return None
        return left < right
    if type(left) is list and type(right) is list:
        for i in range(len(left)):
            if i >= len(right):
                return False
            bool = compare_rec(left[i], right[i])
            if bool is None:
                continue
            return bool
        return None if len(left) == len(right) else (len(left) < len(right))

    if type(left) is int:
        return compare_rec([left], right)

    if type(right) is int:
        return compare_rec(left, [right])


inputs = []
temp1 = []
temp2 = []
i = 0

for line in lines:
#for line in test_input:
    line = line.replace("\n", "")
    i += 1
    if i == 1:
        temp1 = eval(line)
    if i == 2:
        temp2 = eval(line)
    if i == 3:
        inputs.append((temp1, temp2))
        i = 0

i = 1
result = 0
for todo in inputs:
    if compare_rec(todo[0], todo[1]):
        result += i
    i += 1

print(result)

print("----- PART 2 -----")


def compare_sort(left, right):
    temp = compare_rec(left, right)
    return 0 if temp is None else (-1 if temp else 1)


inputs = [[[2]], [[6]]]
for line in lines:
    if line != "\n":
        inputs.append(eval(line))
inputs_sorted = sorted(inputs, key=functools.cmp_to_key(compare_sort))
print((1 + inputs_sorted.index([[2]])) * (1 + inputs_sorted.index([[6]])))
