def is_valid(password):
    if "i" in password or "o" in password or "l" in password:
        return False

    temp = [ord(c) for c in password]
    for i in range(len(temp) - 2):
        if temp[i+1] == temp[i] + 1 and temp[i+2] == temp[i] + 2:
            break
    else:
        return False

    count = 0
    i = 0
    while i < len(temp) - 1:
        if temp[i] == temp[i+1]:
            i += 1
            count += 1
        i += 1

    return count >= 2

def next_password(password):
    for i in range(len(password)):
        if password[i] in "iol":
            password[i] = chr(ord(result[i]) + 1)
            for j in range(i + 1, len(password)):
                password[j] = "a"
            return

    for i in range(len(password) - 1, -1, -1):
        if password[i] != "z":
            password[i] = chr(ord(result[i]) + 1)
            return
        password[i] = "a"


result = [c for c in "cqjxjnds"]
result[-1] = "a" if result[-1] == "z" else chr(ord(result[-1]) + 1)
print(result)
next_password(result)
while not is_valid(result):
    next_password(result)

print(*result)

print("----- PART 2 -----")

next_password(result)
while not is_valid(result):
    next_password(result)

print(*result)
