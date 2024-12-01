import sys

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
data = []

for line in inputt:
    line = line.replace("\n", "")
    line_splited = line.split(":")[1].split(",")
    temp = []
    for val in line_splited:
        temp.append(int(val.split(" ")[2]))
    data.append(temp)
print(data)

# 2 val
result = 0
result2 = 0
for i in range(1, 101):
    for j in range(1, 101 - i):
        temp = []
        for k in range(len(data[0]) - 1):
            temp.append(max(0, data[0][k] * i + data[1][k] * j))
        val = temp[0] * temp[1] * temp[2] * temp[3]
        if val > result:
            print(f"new result for {i}  {j} : {val}")
            print(temp)
            result = val
            calories = data[0][-1] * i + data[1][-1] * j
            if calories == 500:
                print(f"New result2 : {val}")
                result2 = val
print(result2)
# 4 val
result = 0
result2 = 0
for i in range(1, 101):
    for j in range(1, 101 - i):
        for ii in range(1, 101 - (i + j)):
            for jj in range(1, 101 - (i + j + ii)):
                if i + j + ii + jj != 100:
                    continue

                temp = []
                for k in range(len(data[0]) - 1):
                    temp.append(max(0, data[0][k] * i + data[1][k] * j + data[2][k] * ii + data[3][k] * jj))
                val = temp[0] * temp[1] * temp[2] * temp[3]
                if val > result:
                    print(f"new result for {i} {j} {ii} {jj} : {val}")
                    print(temp)
                    result = val

                calories = data[0][-1] * i + data[1][-1] * j + data[2][-1] * ii + data[3][-1] * jj
                if val > result2 and calories == 500:
                    print(f"New result2 for {i} {j} {ii} {jj} : {val}")
                    result2 = val

print("----- PART 2 -----")

print(result2)
