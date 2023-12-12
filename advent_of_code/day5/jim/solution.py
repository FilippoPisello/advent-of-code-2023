import re

def main(problem_input: list[str]):
    
    number_pattern = r'(\d+)'
    letter_pattern = r'/^[a-z]+$/'
    seeds_list = []
    
    for line in problem_input:
        print(line)
        
        if re.match("seeds", line):
            line = line.split(":")
            seeds = re.findall(number_pattern, line[1])
            seeds = [int(seed) for seed in seeds]
            seeds_list.append(seeds)
            
        if line == "":
            continue
        
        if re.finditer(letter_pattern, line):
            print(line)
    
    return seeds