import re
from collections import defaultdict
import numpy as np

def main(problem_input: list[str]):
    
    number_pattern = r'(\d+)'
    letter_pattern = r'[a-zA-Z]'
    map_dict = defaultdict(list)
    locations = []
    seeds_ranges = []
    total = []
    
    for line in problem_input:
        
        ## Part One        
        # if re.match("seeds", line):
        #     line_list = line.split(":")
        #     seeds = re.findall(number_pattern, line_list[1])
        #     seeds_range = [int(seed) for seed in seeds]
        #     continue
        
        ## Part Two  
        if re.search("seeds", line):
            line_list = line.split(":")
            seeds_list = re.findall(number_pattern, line_list[1])
            seeds_list = [int(seed) for seed in seeds_list]
            seeds_list = np.array(seeds_list)
            seeds_list = np.array_split(seeds_list, seeds_list.shape[0] // 2)
            for couple in seeds_list:
                seeds_range = range(couple[0], couple[0] + couple[1])
                seeds_ranges.append(seeds_range)
            continue
            
        if line == "":
            continue
        
        if re.search(letter_pattern, line):
            line_key = line.rstrip(" map:")
            map_dict[line_key] = []
            continue

        if re.search(number_pattern, line):
            numbers = re.findall(number_pattern, line)
            numbers = [int(number) for number in numbers]
            map_dict[line_key].append(numbers)
        
    for seeds_range in seeds_ranges:
        print("NEW RANGE")
        print(seeds_range)
        for _, content in map_dict.items():
            for row in content:
                print("Start range")
                print(seeds_range)
                diff = row[1] - row[0]
                source_range = range(row[1], row[1] + row[2])
                print("Source")
                print(source_range)
                common_range = range(max(seeds_range[0], source_range[0]), min(
                    seeds_range[-1], source_range[-1])+1)
                print("Common range")
                print(common_range)
                if common_range and common_range == seeds_range:
                    seeds_range = range(common_range[0] - diff, (common_range[-1] - diff + 1))
                    print("common = start", seeds_range)
                    break
                elif common_range and common_range != seeds_range:
                    seeds_range_common = range(common_range[0] - diff, (common_range[-1] - diff + 1))
                    print("common", seeds_range_common)
                    seeds_range_uncommon = range(seeds_range[0], common_range[0]) if seeds_range[
                        0] < common_range[0] else range(common_range[-1] + 1, seeds_range[-1] + 1)
                    print("uncommon",seeds_range_uncommon) 
                    if seeds_range_common[0] < seeds_range_uncommon[0]:
                        seeds_range = seeds_range_common
                        print("common < uncommon", seeds_range)
                        break
                    elif seeds_range_uncommon[0] < seeds_range_common[0]:
                        seeds_range = seeds_range_uncommon
                        print("uncommon < common", seeds_range)
                        break
        total.append(seeds_range)
        for i in total:
            locations.append(i[0])  
                    
        # One indent less for part one
        # for seed in seeds_range:
        #     for _, content in map_dict.items():
        #         for row in content:
        #             source_dest_diff = row[1] - row[0]
        #             source_range = range(row[1], row[1] + row[2])
        #             if seed in source_range:
        #                 seed = seed - source_dest_diff
        #                 break
        #     locations.append(seed)                    
    
    return min(locations)