with open('input.txt') as f:
    lines = f.readlines()

shape_score = {"Y": 2, "X": 1, "Z": 3}
map_win = {"A": "Y", "B": "Z", "C": "X"}
mat_win = {"A": "X", "B": "Y", "C": "Z"}

result = 0
for line in lines:
    temp = line.replace("\n", "").split(" ")
    result += shape_score[temp[1]]

    if temp[1] == mat_win[temp[0]]:
        result += 3
        continue

    if temp[1] == map_win[temp[0]]:
        result += 6
        continue
    result += 0

print(result)

print("PART 2")

loss_map = {"A" : "Z", "B" : "X", "C": "Y"}

result = 0
for line in lines:
    temp = line.replace("\n", "").split(" ")

    print(temp)
    print(result)
    if temp[1] == "X":
        result += shape_score[loss_map[temp[0]]]
        continue

    if temp[1] == "Y":
        result += 3
        result += shape_score[mat_win[temp[0]]]
        continue

    if temp[1] == "Z":
        result += shape_score[map_win[temp[0]]]
        result += 6

print(result)