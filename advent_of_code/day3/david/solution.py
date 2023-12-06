import os
import re

def main_part_one(problem_input: list[str]):

    max_row = len(problem_input)
    max_col = len(problem_input[0])
    
    print(max_row)
    for index, string in enumerate(problem_input):
        pattern = r'\d+'
        matches = re.finditer(pattern, string)
        result = []
        for match in matches:
            start_index = match.start()
            number = int(match.group())

            break_outer_loop = False
            print(f">>>>>>>>>>>>>>>> number: {number} <<<<<<<<<<<<<<<<<")
            for i in [index-1,index,index+1]: 
                if i<0 or i>max_row-1:
                    print("ok")

                else:
                    if(i==index-1):
                        for j in list(range(start_index-1,start_index+len(str(number)))):
                            print(f"{index} col {j}")
                            if j<0 or j>max_col-1:
                                # print("out of range")
                                "yo"
                            elif problem_input[i][j].isdigit == 1 or problem_input[i][j] == ".":
                                # print("")
                                "yo"
                            else:
                                result.append(number)
                                break_outer_loop = True
                                break
                    
                    if(i==index):
                        for j in [start_index-1,start_index+len(str(number))]:
                            if j<0 or j>max_col-1:
                                # print("out of range")
                                "yo"
                            elif problem_input[i][j].isdigit == 1 or problem_input[i][j] == ".":
                                # print("")
                                "yo"
                            else:
                                result.append(number)
                                break_outer_loop = True
                                break

                    if(i==index+1):
                        for j in list(range(start_index-1,start_index+len(str(number)))):
                            if j<0 or j>max_col-1:
                                # print("out of range")
                                "yo"
                            elif problem_input[i][j].isdigit == 1 or problem_input[i][j] == ".":
                                # print("not a number yet")
                                "yo"
                            else:
                                result.append(number)
                                break_outer_loop = True
                                break

                if break_outer_loop:
                    break
    return result
                                    


                    

        


