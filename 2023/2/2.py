with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input

result = 0
i = 0
for line in inputt:
    i += 1
    batchs = line.split(";")
    for batch in batchs:
        blue = 0
        red = 0
        green = 0
        res = batch.split(",")
        work = True
        for r in res:
            temp = r.split(" ")
            if r.startswith("G"):
                if temp[3].startswith("r"):
                    red += int(temp[2])
                if temp[3].startswith("g"):
                    green += int(temp[2])
                if temp[3].startswith("b"):
                    blue += int(temp[2])

                if green > 13 or red > 12 or blue > 14:
                    work = False
                    break
                continue
            if temp[2].startswith("r"):
                red += int(temp[1])
            if temp[2].startswith("g"):
                green += int(temp[1])
            if temp[2].startswith("b"):
                blue += int(temp[1])

            if green > 13 or red > 12 or blue > 14:
                work = False
                break
        if not work:
            break
    else:
        result += i

print(result)

print("----- PART 2 -----")

i = 0
result = 0
for line in inputt:
    i += 1
    batchs = line.split(";")
    max_blue = 0
    max_red = 0
    max_green = 0
    for batch in batchs:
        blue = 0
        red = 0
        green = 0
        res = batch.split(",")
        for r in res:
            temp = r.split(" ")
            if r.startswith("G"):
                if temp[3].startswith("r"):
                    red += int(temp[2])
                if temp[3].startswith("g"):
                    green += int(temp[2])
                if temp[3].startswith("b"):
                    blue += int(temp[2])

            if temp[2].startswith("r"):
                red += int(temp[1])
            if temp[2].startswith("g"):
                green += int(temp[1])
            if temp[2].startswith("b"):
                blue += int(temp[1])
        max_blue = max(blue, max_blue)
        max_green = max(green, max_green)
        max_red = max(red, max_red)
    result += max_red * max_green * max_blue

print(result)
