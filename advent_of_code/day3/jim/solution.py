import re 

pattern_number = r'\d+'
pattern_symbol = re.compile(r'[^\w\s.]')

def main(problem_input: list[str]):
       
    key_line = 1
    key_number = 0
    key_symbol = 0 
    total = [] 
    number_dict = {}
    symbol_dict = {}

    for line in problem_input:
        
        for match_number in re.finditer(pattern_number, line):
            number_list = []
            number_list.append(key_line)
            number_list.append(match_number.group(0))
            number_list.append(match_number.span())
            number_dict[key_number] = number_list
            key_number += 1
            
        for match_symbol in re.finditer(pattern_symbol, line):
            symbol_list = []
            symbol_list.append(key_line)
            symbol_list.append(match_symbol.group(0))
            symbol_list.append(match_symbol.span())
            symbol_dict[key_symbol] = symbol_list
            key_symbol += 1
    
        key_line += 1
    
    for _, number_info in number_dict.items():
        for _, symbol_info in symbol_dict.items():
            
            number_span = list(range(number_info[2][0], number_info[2][1])) 
            symbol_span = symbol_info[2][0]
            
            if number_info[0] == symbol_info[0] or number_info[0] == symbol_info[0] - 1 or number_info[0] == symbol_info[0] + 1:
                for span in number_span:
                        if span == symbol_span - 1 or span == symbol_span + 1 or span == symbol_span:
                            total.append(int(number_info[1]))
                            break
    return sum(total)