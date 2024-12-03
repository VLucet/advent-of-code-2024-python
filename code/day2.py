# Libraries
import pandas as pd
import numpy as np

# Importing data

with open('data/day2-ex1.txt', 'r') as file: 
    ex1 = file.readlines()
ex1_parsed = [list(map(int, line.split(" "))) for line in (
    [line.strip() for line in ex1])]

with open('data/day2-dat.txt', 'r') as file: 
    dat = file.readlines()
dat_parsed = [list(map(int, line.split(" "))) for line in (
    [line.strip() for line in dat])]

# Part 1
# ------

def check_safety (the_list):
    diffed = [list(np.diff(line)) for line in the_list]
    safety = [((all(np.greater(x, 0)) | all(np.less(x, 0))) & 
      (all(np.greater_equal(np.abs(x), 0)) & all(np.less_equal(np.abs(x), 3)))) 
      for x in diffed]
    safety_sum = sum(safety)
    return safety_sum

check_safety(ex1_parsed) == 2
check_safety(dat_parsed)

# Part 2
# ------

def check_line_safety (line):
    line_diff = np.diff(line)
    safety = ((all(np.greater(line_diff, 0)) | all(np.less(line_diff, 0))) & 
      (all(np.greater_equal(np.abs(line_diff), 0)) & all(np.less_equal(np.abs(line_diff), 3))))
    return safety

def check_line_safety_combinations (line):
    subarrays = [list(np.delete(line, i)) for i in range(0, len(line))]
    subarrays.append(line)
    subsafety = [check_line_safety(x) for x in subarrays]
    return any(subsafety)

sum([check_line_safety_combinations(x) for x in ex1_parsed]) == 4
sum([check_line_safety_combinations(x) for x in dat_parsed])