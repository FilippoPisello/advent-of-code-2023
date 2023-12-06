import re
import string
from dataclasses import dataclass
from typing import ClassVar


def main_part_one(problem_input: list[str]):
    total = 0
    for index, current_row in enumerate(problem_input):
        previous_row = _get_row(index - 1, problem_input)
        next_row = _get_row(index + 1, problem_input)
        numbers = extract_numbers_from_line(current_row)
        for number in numbers:
            if has_symbol(current_row, number.same_row_indexes) or has_symbol(
                previous_row, number.adjacent_row_indexes
            ) or has_symbol(next_row, number.adjacent_row_indexes):
                total += number.value
    return total

def _get_row(index: int, problem_input: list[str]) -> str:
    try:
        return problem_input[index]
    except IndexError:
        return "A" * 140


def main_part_two(problem_input: list[str]):
    return


@dataclass
class Number:
    value: int
    starting_index: int
    ROW_LENGTH: ClassVar[int] = 140

    @property
    def number_length(self) -> int:
        return len(str(self.value))

    @property
    def ending_index(self) -> int:
        return self.starting_index + self.number_length - 1

    @property
    def occupied_indexes(self) -> set[int]:
        return {x for x in range(self.starting_index, self.ending_index + 1)}

    @property
    def same_row_indexes(self) -> set[int]:
        if self.starting_index == 0:
            return set([self.ending_index + 1])
        elif self.ending_index == (self.ROW_LENGTH - 1):
            return set([self.starting_index - 1])
        else:
            return set([self.starting_index - 1, self.ending_index + 1])

    @property
    def adjacent_row_indexes(self) -> list[int]:
        return self.same_row_indexes | self.occupied_indexes


def extract_numbers_from_line(line: str) -> int:
    expr = re.compile(r"\d+")
    return [
        Number(int(match.group()), match.span()[0]) for match in expr.finditer(line)
    ]


def has_symbol(line: str, indexes: str) -> bool:
    symbols = string.punctuation.replace(".", "")
    for index in indexes:
        if line[index] in symbols:
            return True
    return False
