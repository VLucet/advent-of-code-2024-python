# Libraries
import pandas as pd
from collections import Counter

# Importing data
ex1 = pd.read_csv('data/day1-ex1.txt', sep='   ', engine='python', header=None, 
                  names=["a", "b"])
print(ex1.head())

dat = pd.read_csv('data/day1-dat.txt', sep='   ', engine='python', header=None, 
                  names=["a", "b"])
print(dat.head())

# Part 1
# ------

def sort_distance_sum (df):
    df_sorted = df.apply(lambda col: col.sort_values().values, axis=0)
    df_distanced = df_sorted.apply(lambda vals: abs(vals.iloc[0] - vals.iloc[1]), 
                                   axis=1)
    return sum(df_distanced)

sort_distance_sum(ex1) == 11
sort_distance_sum(dat)

# Part 2
# ------

def similarity_score (df):
    counts = Counter(df.b)
    score = sum(df.a.apply(lambda x: counts[x] * x))
    return score

similarity_score(ex1) == 31
similarity_score(dat)