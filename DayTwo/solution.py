
"""
Day 2 of AoC2021(Advent of code 2021)


the statement of the problem:
https://adventofcode.com/2021/day/2

"""


"""
---Part One---
"""


def solveA(commands):
    hor_pos = 0
    depth = 0
    for i in commands:
        if i[0] == 'forward':
            hor_pos += int(i[1])
        elif i[0] == 'down':
            depth += int(i[1])
        if i[0] == 'up':
            depth -= int(i[1])
    return depth*hor_pos


"""
---Part Two---
"""


def solveB(commands):
    hor_pos = 0
    depth = 0
    aim = 0
    for i in commands:
        if i[0] == 'forward':
            hor_pos += int(i[1])
            depth += aim*int(i[1])
        elif i[0] == 'down':
            aim += int(i[1])
        if i[0] == 'up':
            aim -= int(i[1])

    return depth*hor_pos


"""
Getting the input data
"""

input_file = open("input.txt", "r")
lst = [(i.strip()).split() for i in input_file.readlines()]
print(solveB(lst))
