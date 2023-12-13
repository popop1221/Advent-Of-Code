import hashlib

inputt = "ckczppom"

result = 0
while not hashlib.md5((inputt + str(result)).encode()).hexdigest().startswith("00000"):
    result += 1

print(result)

print("----- PART 2 -----")

result = 0
while not hashlib.md5((inputt + str(result)).encode()).hexdigest().startswith("000000"):
    result += 1

print(result)
