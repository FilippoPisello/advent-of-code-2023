def main_part_one(problem_input: list[str]):
    total = 0
    for line in problem_input:
        winning, owned = parse_line(line)
        winning_and_owned = winning & owned
        if not winning_and_owned:
            continue
        score = 2 ** (len(winning_and_owned) - 1)
        total += score
    return total


def main_part_two(problem_input: list[str]):
    return


def parse_line(line: str) -> tuple[set[int], set[int]]:
    _, line_without_card = line.split(":")
    winning, owned = line_without_card.split("|")
    winning = set(int(n) for n in winning.split())
    owned = set(int(n) for n in owned.split())
    return winning, owned
