import sys

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

workflows = {}
parts = []
step = 0
for line in inputt:
    if line == "":
        step += 1
        continue

    if step == 0:
        name = line.split("{")[0]
        to_add = []
        print(line)
        for part in line.split("{")[1].replace("}", "").split(","):
            print(part)
            if len(part) <= 5:
                to_add.append([part])
                continue

            char = ">" if ">" in part else "<"
            part = part.replace(">", "<")
            temp = part.split("<")
            to_add.append([temp[0], char, temp[1].split(":")[0], temp[1].split(":")[1]])
        print(f"Add {name} to {to_add}")
        workflows[name] = to_add
        continue

    temp = line.split("=")
    parts.append({"x": temp[1].split(",")[0], "m": temp[2].split(",")[0], "a": temp[3].split(",")[0],
                  "s": temp[4].split(",")[0].replace("}", "")})

print(workflows)
print(parts)

accepted = []
for part in parts:
    end = False
    curr = "in"
    index = 0
    print(f"Part {part}: ", end="")
    while not end:
        if curr == "A":
            end = True
            accepted.append(part)
            break
        if curr == "R":
            end = True
            break

        print(f" -> {curr}", end="")
        index = 0
        while not end:
            workflow = workflows[curr][index]
            print(f" {index}", end="")
            if len(workflow) == 1:
                if workflow[0] == "A":
                    accepted.append(part)
                    end = True
                elif workflow[0] == "R":
                    end = True
                else:
                    curr = workflow[0]
                break
            if eval(f"{part[workflow[0]]} {workflow[1]} {workflow[2]}"):
                curr = workflow[3]
                break
            index += 1
    print()

print(accepted)
result = 0

for part in accepted:
    result += int(part["x"]) + int(part["m"]) + int(part["a"]) + int(part["s"])

print(result)

print("----- PART 2 -----")


def evaluate_range(curr, index, start_x, end_x, start_m, end_m, start_a, end_a, start_s, end_s, result):
    if curr in "AR":
        if curr == "A":
            result[0] += (end_x - start_x + 1) * (end_m - start_m + 1) * (end_a - start_a + 1) * (end_s - start_s + 1)
        return

    workflow = workflows[curr][index]
    if len(workflow) == 1:
        if workflow[0] == "A":
            result[0] += (end_x - start_x + 1) * (end_m - start_m + 1) * (end_a - start_a + 1) * (end_s - start_s + 1)
        elif workflow[0] == "R":
            return
        else:
            evaluate_range(workflow[0], 0, start_x, end_x, start_m, end_m, start_a, end_a, start_s, end_s, result)
        return

    print(f"go for {curr, index, workflow, start_x, end_x, start_m, end_m, start_a, end_a, start_s, end_s, result}")
    start = {"s": start_s, "x": start_x, "m": start_m, "a": start_a}[workflow[0]]
    end = {"s": end_s, "x": end_x, "m": end_m, "a": end_a}[workflow[0]]
    if workflow[1] == "<":
        if end < int(workflow[2]):
            evaluate_range(workflow[3], 0, start_x, end_x, start_m, end_m, start_a, end_a, start_s, end_s, result)
        elif start > int(workflow[2]):
            evaluate_range(curr, index + 1, start_x, end_x, start_m, end_m, start_a, end_a, start_s, end_s, result)
        else:
            if workflow[0] == "s":
                evaluate_range(workflow[3], 0, start_x, end_x, start_m, end_m, start_a, end_a, start, int(workflow[2]) - 1, result)
                evaluate_range(curr, index + 1, start_x, end_x, start_m, end_m, start_a, end_a, int(workflow[2]), end, result)
            elif workflow[0] == "x":
                evaluate_range(workflow[3], 0, start, int(workflow[2]) - 1, start_m, end_m, start_a, end_a, start_s, end_s, result)
                evaluate_range(curr, index + 1, int(workflow[2]), end, start_m, end_m, start_a, end_a, start_s, end_s, result)
            elif workflow[0] == "m":
                evaluate_range(workflow[3], 0, start_x, end_x, start, int(workflow[2]) - 1, start_a, end_a, start_s, end_s, result)
                evaluate_range(curr, index + 1, start_x, end_x, int(workflow[2]), end, start_a, end_a, start_s, end_s, result)
            elif workflow[0] == "a":
                evaluate_range(workflow[3], 0, start_x, end_x, start_m, end_m, start, int(workflow[2]) - 1, start_s, end_s, result)
                evaluate_range(curr, index + 1, start_x, end_x, start_m, end_m, int(workflow[2]), end, start_s, end_s, result)
    else:
        if start > int(workflow[2]):
            evaluate_range(workflow[3], 0, start_x, end_x, start_m, end_m, start_a, end_a, start_s, end_s, result)
        elif end < int(workflow[2]):
            evaluate_range(curr, index + 1, start_x, end_x, start_m, end_m, start_a, end_a, start_s, end_s, result)
        else:
            if workflow[0] == "s":
                evaluate_range(curr, index + 1, start_x, end_x, start_m, end_m, start_a, end_a, start, int(workflow[2]), result)
                evaluate_range(workflow[3], 0, start_x, end_x, start_m, end_m, start_a, end_a, int(workflow[2]) + 1, end, result)
            elif workflow[0] == "x":
                print(f"goto {curr} {index +1} or {workflow[3]} 0")
                evaluate_range(curr, index + 1, start, int(workflow[2]), start_m, end_m, start_a, end_a, start_s, end_s, result)
                evaluate_range(workflow[3], 0, int(workflow[2]) + 1, end, start_m, end_m, start_a, end_a, start_s, end_s, result)
            elif workflow[0] == "m":
                evaluate_range(curr, index + 1, start_x, end_x, start, int(workflow[2]), start_a, end_a, start_s, end_s, result)
                evaluate_range(workflow[3], 0, start_x, end_x, int(workflow[2]) + 1, end, start_a, end_a, start_s, end_s, result)
            elif workflow[0] == "a":
                evaluate_range(curr, index +1, start_x, end_x, start_m, end_m, start, int(workflow[2]), start_s, end_s, result)
                evaluate_range(workflow[3], 0, start_x, end_x, start_m, end_m, int(workflow[2]) + 1, end, start_s, end_s, result)


result = [0]
evaluate_range("in", 0, 1, 4000, 1, 4000, 1, 4000, 1, 4000, result)
print(result)
