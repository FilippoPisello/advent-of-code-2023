import re

def main_part_one(problem_input: list[str]):
    return


def main_part_two(problem_input: list[str]):
    return


def extract_number_from_line(line: str) -> int:
   matches = re.match(r"\d+",line)
   return int(matches[0])