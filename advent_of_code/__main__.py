import argparse
from importlib import import_module

import pytest

from advent_of_code import MODULE_DIR
from advent_of_code.read_input import read_txt_input


def main():
    args = _parse_args()
    if args.test:
        run_tests(args.day, args.user)
    else:
        run_solution(args.day, args.user)


def _parse_args():
    parser = argparse.ArgumentParser(
        description="Run your solution or tests for a day of the Advent of Code challenge."
    )
    parser.add_argument("day", type=int, help="The number of the day to run.")
    parser.add_argument("user", type=str, help="The user to run for.")
    parser.add_argument(
        "--test",
        "--tests",
        action="store_true",
        help="Run tests instead of the solution.",
        default=False,
    )
    return parser.parse_args()


def run_solution(day: int, user: str):
    problem_input = read_txt_input(day, user)
    user_dir = ".".join(["advent_of_code", f"day{day}", user])
    solution = import_module(user_dir + ".solution")
    result = solution.main(problem_input)
    print(result)


def run_tests(day: int, user: str):
    pytest.main([MODULE_DIR / f"day{day}" / user / "tests.py"])


if __name__ == "__main__":
    main()
