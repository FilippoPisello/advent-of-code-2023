from dataclasses import dataclass


def main_part_one(problem_input: list[str]) -> int:
    return None


def main_part_two(problem_input: list[str]):
    return None


@dataclass
class Map:
    start: int
    end: int
    delta: int

    @property
    def destination_start(self) -> int:
        return self.start + self.delta

    @property
    def destination_end(self) -> int:
        return self.end + self.delta


def combine_mappings(first: Map, second: Map) -> list[Map]:
    if first.destination_start <= second.start <= second.end <= first.destination_end:
        return [
            Map(
                start=first.start, end=second.start - 1 - first.delta, delta=first.delta
            ),
            Map(start=second.start, end=second.end, delta=second.delta),
            Map(start=second.end - first.delta + 1, end=first.end, delta=first.delta),
        ]
    if first.destination_end <= second.start:
        return [first, second]
