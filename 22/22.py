with open('input.txt') as f:
    lines = f.readlines()

with open('test_inputs') as f:
    test_input = f.readlines()

y = -1
board = [[" " for j in range(len(lines[0]))] for i in range(len(lines) - 2)]
# board = [[" " for j in range(len(test_input[0]) + 4)] for i in range(len(test_input) - 2)]
passw = []
for line in lines:
    # for line in test_input:
    y += 1
    line = line.replace("\n", "")
    if line == "":
        continue
    if line.startswith("1") or line.startswith("4"):
        temp = ""
        for char in line:
            if char.isnumeric():
                temp += char
            else:
                passw.append(int(temp))
                temp = ""
                passw.append(char)
        passw.append(int(temp))
        continue

    x = 0
    for char in line:
        board[y][x] = char
        x += 1

x = 0
y = 0
orien = 0

while board[y][x] == " ":
    x += 1

for instru in passw:
    if instru == "R":
        orien = (orien + 1) % 4
        continue
    if instru == "L":
        orien = (orien - 1) % 4
        continue

    while instru != 0:
        instru -= 1
        new_x = x
        new_y = y
        if orien == 0:
            new_x += 1
        if orien == 1:
            new_y += 1
        if orien == 2:
            new_x -= 1
        if orien == 3:
            new_y -= 1

        if new_y == len(board) or new_x == len(board[0]) or new_x == -1 or new_y == -1 or board[new_y][new_x] == " ":
            temp_x = x
            temp_y = y
            if orien == 0:
                temp_x = 0
                while board[temp_y][temp_x] == " ":
                    temp_x += 1
                if board[temp_y][temp_x] == "#":
                    break
            if orien == 1:
                temp_y = 0
                while board[temp_y][temp_x] == " ":
                    temp_y += 1
                if board[temp_y][temp_x] == "#":
                    break
            if orien == 2:
                temp_x = len(board[0]) - 1
                while board[temp_y][temp_x] == " ":
                    temp_x -= 1
                if board[temp_y][temp_x] == "#":
                    break
            if orien == 3:
                temp_y = len(board) - 1
                while board[temp_y][temp_x] == " ":
                    temp_y -= 1
                if board[temp_y][temp_x] == "#":
                    break
            x = temp_x
            y = temp_y
            continue
        if board[new_y][new_x] == ".":
            y = new_y
            x = new_x
            continue
        if board[new_y][new_x] == "#":
            break

print(1000 * (y + 1) + (x + 1) * 4 + orien)

print("----- PART 2 -----")
x = 0
y = 0
orien = 0

while board[y][x] == " ":
    x += 1

for instru in passw:
    if instru == "R":
        orien = (orien + 1) % 4
        continue
    if instru == "L":
        orien = (orien - 1) % 4
        continue

    while instru != 0:
        instru -= 1
        new_x = x
        new_y = y
        new_orien = orien
        if orien == 0:
            new_x += 1
        if orien == 1:
            new_y += 1
        if orien == 2:
            new_x -= 1
        if orien == 3:
            new_y -= 1

        if new_y < 0 or new_x < 0 or new_y >= len(board) or new_x >= len(board[0]) or board[new_y][new_x] == " ":
            if y == 0 and 50 <= x <= 99 and orien == 3:
                new_y, new_x, new_orien = x + 100, y, 0
            elif 0 <= y <= 49 and x == 50 and orien == 2:
                new_y, new_x, new_orien = 149 - y, 0, 0
            elif 100 <= y <= 149 and x == 99 and orien == 0:
                new_y, new_x, new_orien = 149 - y, 149, 2
            elif y == 149 and 50 <= x <= 99 and orien == 1:
                new_y, new_x, new_orien = x + 100, 49, 2
            elif y == 0 and 100 <= x <= 149 and orien == 3:
                new_y, new_x, new_orien = 199, x - 100, 3
            elif 0 <= y <= 49 and x == 149 and orien == 0:
                new_y, new_x, new_orien = 149 - y, 99, 2
            elif y == 49 and 100 <= x <= 149 and orien == 1:
                new_y, new_x, new_orien = x - 50, 99, 2
            elif 50 <= y <= 99 and x == 50 and orien == 2:
                new_y, new_x, new_orien = 100, y - 50, 1
            elif 50 <= y <= 99 and x == 99 and orien == 0:
                new_y, new_x, new_orien = 49, y + 50, 3
            elif 150 <= y <= 199 and x == 49 and orien == 0:
                new_y, new_x, new_orien = 149, y - 100, 3
            elif y == 199 and 0 <= x <= 49 and orien == 1:
                new_y, new_x, new_orien = 0, x + 100, 1
            elif 150 <= y <= 199 and x == 0 and orien == 2:
                new_y, new_x, new_orien = 0, y - 100, 1
            elif y == 100 and 0 <= x <= 49 and orien == 3:
                new_y, new_x, new_orien = 50 + x, 50, 0
            elif 100 <= y <= 149 and x == 0 and orien == 2:
                new_y, new_x, new_orien = 149 - y, 50, 0

        if board[new_y][new_x] == "#":
            break

        y = new_y
        x = new_x
        orien = new_orien

print(1000 * (y + 1) + (x + 1) * 4 + orien)
