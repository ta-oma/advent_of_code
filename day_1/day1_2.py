import numpy as np

a = np.loadtxt(fname="input.txt")

measurements = []

for num in a:
    measurements.append(int(num))

total = 0

sums = []

for m in range(0, len(measurements)):
    try:
        sums.append(measurements[m] + measurements[m+1] + measurements[m+2])
    except:
        pass

for i in range(1, len(sums)):
    if sums[i] > sums[i-1]:
        total += 1


print(total)