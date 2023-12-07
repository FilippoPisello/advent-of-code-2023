import re

red = 12
green = 13
blue = 14

pattern_red = r'(\d+)red'
pattern_green = r'(\d+)green'
pattern_blue = r'(\d+)blue'

def main(problem_input: list[str]):
    
    key = 1
    games_dict = {}
    impossible = []
    possible = []
    
    for line in problem_input:
        
        games = line.lstrip(f"Game {key}:")
        games = games.replace(";",",")
        games = games.replace(" ", "")
        games_dict[key] = games
        key += 1
        
    for key, game in games_dict.items():
        r = re.findall(pattern_red, game)
        g = re.findall(pattern_green, game)
        b = re.findall(pattern_blue, game)
        for i in r:
            if int(i) > red:
                impossible.append(key)
        for j in g:
            if int(j) > green:
                impossible.append(key)
        for k in b:
            if int(k) > blue:
                impossible.append(key)

    for i in range (1,101):
        if i not in set(impossible):
            possible.append(i)

    return sum(possible)