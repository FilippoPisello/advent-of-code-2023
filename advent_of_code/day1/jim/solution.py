import pandas as pd 
import numpy as np

f = open("day1_1\day1_1.txt", "r")
print(f.read()[0])

combinations = []
for i in f.read():
    if f.read()[i].isnumeric():
        combinations.append(f.read()[i])

print(combinations)
