from dataclasses import dataclass
import re


@dataclass
class Symbol:
    symbol: str
    x: int
    y: int


def main(problem_input: list[str]):
    map_symbol = mapping_symbol(problem_input)
    return map_symbol


def mapping_symbol(problem_input):
    return [
        Symbol(
            symbol=problem_input[y][],
            x=x,
            y=y,
        )
        for x in range(len(problem_input[0]))
        for y in range(len(problem_input))
        if problem_input[y][x] not in "1234567890."
    ]
