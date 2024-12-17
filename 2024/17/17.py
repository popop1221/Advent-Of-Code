import sys

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

A = 0
B = 0
C = 0
parsed = []

step = 0
for line in inputt:
    if step == 0:
        A = int(line.split(" ")[2])
        step += 1
    elif step == 1:
        B = int(line.split(" ")[2])
        step += 1
    elif step == 2:
        C = int(line.split(" ")[2])
        step += 1
    else:
        ls = line.split(",")
        for i in range(0, len(ls), 1):
            parsed.append((int(ls[i])))  # , int(ls[i + 1])))

print(f"A: {A}")
print(f"B: {B}")
print(f"C : {C}")
print(parsed)


"""def get_combo_operand(combo_operand):
    if 0 <= combo_operand <= 3:
        return combo_operand
    if 4 <= combo_operand <= 6:
        return [A, B, C][combo_operand - 4]
    exit(42)


i = 0
result = ""
while i < len(parsed):
    print(f"--------\nPC : {i}")
    print(f"A: {A}")
    print(f"B: {B}")
    print(f"C : {C}")
    if parsed[i] == 0:
        A = int(A / (2 ** get_combo_operand(parsed[i + 1])))
        i += 2
    elif parsed[i] == 1:
        B = B ^ parsed[i + 1]
        i += 2
    elif parsed[i] == 2:
        B = get_combo_operand(parsed[i + 1]) % 8
        i += 2
    elif parsed[i] == 3:
        if A == 0:
            i += 2
            continue
        i = parsed[i + 1]
    elif parsed[i] == 4:
        B = B ^ C
        i += 2
    elif parsed[i] == 5:
        result += f"{get_combo_operand(parsed[i + 1]) % 8},"
        i += 2
    elif parsed[i] == 6:
        B = int(A / (2 ** get_combo_operand(parsed[i + 1])))
        i += 2
    elif parsed[i] == 7:
        C = int(A / (2 ** get_combo_operand(parsed[i + 1])))
        i += 2

print(f"--------\nPC : {i}")
print(f"A: {A}")
print(f"B: {B}")
print(f"C : {C}")
print(f"Result : {result}")
"""
print("----- PART 2 -----") # By hand

def evaluate(A):

    B = 0
    C = 0
    i = 0

    def get_combo_operand(combo_operand):
        if 0 <= combo_operand <= 3:
            return combo_operand
        if 4 <= combo_operand <= 6:
            return [A, B, C][combo_operand - 4]
        exit(42)

    result = ""
    while i < len(parsed):
        if parsed[i] == 0:
            A = int(A / (2 ** get_combo_operand(parsed[i + 1])))
            i += 2
        elif parsed[i] == 1:
            B = B ^ parsed[i + 1]
            i += 2
        elif parsed[i] == 2:
            B = get_combo_operand(parsed[i + 1]) % 8
            i += 2
        elif parsed[i] == 3:
            if A == 0:
                i += 2
                continue
            i = parsed[i + 1]
        elif parsed[i] == 4:
            B = B ^ C
            i += 2
        elif parsed[i] == 5:
            result += f"{get_combo_operand(parsed[i + 1]) % 8},"
            i += 2
        elif parsed[i] == 6:
            B = int(A / (2 ** get_combo_operand(parsed[i + 1])))
            i += 2
        elif parsed[i] == 7:
            C = int(A / (2 ** get_combo_operand(parsed[i + 1])))
            i += 2
    return result

# todo : 2,4,1,5,7,5,4,3,1,6,0,3,5,5,3,0
# 16

# A = 1 -> 2,
# 128 -> 7,3,1
# 512 -> 3,1,3,2
# 2 097 152 -> 3,3,3,3,3,1,3,2, --> 8
# 1099511627776 -> 3,3,3,3,3,3,3,3,3,3,3,7,3,1, --> 14
# 4398046511104 -> 3,3,3,3,3,3,3,3,3,3,3,3,1,3,2, --> 15
# 8796093022208 -> 3,3,3,3,3,3,3,3,3,3,3,3,7,3,1, --> 15
# 17592186044416 ->3,3,3,3,3,3,3,3,3,3,3,3,3,2,5, --> 15
# 35184372088832 ->3,3,3,3,3,3,3,3,3,3,3,3,3,1,3,2, --> 16 2**44
# 70368744177664 ->3,3,3,3,3,3,3,3,3,3,3,3,3,7,3,1,
#140737488355328 ->3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,5, --> 2**48
# ^ - 1            3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,5,

# 281474976710654 -> 2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,5,

# todo : 2,4,1,5,7,5,4,3,1,6,0,3,5,5,3,0

# 281474976710654
# 111 111 111 111 111 111 111 111 111 111 111 111 111 111 111 110

# 111 111 111 111 111 111 111 111 111 111 111 111 111 111 111 110 =

# 111 110 101 100 001 000 010 011 = 16433683 --> 0,1,3,4,1,3,2,5,

# 111  5
# 110  2
# 101   3
# 100    1
# 001   4
# 000   3
# 010   1
# 011 ->0

# 011 101 111 111 000 011 011 010 101 001 111 111 111 010 001 110 = 131876344299150
# 4, 7, 6, 3, 3, 7, 0, 3, 0, 0, 7, 4, 3, 7, 3, 0,

"""
B = A % 8 # 2, 4
B = B ^ 5 # 1, 5
C = A / 2**B  #7, 5
B = B ^ C # 4, 3
B = B ^ 6 # 1, 6
A = A / 2**3 # 0, 3
print(B%8) #5, 5
if (A != 0) goto 0 #3, 0
"""

# todo : 2,4,1,5,7,5,4,3,1,6,0,3,5,5,3,0

# result = 011 101 ***

print(f"Part 1: {evaluate(61156655)}")
print(f"Evaluate : {evaluate(0b011101)}")
print(f"Eval to high ? : {evaluate(110132820806042)}") # 011001000010101001001011101010011000100110011010

# 011 000 000 010 101 001 001 011 101 010 011 000 100 110 011
# 011 000 000 010 101 001 001 011 101 010 011 000 110
# 011 000 000 010 101 001 001 011 101 010 011 000 111
# 011 000 000 010 101 001 001 011 101 010 100
# 011 000 000 010 101 001 001 011 111
# 011 000 000 010 101 001 001 100
# 011 000 000 010 101 010
# 011 000 000 010 101 110
# 011 000 000 100
# 011 000 000 110
# 011 000 000 111
# 011 000 100
# 011 000 110
# 011 000 111
# 011 001
# 011 101
# 011 111

result = "011000000010101001001011101010011000100110011"
for i in range(8): # To find the next value
    print("---")
    temp = str(bin(i)).replace("0b", "")
    while len(temp) != 3:
        temp = "0" + temp
    print(str(bin(i)).replace("0b", "") + " --> " + temp)
    print(result + temp + " = " + str(int(result + temp, 2)))
    print(evaluate(int(result + temp, 2)) + " --> " + evaluate(int(result + temp, 2)))
