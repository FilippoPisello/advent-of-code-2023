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
    return


def _parse_galaxies(expanded_input: list[str]) -> list[Galaxy]:
    return


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
