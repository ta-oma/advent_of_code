import numpy as np

a = np.loadtxt(fname="input.txt")

measurements = []


for num in a:
    measurements.append(int(num))

total = 0

for m in range(0, len(measurements)):
    if measurements[m-1] < measurements[m]:
        total = total+1
    else:
        pass

print(total)

