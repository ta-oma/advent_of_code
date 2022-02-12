import numpy as np
from bitstring import BitArray

diag_arr = []
gamma_rate = []
epsilon_rate = []
power_consumption = 0
first = 0
zero_count = 0
one_count = 0

with open("diag.txt", "r") as file:
    for line in file:
        line_text = str(line).replace('\n', '')
        diag_arr.append(line_text)
    binary_len = len(diag_arr[0])


for j in range(0, binary_len):
    for i in range(0, len(diag_arr)):
        if diag_arr[i][j] == "0":
            zero_count += 1
        if diag_arr[i][j] == "1":
            one_count += 1
    gamma_rate.append("0" if zero_count > one_count else "1")
    epsilon_rate.append("0" if zero_count < one_count else "1")
    zero_count = 0
    one_count = 0


print(int(''.join(gamma_rate), 2) * int(''.join(epsilon_rate), 2))


