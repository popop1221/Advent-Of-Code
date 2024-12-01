import os

year = "2024"

os.mkdir(year)

with open('template.py') as f:
    template = f.readlines()

for i in range(25):
    os.mkdir(f"./{year}/{i+1}")
    with open(f"./{year}/{i+1}/{i+1}.py", "w") as f:
        f.writelines(template)
    with open(f"./{year}/{i+1}/input.txt", "w") as f:
        pass
    with open(f"./{year}/{i+1}/test_input.txt", "w") as f:
        pass
