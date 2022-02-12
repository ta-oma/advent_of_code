d = {"forward": 0, "up": 0, "down": 0}

with open("directions.txt", "r") as file:
    for line in file:
        key, value = line.split()
        d[key] = d[key] + int(value)

hor_pos = 0
depth = 0

for key, value in d.items():
    if key == "forward":
        hor_pos = hor_pos + int(value)
    if key == "up":
        depth = depth - int(value)
    if key == "down":
        depth = depth + int(value)


print(hor_pos * depth)


