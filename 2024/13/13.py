import sys
import z3

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

parsed = []
step = 0
for line in inputt:
    sp = line.replace(",", "").split(" ")
    if step == 0:
        parsed.append([(int(sp[2].split("+")[1]), int(sp[3].split("+")[1]))])
        step += 1
        continue
    if step == 1:
        parsed[-1].append((int(sp[2].split("+")[1]), int(sp[3].split("+")[1])))
        step += 1
        continue
    if step == 2:
        parsed[-1].append((int(sp[1].split("=")[1]), int(sp[2].split("=")[1])))
        step += 1
        continue
    step = 0

print(parsed)
result = 0
for par in parsed:
    solver = z3.Optimize()
    a = z3.Int("a")
    b = z3.Int("b")
    solver.add(a * par[0][0] + b * par[1][0] == par[2][0])
    solver.add(a * par[0][1] + b * par[1][1] == par[2][1])
    solver.minimize(3 * a + b)
    if solver.check() == z3.sat:
        result += 3 * solver.model().eval(a).as_long() + solver.model().eval(b).as_long()

print(result)

print("----- PART 2 -----")

result = 0
for par in parsed:
    solver = z3.Optimize()
    a = z3.Int("a")
    b = z3.Int("b")
    solver.add(a * par[0][0] + b * par[1][0] == par[2][0] + 10000000000000)
    solver.add(a * par[0][1] + b * par[1][1] == par[2][1] + 10000000000000)
    solver.minimize(3 * a + b)
    if solver.check() == z3.sat:
        result += 3 * solver.model().eval(a).as_long() + solver.model().eval(b).as_long()

print(result)
