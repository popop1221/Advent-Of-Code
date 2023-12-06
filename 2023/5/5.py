with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input

seeds = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temp = []
temp_to_hum = []
hum_to_loc = []
steps = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temp, temp_to_hum, hum_to_loc]

step = 0
for line in inputt:
    line = line.replace("\n", "")
    if step == 0:
        seeds = [int(elem) for elem in line.split(" ")[1:]]
        step += 1
        continue
    if line.startswith("seed-to"):
        step += 1
        continue
    if step == 2:
        if line != "" and line[0].isnumeric():
            seed_to_soil.append([int(elem) for elem in line.split(" ")])

    if line.startswith("soil-to"):
        step += 1
        continue
    if step == 3:
        if line != "" and line[0].isnumeric():
            soil_to_fertilizer.append([int(elem) for elem in line.split(" ")])

    if line.startswith("fertilizer-to"):
        step += 1
        continue
    if step == 4:
        if line != "" and line[0].isnumeric():
            fertilizer_to_water.append([int(elem) for elem in line.split(" ")])

    if line.startswith("water-to"):
        step += 1
        continue
    if step == 5:
        if line != "" and line[0].isnumeric():
            water_to_light.append([int(elem) for elem in line.split(" ")])

    if line.startswith("light-to"):
        step += 1
        continue
    if step == 6:
        if line != "" and line[0].isnumeric():
            light_to_temp.append([int(elem) for elem in line.split(" ")])

    if line.startswith("temperature-to"):
        step += 1
        continue
    if step == 7:
        if line != "" and line[0].isnumeric():
            temp_to_hum.append([int(elem) for elem in line.split(" ")])

    if line.startswith("humidity-to"):
        step += 1
        continue
    if step == 8:
        if line != "" and line[0].isnumeric():
            hum_to_loc.append([int(elem) for elem in line.split(" ")])

print(seeds)
print(seed_to_soil)
print(soil_to_fertilizer)
print(fertilizer_to_water)
print(water_to_light)
print(light_to_temp)
print(temp_to_hum)
print(hum_to_loc)


def evaluate(step_id, value, curr_min):
    if step_id == len(steps):
        if value < curr_min[0]:
            curr_min[0] = value
        return

    count = 0
    for temp in steps[step_id]:
        if temp[1] <= value <= temp[1] + temp[2]:
            evaluate(step_id + 1, temp[0] + value - temp[1], curr_min)
            count += 1
    if count == 0:
        evaluate(step_id + 1, value, curr_min)


result = [1000000000000]
for seed in seeds:
    evaluate(0, seed, result)

print(result)
print("----- PART 2 -----")


def unused(input, used):
    result = []
    start, end = input
    current_start = start

    for used_start, used_end in sorted(used):
        if current_start < used_start:
            result.append((current_start, used_start - 1))
        current_start = max(current_start, used_end + 1)

    if current_start <= end:
        result.append((current_start, end))

    return result


def evaluate_2(step_id, value_start, value_end, curr_min):
    if step_id == len(steps):
        if value_start < curr_min[0]:
            curr_min[0] = value_start
        return

    used = []
    for temp in steps[step_id]:
        if temp[1] <= value_start <= temp[1] + temp[2] - 1 <= value_end:
            evaluate_2(step_id + 1, temp[0] + (value_start - temp[1]), temp[0] + temp[2] - 1, curr_min)
            used.append((value_start, temp[1] + temp[2] - 1))
        elif value_start <= temp[1] <= value_end <= temp[1] + temp[2] - 1:
            evaluate_2(step_id + 1, temp[0], temp[0] + (value_end - temp[1]), curr_min)
            used.append((temp[1], value_end))
        elif value_start <= temp[1] and temp[1] + temp[2] - 1 <= value_end:
            evaluate_2(step_id + 1, temp[0], temp[0] + temp[2] - 1, curr_min)
            used.append((temp[1], temp[1] + temp[2] - 1))
        elif temp[1] <= value_start <= value_end <= temp[1] + temp[2] - 1:
            evaluate_2(step_id + 1, temp[0] + (value_start - temp[1]),
                       temp[0] + (value_start - temp[1]) + (value_end - value_start), curr_min)
            used.append((value_start, value_end))
    for start, end in unused((value_start, value_end), used):
        evaluate_2(step_id + 1, start, end, curr_min)


result = [1000000000000]
i = 0
while i + 1 < len(seeds):
    evaluate_2(0, seeds[i], seeds[i] + seeds[i + 1] - 1, result)
    i += 2

print(result)
