# Libraries
import re

# Importing data
with open('data/day3-ex1.txt', 'r') as file: 
    ex1 = file.read().splitlines()[0]

with open('data/day3-ex2.txt', 'r') as file: 
    ex2 = file.read().splitlines()[0]

with open('data/day3-dat.txt', 'r') as file: 
    dat = file.read().splitlines()

# Part 1
# ------

def find_and_compute (line, reg="(?:mul)\((\d{1,3},\d{1,3})\)"):
    x = [int(x[0]) * int(x[1]) for x in [x.split(",") for x in re.findall(reg, line)]]
    return sum(x)

find_and_compute(ex1) == 161
sum([find_and_compute(line) for line in dat])

# Part 2
# ------

def find_and_compute_2 (line, reg="(?:mul)\((\d{1,3},\d{1,3})\)"):
    line = ''.join([x[0] for x in [line.split("don't()") for line in line.split("do()")]])
    print(line)
    x = [int(x[0]) * int(x[1]) for x in [x.split(",") for x in re.findall(reg, line)]]
    return sum(x)

find_and_compute_2(ex2) == 48
find_and_compute_2(''.join(dat))
