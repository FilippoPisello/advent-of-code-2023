import pandas as pd
from io import StringIO

file = 'input.txt'

with open(file, 'r') as f:
    lines = f.readlines()

cards=[]
cards.append(lines[1])

print(cards)

# Affichez la liste de listes
#print(cards)


#def main_part_one(problem_input: list[str]):
   # return

#def main_part_two(problem_input: list[str]):
    #return
