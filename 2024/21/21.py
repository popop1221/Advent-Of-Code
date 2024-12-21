import sys

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

numeric_pad = ["789",
               "456",
               "123",
               " 0A"]
numeric_move = {"780A": "^^^<<A>AvvvA>A",
                "539A": "<^^Av>A^^AvvvA",
                "341A": "^A<<^AvA>>vA",
                "189A": "^<<A^^>A>AvvvA",
                "682A": "^^A<^AvvAv>A"}
dir_pad = [" ^A", "<v>"]
result = 0
for line in inputt:
    print(f"{line} -> ", end="")
    temp = numeric_move[line]
    print(f"{temp} -> ", end="")

    temp2 = ""
    pos = (0, 2)
    for char in temp:
        while dir_pad[pos[0]][pos[1]] != char:
            if char in dir_pad[pos[0]]:
                if dir_pad[pos[0]].index(char) > pos[1]:
                    pos = (pos[0], pos[1] + 1)
                    temp2 += ">"
                else:
                    pos = (pos[0], pos[1] - 1)
                    temp2 += "<"
            elif pos[0] == 0:
                pos = (1, pos[1])
                temp2 += "v"
            else:
                pos = (0, pos[1])
                temp2 += "^"
        temp2 += "A"
    print(f"{temp2} -> ", end="")

    temp3 = ""
    pos = (0, 2)
    for char in temp2:
        while dir_pad[pos[0]][pos[1]] != char:
            if char in dir_pad[pos[0]]:
                if dir_pad[pos[0]].index(char) > pos[1]:
                    pos = (pos[0], pos[1] + 1)
                    temp3 += ">"
                else:
                    pos = (pos[0], pos[1] - 1)
                    temp3 += "<"
            elif pos[0] == 0:
                pos = (1, pos[1])
                temp3 += "^"
            else:
                pos = (0, pos[1])
                temp3 += "v"
        temp3 += "A"
    print(temp3)
    result += len(temp3) * int(line[:-1])
    print(f"{len(temp3)} * {int(line[:-1])}")
print(result)

print("----- PART 2 -----")

# " ^A",
# "<v>"
dir_move = {('^', 'A'): ">A", ('^', '<'): "v<A", ('^', 'v'): "vA",
            ('^', '>'): "v>A", ('A', '<'): "v<<A", ('A', 'v'): "<vA",
            ('A', '>'): "vA", ('A', '^'): "<A", ('<', '^'): ">^A",
            ('<', 'A'): ">>^A", ('<', 'v'): ">A", ('<', '>'): ">>A",
            ('v', '^'): "^A", ('v', 'A'): "^>A", ('v', '<'): "<A",
            ('v', '>'): ">A", ('>', '<'): "<<A", ('>', 'v'): "<A",
            ('>', 'A'): "^A", ('>', '^'): "<^A", ('A', 'A'): "A",
            ('<', '<'): "A", ('>', '>'): "A", ('v', 'v'): "A", ('^', '^'): "A"}
result = 0
for line in inputt:
    print(line)
    temp = numeric_move[line]
    print(temp)

    temp2 = {('^', 'A'): 0, ('^', '<'): 0, ('^', 'v'): 0,
             ('^', '>'): 0, ('A', '<'): 0, ('A', 'v'): 0,
             ('A', '>'): 0, ('A', '^'): 0, ('<', '^'): 0,
             ('<', 'A'): 0, ('<', 'v'): 0, ('<', '>'): 0,
             ('v', '^'): 0, ('v', 'A'): 0, ('v', '<'): 0,
             ('v', '>'): 0, ('>', '<'): 0, ('>', 'v'): 0,
             ('>', 'A'): 0, ('>', '^'): 0, ('A', 'A'): 0,
             ('<', '<'): 0, ('>', '>'): 0, ('v', 'v'): 0, ('^', '^'): 0}
    old = "A"
    for char in temp:
        temp2[(old, char)] += 1
        old = char

    for i in range(24):
        temp3 = {('^', 'A'): 0, ('^', '<'): 0, ('^', 'v'): 0,
                 ('^', '>'): 0, ('A', '<'): 0, ('A', 'v'): 0,
                 ('A', '>'): 0, ('A', '^'): 0, ('<', '^'): 0,
                 ('<', 'A'): 0, ('<', 'v'): 0, ('<', '>'): 0,
                 ('v', '^'): 0, ('v', 'A'): 0, ('v', '<'): 0,
                 ('v', '>'): 0, ('>', '<'): 0, ('>', 'v'): 0,
                 ('>', 'A'): 0, ('>', '^'): 0, ('A', 'A'): 0,
                 ('<', '<'): 0, ('>', '>'): 0, ('v', 'v'): 0, ('^', '^'): 0}
        print(i)
        print(temp2)
        pos = (0, 2)
        old = "A"
        for jsp in temp2.keys():
            for char in dir_move[jsp]:
                temp3[(old, char)] += temp2[jsp]
                old = char
        temp2 = temp3
    print(temp2)
    temp4 = sum([len(dir_move[temp5]) * temp2[temp5] for temp5 in temp2.keys()])
    result += temp4 * int(line[:-1])
    print(f"{temp4} * {int(line[:-1])}")
print(result)
