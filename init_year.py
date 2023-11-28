import os

year = "2023"

os.mkdir("2023")

with open('template.py') as f:
    template = f.readlines()

for i in range(25):
    os.mkdir(f"./2023/{i+1}")
    with open(f"./2023/{i+1}/{i+1}.py", "w") as f:
        f.writelines(template)
    with open(f"./2023/{i+1}/input.txt", "w") as f:
        pass
    with open(f"./2023/{i+1}/test_input.txt", "w") as f:
        pass
