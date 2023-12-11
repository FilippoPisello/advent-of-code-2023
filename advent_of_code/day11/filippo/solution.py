from dataclasses import dataclass


def main_part_one(problem_input: list[str]):
    expanded_input = _calculate_expanded_input(problem_input)
    galaxies = _parse_galaxies(expanded_input)
    return _sum_shortest_distances(galaxies)


@dataclass
class Galaxy:
    x: int
    y: int


def _calculate_expanded_input(problem_input: list[str]) -> list[str]:
    return


def _parse_galaxies(expanded_input: list[str]) -> list[Galaxy]:
    return


def _sum_shortest_distances(galaxies: list[Galaxy]) -> int:
    return


def main_part_two(problem_input: list[str]):
    return
