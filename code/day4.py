# Libraries
import numpy as np

# Importing data
with open('data/day4-ex1.txt', 'r') as file: 
    ex1 = file.readlines()
ex1_parsed = np.pad(np.array([list(line) for line in
    [line.strip() for line in ex1]]), 3, constant_values='.')

with open('data/day4-dat.txt', 'r') as file: 
    dat = file.readlines()
dat_parsed = np.pad(np.array([list(line) for line in
    [line.strip() for line in dat]]), 3, constant_values='.')

# Part 1
# ------    

paths = np.array(
        # Cardinals
        [[[ 0,  0],[0, 1], [0, 2], [0, 3]], # right
        [[ 0,  0],[0, -1], [0, -2], [0, -3]], # left
        [[ 0,  0],[1, 0], [2, 0], [3, 0]], # bottom
        [[ 0,  0],[-1, 0], [-2, 0], [-3, 0]], # top
        # Diagonals
        [[ 0,  0],[-1, -1], [-2, -2], [-3, -3]], # top left
        [[ 0,  0],[-1, 1], [-2, 2], [-3, 3]], # top right
        [[ 0,  0],[1, -1], [2, -2], [3, -3]], # bottom left
        [[ 0,  0],[1, 1], [2, 2], [3, 3]] # bottom right
        ])

def match_and_count (arr, paths=paths):
    x_list = np.where(arr == "X")
    x_locs = [[x_list[0][i], x_list[1][i]] for i in range(0, len(x_list[0]))]
    paths_locs = [[a + b for b in paths] for a in x_locs]
    words = [[[''.join([arr[i, j] for i,j in path])]
            for path in paths_locs[x]]
            for x in range(0, len(paths_locs))]
    matches = np.ndarray.flatten(np.array(words)) == 'XMAS'
    return sum(matches)

match_and_count(ex1_parsed) == 18
match_and_count(dat_parsed)

# Part 2
# ------

mask = np.array([[-1,-1], [-1, 1], [1, -1], [1, 1]])

def match_and_count_2 (arr, mask=mask):
    x_list = np.where(arr == "A")
    x_locs = [[x_list[0][i], x_list[1][i]] for i in range(0, len(x_list[0]))]
    mask_locs = [[a + b for b in mask] for a in x_locs]
    letters = [[arr[i, j] for i,j in path]
            for path in mask_locs]
    print(letters)
    matches = [((x.count('M') == 2) & (x.count('S') == 2) & (x[0] != x[3])) 
               for x in letters]
    return sum(matches)

match_and_count_2(ex1_parsed) == 9
match_and_count_2(dat_parsed) # 2072 too high