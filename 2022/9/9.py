with open('input.txt') as f:
    lines = f.readlines()

test_inputs = ["R 4",
               "U 4",
               "L 3",
               "D 1",
               "R 4",
               "D 1",
               "L 5",
               "R 2"]

visited = [[0 for i in range(1000)] for j in range(1000)]
head_pos = (0, 0)
tail_pos = (0, 0)
visited[0][0] = 1

for line in lines:
    # for line in test_inputs:
    line.replace("\n", "")
    inputs = line.split(" ")

    for i in range(int(inputs[1])):
        last_head_pos = head_pos
        if inputs[0] == "R":
            head_pos = (head_pos[0] + 1, head_pos[1])

        if inputs[0] == "L":
            head_pos = (head_pos[0] - 1, head_pos[1])

        if inputs[0] == "U":
            head_pos = (head_pos[0], head_pos[1] + 1)

        if inputs[0] == "D":
            head_pos = (head_pos[0], head_pos[1] - 1)

        possible_pos = [(head_pos[0] - 1, head_pos[1]),
                        (head_pos[0], head_pos[1] - 1),
                        (head_pos[0] - 1, head_pos[1] - 1),
                        (head_pos[0], head_pos[1] + 1),
                        (head_pos[0] + 1, head_pos[1]),
                        (head_pos[0] + 1, head_pos[1] + 1),
                        (head_pos[0] - 1, head_pos[1] + 1),
                        (head_pos[0] + 1, head_pos[1] - 1), head_pos]
        if tail_pos in possible_pos:
            continue
        tail_pos = last_head_pos
        visited[tail_pos[0]][tail_pos[1]] = 1
    last_h_move = inputs[0]

result = 0
for liste in visited:
    result += liste.count(1)
print(result)

print("----- PART 2 -----")
test_inputs = ["R 4",
               "U 4",
               "L 3",
               "D 1",
               "R 4",
               "D 1",
               "L 5",
               "R 2"]
test_inputs1 = ["R 5",
                "U 8",
                "L 8",
                "D 3",
                "R 17",
                "D 10",
                "L 25",
                "U 20"]

visited = [[0 for i in range(2000)] for j in range(2000)]
visited[0][0] = 1

tail = [(0, 0) for i in range(10)]
for line in lines:
    # for line in test_inputs:
    line.replace("\n", "")
    inputs = line.split(" ")

    for i in range(int(inputs[1])):
        if inputs[0] == "R":
            tail[0] = (tail[0][0] + 1, tail[0][1])

        if inputs[0] == "L":
            tail[0] = (tail[0][0] - 1, tail[0][1])

        if inputs[0] == "U":
            tail[0] = (tail[0][0], tail[0][1] + 1)

        if inputs[0] == "D":
            tail[0] = (tail[0][0], tail[0][1] - 1)

        for j in range(1, len(tail)):
            head_pos = tail[j - 1]
            possible_pos = [(head_pos[0] - 1, head_pos[1]),
                            (head_pos[0], head_pos[1] - 1),
                            (head_pos[0] - 1, head_pos[1] - 1),
                            (head_pos[0], head_pos[1] + 1),
                            (head_pos[0] + 1, head_pos[1]),
                            (head_pos[0] + 1, head_pos[1] + 1),
                            (head_pos[0] - 1, head_pos[1] + 1),
                            (head_pos[0] + 1, head_pos[1] - 1), head_pos]
            if tail[j] in possible_pos:
                continue

            if (tail[j][0] + 2) == head_pos[0] and head_pos[1] == tail[j][1]:
                tail[j] = (tail[j][0] + 1, tail[j][1])
                continue

            if tail[j][0] - 2 == head_pos[0] and head_pos[1] == tail[j][1]:
                tail[j] = (tail[j][0] - 1, tail[j][1])
                continue

            if tail[j][1] + 2 == head_pos[1] and head_pos[0] == tail[j][0]:
                tail[j] = (tail[j][0], tail[j][1] + 1)
                continue

            if tail[j][1] - 2 == head_pos[1] and head_pos[0] == tail[j][0]:
                tail[j] = (tail[j][0], tail[j][1] - 1)
                continue

            if tail[j][1] < head_pos[1] and tail[j][0] < head_pos[0]:
                tail[j] = (tail[j][0] + 1, tail[j][1] + 1)
                continue
            if tail[j][1] > head_pos[1] and tail[j][0] > head_pos[0]:
                tail[j] = (tail[j][0] - 1, tail[j][1] - 1)
                continue

            if tail[j][1] < head_pos[1] and tail[j][0] > head_pos[0]:
                tail[j] = (tail[j][0] - 1, tail[j][1] + 1)
                continue

            if tail[j][1] > head_pos[1] and tail[j][0] < head_pos[0]:
                tail[j] = (tail[j][0] + 1, tail[j][1] - 1)
                continue
        visited[tail[9][0]][tail[9][1]] = 1

result = 0
for liste in visited:
    result += liste.count(1)
print(result)
