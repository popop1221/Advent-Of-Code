from hashlib import md5

with open('input.txt') as f:
    lines = f.readlines()

with open('test_inputs') as f:
    test_input = f.readlines()

blueprints = []
for line in lines:
#for line in test_input:
    line = line.replace("\n", "")
    temp = line.split(" ")
    robots = {}
    robots["ore"] = int(temp[6])
    robots["clay"] = int(temp[12])
    robots["obsidian"] = (int(temp[18]), int(temp[21]))
    robots["geode"] = (int(temp[27]), int(temp[30]))
    robots["max_ore"] = max(int(temp[12]), int(temp[18]), int(temp[27]))
    blueprints.append(robots)

memo = {}
geo_max = [0 for i in range(30)]
minute_todo = 24
def simulate(minute, blueprint, ore_r, clay_r, obsi_r, geo_r, ore, clay, obsi, geo):
    global geo_max
    global memo
    if minute == minute_todo:
        return geo

    if geo + (minute_todo + 2 - minute) < geo_max[minute]:
        return geo_max[minute]

    sha = md5(bytes([minute, ore_r, clay_r, obsi_r, geo_r, ore, clay, obsi, geo])).hexdigest()
    if sha in memo.keys():
        return memo[sha]
    ore_o = ore
    clay_o = clay
    obsi_o = obsi
    ore += ore_r
    clay += clay_r
    obsi += obsi_r
    geo += geo_r
    geo_max[minute] = max(geo_max[minute], geo)

    results = []
    if ore_o >= blueprint["ore"] and ore_r < blueprint["max_ore"]:
        results.append(simulate(minute + 1, blueprint, ore_r + 1, clay_r, obsi_r, geo_r, ore - blueprint["ore"], clay, obsi, geo))
    if ore_o >= blueprint["clay"]:
        results.append(simulate(minute + 1, blueprint, ore_r, clay_r + 1, obsi_r, geo_r, ore - blueprint["clay"], clay, obsi, geo))
    if ore_o >= blueprint["obsidian"][0] and clay_o >= blueprint["obsidian"][1]:
        results.append(simulate(minute + 1, blueprint, ore_r, clay_r, obsi_r + 1, geo_r, ore - blueprint["obsidian"][0], clay  - blueprint["obsidian"][1], obsi, geo))
    if ore_o >= blueprint["geode"][0] and obsi_o >= blueprint["geode"][1]:
        results.append(simulate(minute + 1, blueprint, ore_r, clay_r, obsi_r, geo_r + 1, ore - blueprint["geode"][0], clay, obsi - blueprint["geode"][1], geo))
    results.append(simulate(minute + 1, blueprint, ore_r, clay_r, obsi_r, geo_r, ore, clay, obsi, geo))
    new_max = max(results)
    memo[sha] = new_max
    return new_max

result = 0
id = 1
for blueprint in blueprints:
    memo = {}
    geo_max = [0 for i in range(30)]
    result += id * simulate(0, blueprint, 1, 0, 0, 0, 0, 0, 0, 0)
    id += 1

print(result)

print("----- PART 2 -----")
result = 1
for i in range(3):
    minute_todo = 32
    memo = {}
    geo_max = [0 for j in range(35)]
    result *= simulate(0, blueprints[i], 1, 0, 0, 0, 0, 0, 0, 0)

print(result)
