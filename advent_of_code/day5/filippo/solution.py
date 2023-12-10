from dataclasses import dataclass
from typing import Generator, Iterable, Self

import pytest


def main_part_one(problem_input: list[str]) -> int:
    seeds_str = problem_input[0][7:]
    seeds = [int(seed) for seed in seeds_str.split()]

    maps = parse_maps(problem_input[2:])
    return _get_lowest_possible_destination(seeds, maps)


def main_part_two(problem_input: list[str]):
    seeds_str = problem_input[0][7:]
    seeds = [int(seed) for seed in seeds_str.split()]
    seeds_range = _convert_seeds_to_seed_ranges(seeds)

    maps = parse_maps(problem_input[2:])
    return _get_lowest_possible_destination(seeds_range, maps)


@dataclass
class Map:
    destination_start: int
    source_start: int
    length: int

    @classmethod
    def from_line(cls, line: str):
        destination_start, source_start, length = line.split()
        return cls(
            destination_start=int(destination_start),
            source_start=int(source_start),
            length=int(length),
        )

    def map(self, number: int) -> int:
        if number in range(self.source_start, self.source_start + self.length):
            return number + self.destination_start - self.source_start
        raise ValueError(f"Number {number} is not in range")

    def range(self) -> range:
        return range(self.source_start, self.source_start + self.length)


def merge_maps(maps: list[list[Map]]) -> dict[int, int]:
    output = {}
    for map_section in maps:
        for map in map_section:
            for number in map.range():
                if number in output:
                    output[number] = map.map(output[number])
                output[number] = map.map(number)
    return output


def _convert_seeds_to_seed_ranges(seeds: list[int]) -> Generator[int, None, None]:
    original_starts = seeds[::2]
    original_lengths = seeds[1::2]
    orignal_ends = [
        start + length for start, length in zip(original_starts, original_lengths)
    ]
    ranges = list(zip(original_starts, orignal_ends))
    unique_ranges = _find_unique_ranges(ranges)
    for start, end in unique_ranges:
        yield from range(start, end)


def _find_unique_ranges(ranges):
    unique_ranges = {ranges[0]}
    for _range in ranges[1:]:
        new_start, new_end = _range
        for existing_start, existing_end in unique_ranges:
            if existing_start <= new_start <= existing_end:
                new_start = existing_end + 1
            if existing_start <= new_end <= existing_end:
                new_end = existing_start - 1
            if new_start >= new_end:
                continue
        unique_ranges.add((new_start, new_end))
    return unique_ranges


def parse_maps(maps: list[str]) -> list[list[Map]]:
    output = []
    current_section = []
    for line in maps:
        if line == "":
            output.append(current_section)
            current_section = []
            continue
        if line.endswith(":"):
            continue
        current_section.append(Map.from_line(line))
    output.append(current_section)
    return output


def _get_lowest_possible_destination(inputs: Iterable[int], maps: list[list[Map]]):
    for map_section in maps:
        print("Moving to next section")
        inputs = lorem_ipsum(inputs, map_section)
    return min(inputs)


def lorem_ipsum(inputs: Iterable[int], map: list[Map]):
    for input in inputs:
        yield map_number(input, map)


def map_number(number: int, maps: list[Map]) -> int:
    for map in maps:
        if number in map.range():
            return map.map(number)
        continue
    return number
