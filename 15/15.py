with open('input.txt') as f:
    lines = f.readlines()

with open('test_inputs') as f:
    test_input = f.readlines()

sensor = []
beacons = set()
x = []
for line in lines:
#for line in test_input:
    line = line.replace("\n", "")
    temp = line.split(" ")
    dic = {"coord": (int(temp[2].split('=')[1].split(",")[0]), int(temp[3].split('=')[1].split(":")[0]))}
    bec = (int(temp[8].split('=')[1].split(",")[0]), int(temp[9].split('=')[1].split(",")[0]))
    dist_x = abs(dic["coord"][0] - bec[0])
    dist_y = abs(dic["coord"][1] - bec[1])
    dic["dist"] = (dist_x + dist_y)
    x.append(int(temp[2].split('=')[1].split(",")[0]))
    x.append(int(temp[8].split('=')[1].split(",")[0]))
    beacons.add(bec)
    sensor.append(dic)

x_max = max(x)
x_min = min(x)
y = 2000000
result = 0
for i in range(-10000000,10000000):
    if (i, y) in beacons:
        continue
    for sens in sensor:
        manh = abs((sens["coord"][0] - i)) + abs((sens["coord"][1] - y))
        if sens["dist"] >= manh:
            result += 1
            break

print(result)

print("----- PART 2 -----")


def is_valid_pos(x, y):
    if (x, y) in beacons:
        return False
    if x < 0 or y < 0 or x > 4000000 or y > 4000000:
        return False
    for sens in sensor:
        manh = abs((sens["coord"][0] - x)) + abs((sens["coord"][1] - y))
        if sens["dist"] >= manh:
            return False
    print("FOUND")
    print(x)
    print(y)
    print(x * 4000000 + y)
    return True


for sens in sensor:
    for i in range(sens["dist"]+1):
        x = sens["coord"][0] + sens["dist"]+1 - i
        y = sens["coord"][1] - i
        if is_valid_pos(x, y):
            break

for sens in sensor:
    for i in range(sens["dist"]+1):
        x = sens["coord"][0] + i
        y = sens["coord"][1] + sens["dist"]+1 - i
        if is_valid_pos(x, y):
            break

for sens in sensor:
    for i in range(sens["dist"]+1):
        x = sens["coord"][0] - sens["dist"]+1 - i
        y = sens["coord"][1] - i
        if is_valid_pos(x, y):
            break

for sens in sensor:
    for i in range(sens["dist"]+1):
        x = sens["coord"][0] - i
        y = sens["coord"][1] - sens["dist"]+1 - i
        if is_valid_pos(x, y):
            break




found = False
for x in range(4000001):
    print(x)
    if found:
        break
    for y in range(4000001):
        if is_valid_pos(x, y):
            found = True
            break
