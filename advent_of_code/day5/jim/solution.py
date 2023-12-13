import re
from collections import defaultdict

def main(problem_input: list[str]):
    
    number_pattern = r'(\d+)'
    letter_pattern = r'[a-zA-Z]'
    map_dict = defaultdict(list)
    locations = []
    
    for line in problem_input:
        
        if re.match("seeds", line):
            line_list = line.split(":")
            seeds = re.findall(number_pattern, line_list[1])
            seeds = [int(seed) for seed in seeds]
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
            map_dict = dict(map_dict)
    
    for seed in seeds:
        for _, content in map_dict.items():
            for row in content:
                source_dest_diff = row[1] - row[0]
                source_range = range(row[1], row[1] + row[2])
                if seed in source_range:
                    seed = seed - source_dest_diff
                    break
        locations.append(seed)                    
    
    return min(locations)