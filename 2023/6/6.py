def evaluate(time, dist):
    result = 0
    for i in range(time):
        if (time - i) * i > dist:
            result += 1
    return result


print(evaluate(55, 401) * evaluate(99, 1485) * evaluate(97, 2274) * evaluate(93, 1405))

print("----- PART 2 -----")
print(evaluate(55999793, 401148522741405))
