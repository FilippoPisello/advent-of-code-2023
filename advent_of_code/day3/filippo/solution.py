import re

def main_part_one(problem_input: list[str]):
    return


def main_part_two(problem_input: list[str]):
    return


def extract_numbers_from_line(line: str) -> int:
   matches = re.findall(r"\d+",line)
   return [int(x) for x in matches]