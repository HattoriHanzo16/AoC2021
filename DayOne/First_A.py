
"""
Day 1 of AoC2021(Advent of code 2021)


the statement of the problem:
https://adventofcode.com/2021/day/1

"""


"""
First part of the solution
"""


def solveA(measurements):
    ret = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i-1]:
            ret += 1
    return ret


"""
Second part of the solution
"""


def solveB(measurements):
    ret = 0
    prev = 0
    for i in range(len(measurements)-2):
        curr = 0
        for j in range(3):
            curr += measurements[i+j]
        print(curr, prev)
        if curr > prev:
            ret += 1
        prev = curr
    return ret-1


"""
Getting the input data
"""

input_file = open("input.txt", "r")
lst = [int(i.strip()) for i in input_file.readlines()]
print(solveB(lst))
