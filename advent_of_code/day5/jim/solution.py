import re
from collections import defaultdict


def main(problem_input: list[str]):
    
    number_pattern = r'(\d+)'
    letter_pattern = r'[a-zA-Z]'
    seeds_list = []
    map_dict = defaultdict(list)
    
    for line in problem_input:
        
        if re.match("seeds", line):
            line_list = line.split(":")
            seeds = re.findall(number_pattern, line_list[1])
            seeds = [int(seed) for seed in seeds]
            seeds_list.append(seeds)
            continue
            
        if line == "":
            continue
        
        if re.match(letter_pattern, line):
            line_key = line.rstrip(" map:")
            map_dict[line_key] = []
            continue

        if re.match(number_pattern, line):
            numbers = re.findall(number_pattern, line)
            numbers = [int(number) for number in numbers]
            map_dict[line_key].append(numbers)
    
    return seeds, dict(map_dict)