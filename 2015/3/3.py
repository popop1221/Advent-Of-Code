with open('input.txt') as f:
    real_input = f.readlines()

inputt = real_input[0].replace("\n", "")
dico = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}

pos = (0, 0)
result = set()
result.add(pos)
for char in inputt:
    t = dico[char]
    pos = (pos[0] + t[0], pos[1] + t[1])
    result.add(pos)

print(len(result))

print("----- PART 2 -----")

pos = (0, 0)
pos2 = (0, 0)
i = 0
result = set()
result.add(pos)
for char in inputt:
    i += 1
    t = dico[char]
    if i % 2 == 0:
        pos = (pos[0] + t[0], pos[1] + t[1])
    else:
        pos2 = (pos2[0] + t[0], pos2[1] + t[1])

    result.add(pos)
    result.add(pos2)

print(len(result))
