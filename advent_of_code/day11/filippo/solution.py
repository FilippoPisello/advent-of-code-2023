import re
from dataclasses import dataclass
from typing import Self


def main_part_one(problem_input: list[str]):
    expanded_input = _calculate_expanded_input(problem_input)
    galaxies = _parse_galaxies(expanded_input)
    return _sum_shortest_distances(galaxies)


@dataclass
class Galaxy:
    x: int
    y: int

    def distance(self, other: Self) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)


def _calculate_expanded_input(problem_input: list[str]) -> list[str]:
    new_universe = []
    new_universe = expand_rows(problem_input)
    return expand_columns(new_universe)


def expand_rows(problem_input: list[str]) -> list[str]:
    expanded_universe = []
    for i in problem_input:
        if "#" in i:
            expanded_universe.append(i)
        else:
            expanded_universe.append(i)
            expanded_universe.append(i)

    return expanded_universe


def expand_columns(problem_input: list[str]) -> list[str]:
    expanded_universe = [[] for _ in problem_input]
    for i, _ in enumerate(problem_input[0]):
        column = [row[i] for row in problem_input]
        for index, row in enumerate(expanded_universe):
            if "#" in column:
                row.append(column[index])
            else:
                row.append(column[index])
                row.append(column[index])
    return ["".join(row) for row in expanded_universe]


def _parse_galaxies(expanded_input: list[str]) -> list[Galaxy]:
    galaxies = []
    expr = re.compile(r"#")
    for y, line in enumerate(expanded_input):
        for match in expr.finditer(line):
            galaxies.append(Galaxy(match.span()[0], y))
    return galaxies


def _sum_shortest_distances(galaxies: list[Galaxy]) -> int:
    pairs_checked = set()
    distance = 0
    for index, galaxy in enumerate(galaxies):
        for other_index, other_galaxy in enumerate(galaxies):
            pair = f"{min(index, other_index)}-{max(index, other_index)}"
            if (index == other_index) or (pair in pairs_checked):
                continue
            distance += galaxy.distance(other_galaxy)
            pairs_checked.add(pair)
    return distance


def main_part_two(problem_input: list[str]):
    return
