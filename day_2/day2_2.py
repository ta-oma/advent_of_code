d = {"forward": 0, "up": 0, "down": 0}

hor_pos = 0
depth = 0
aim = 0


with open("directions.txt", "r") as file:
    for line in file:
        key, value = line.split()
        d[key] = d[key] + int(value)
        if key == "forward":
            hor_pos = hor_pos + int(value)
            depth = depth + (aim * int(value))
        if key == "up":
            aim -= int(value)
        if key == "down":
            aim += int(value)


print(hor_pos, depth, aim)
print(hor_pos * depth)


