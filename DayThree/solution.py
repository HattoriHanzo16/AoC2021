
"""
Day 3 of AoC2021(Advent of code 2021)


the statement of the problem:
https://adventofcode.com/2021/day/3

"""

"""
---Part One---
"""




from copy import copy
def convert(st):
    ret = 0
    for ind, bit in enumerate(st):
        ret += 2**(len(st)-1-ind) * int(bit)
    return ret


def Power_Consumption(matr):
    gamma_rate = ""
    epsilon_rate = ""
    for i in range(len(matr[0])):
        one = 0
        zero = 0
        for j in range(len(matr)):
            if matr[j][i] == '1':
                one += 1
            else:
                zero += 1
        curr = 1 if one > zero else 0
        gamma_rate += str(curr)
        epsilon_rate += '0' if curr == 1 else '1'
        print(gamma_rate, epsilon_rate)

    return convert(gamma_rate) * convert(epsilon_rate)


"""
---Part Two---
"""

input_file = open("input.txt", "r")
lst = [i.strip() for i in input_file.readlines()]


oxygen = copy(lst)
for i in range(len(oxygen[0])):
    if len(oxygen) == 1:
        break
    all_entries = [entry[i] for entry in oxygen]
    common = '1' if all_entries.count('1') >= len(oxygen)/2 else '0'
    oxygen = [entry for entry in oxygen if entry[i] == common]
print(convert(oxygen[0]))


co2 = copy(lst)
for i in range(len(co2[0])):
    if len(co2) == 1:
        break
    all_entries = [entry[i] for entry in co2]
    least_common = '0' if all_entries.count('1') >= len(co2)/2 else '1'
    co2 = [entry for entry in co2 if entry[i] == least_common]
print(convert(co2[0]))
