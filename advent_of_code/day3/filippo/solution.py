import re
from dataclasses import dataclass


def main_part_one(problem_input: list[str]):
    return


def main_part_two(problem_input: list[str]):
    return


@dataclass
class Number:
    value: int
    starting_index: int
    ending_index: int


def extract_numbers_from_line(line: str) -> int:
    matches = re.findall(r"\d+", line)
    return [Number(int(x), 0, 0) for x in matches]
