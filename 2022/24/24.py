with open('input.txt') as f:
    lines = f.readlines()

with open('test_inputs') as f:
    test_input = f.readlines()

max_y = len(lines) - 1
#max_y = len(test_input) - 1
max_x = len(lines[0]) - 2
#max_x = len(test_input[0]) - 2

start = (1,0)
end = (max_x - 1, max_y)
walls = set()

states = {}

init_pos = set()
init_bliz = {}
y = -1
for line in lines:
#for line in test_input:
    y += 1
    line = line.replace("\n", "")
    x = -1
    for char in line:
        x += 1
        if char == "#":
            walls.add((x,y))
        elif char != ".":
            init_pos.add((x,y))
            if (x,y) in init_bliz.keys():
                init_bliz[(x,y)].append(char)
            else:
                init_bliz[(x,y)] = [char]

states[0] = (init_pos, init_bliz)
print(states)

def next_state(state):
    curr_pos, curr_bliz = states[state]
    new_pos, new_bliz = set(), {}

    for pos in curr_bliz.keys():
        for move in curr_bliz[pos]:
            if move == "<":
                if pos[0] - 1 == 0:
                    temp = (max_x - 1, pos[1])
                else:
                    temp = (pos[0] - 1, pos[1])
            elif move == ">":
                if pos[0] + 1 == max_x:
                    temp = (1, pos[1])
                else:
                    temp = (pos[0] + 1, pos[1])
            elif move == "v":
                if pos[1] + 1 == max_y:
                    temp = (pos[0], 1)
                else:
                    temp = (pos[0], pos[1] + 1)
            else:
                if pos[1] - 1 == 0:
                    temp = (pos[0], max_y - 1)
                else:
                    temp = (pos[0], pos[1] - 1)

            new_pos.add(temp)
            if temp in new_bliz.keys():
                new_bliz[temp].append(move)
            else:
                new_bliz[temp] = [move]
    states[state + 1] = (new_pos, new_bliz)


for i in range(0, 1001):
    next_state(i)

min_turn = 600
memo = set()


def simulate(x, y, turn, acc):
    global min_turn

    if (x, y) == end:
        print(f"End in {turn}    {acc}")
        min_turn = min(min_turn, turn)

    if (x, y, turn) in memo:
        return

    memo.add((x, y, turn))

    if turn >= min_turn:
        return

    curr_pos, curr_bliz = states[turn]

    i = -1
    for next in [(x + pos[0], y + pos[1]) for pos in [(1, 0), (0, 1), (-1, 0), (0, -1)]]:
        i += 1
        if next in walls or next in curr_pos or next[0] < 0 or next[1] < 0 or next[0] > max_x or next[1] > max_y:
            continue
        simulate(next[0], next[1], turn + 1, acc.copy() + [["Right"], ["Down"], ["Left"], ["Up"]][i] + [(x, y)])

    if (x, y) not in curr_pos:
        simulate(x, y, turn + 1, acc.copy() + ["Wait"] + [(x, y)])

simulate(start[0], start[1], 1, [])
print(min_turn - 1)
part1 = min_turn - 1

print("----- PART 2 -----")
min_turn = [300, 601, 1001]
memo = set()


def simulate2(x, y, turn, acc, end1, j):
    global min_turn
    if (x, y) == end1:
        print(f"End {j} in {turn}    {acc}")
        min_turn[j] = min(min_turn[j], turn)

    if (x, y, turn, end1, j) in memo:
        return

    memo.add((x, y, turn, end1, j))

    if turn >= min_turn[j]:
        return

    curr_pos, curr_bliz = states[turn]

    i = -1
    for next in [(x + pos[0], y + pos[1]) for pos in [(1, 0), (0, 1), (-1, 0), (0, -1)]]:
        i += 1
        if next in walls or next in curr_pos or next[0] < 0 or next[1] < 0 or next[0] > max_x or next[1] > max_y:
            continue
        simulate2(next[0], next[1], turn + 1, acc.copy() + [["Right"], ["Down"], ["Left"], ["Up"]][i] + [(x, y)], end1, j)

    if (x, y) not in curr_pos:
        simulate2(x, y, turn + 1, acc.copy() + ["Wait"] + [(x, y)], end1, j)


simulate2(start[0], start[1], 1, [], end, 0)
simulate2(end[0], end[1], min_turn[0], [], start, 1)
simulate2(start[0], start[1], min_turn[1], [], end, 2)
print(min_turn[2] - 1)

