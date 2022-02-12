from bitstring import BitArray


def binary_to_decimal(binary_num):
    dec_num = 0
    m = 1
    for digit in binary_num:
        digit = int(digit)
        dec_num = dec_num + (digit * m)
        m = m * 2
    return dec_num


oxy_gen_rate = []
C02_scrub_rate = []
life_sup_rate = 0
zero_count = 0
one_count = 0

with open("diag.txt", "r") as file:
    for line in file:
        line_text = str(line).replace('\n', '')
        oxy_gen_rate.append(line_text)
        C02_scrub_rate.append(line_text)
    binary_len = len(oxy_gen_rate[0])

while len(C02_scrub_rate) > 1:
    for j in range(0, binary_len):
        for i in range(0, len(C02_scrub_rate)):
            if C02_scrub_rate[i][j] == "0":
                zero_count += 1
            if C02_scrub_rate[i][j] == "1":
                one_count += 1
        x = len(C02_scrub_rate)
        i = 0
        while i < x:
            if zero_count <= one_count:
                if C02_scrub_rate[i][j] == "1":
                    C02_scrub_rate.pop(i)
                    i -= 1
            else:
                if C02_scrub_rate[i][j] == "0":
                    C02_scrub_rate.pop(i)
                    i -= 1
            x = len(C02_scrub_rate)
            i += 1
        zero_count = 0
        one_count = 0
        if len(C02_scrub_rate) == 1:
            break

while len(oxy_gen_rate) > 1:
    for j in range(0, binary_len):
        for i in range(0, len(oxy_gen_rate)):
            if oxy_gen_rate[i][j] == "0":
                zero_count += 1
            if oxy_gen_rate[i][j] == "1":
                one_count += 1
        x = len(oxy_gen_rate)
        i = 0
        while i < x:
            if zero_count <= one_count:
                if oxy_gen_rate[i][j] == "0":
                    oxy_gen_rate.pop(i)
                    i -= 1
            else:
                if oxy_gen_rate[i][j] == "1":
                    oxy_gen_rate.pop(i)
                    i -= 1
            x = len(oxy_gen_rate)
            i += 1
        zero_count = 0
        one_count = 0
        if len(oxy_gen_rate) == 1:
            break

print(int(''.join(C02_scrub_rate), 2) * int(''.join(oxy_gen_rate), 2))