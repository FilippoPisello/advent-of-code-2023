import pytest

from day1.filippo.solution import run


def test_if_string_has_two_digits_then_take_first_and_last():
    content = ["1abc2"]
    result = run(content)
    assert result == "12"


def test_if_string_has_more_than_two_digits_then_take_first_and_last():
    content = ["a1b2c3d4e5f"]
    result = run(content)
    assert result == "15"


def test_if_more_than_one_string_results_are_added_together():
    content = ["1abc2", "a1b2c3d4e5f"]
    result = run(content)
    assert result == "27"


def test_if_only_one_digit_then_take_it_twice():
    content = ["treb7uchet"]
    result = run(content)
    assert result == "77"


def test_if_no_digits_then_return_zero():
    content = ["david"]
    result = run(content)
    assert result == "0"


def test_run_first_example():
    content = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    result = run(content)
    assert result == "142"


@pytest.mark.parametrize(
    ("string", "expected"),
    (
        ("two1nine", "29"),
        ("abcone2threexyz", "13"),
    ),
)
def test_if_spelled_out_digits_are_in_order_then_parse(string, expected):
    content = [string]
    result = run(content)
    assert result == expected


def test_if_spelled_out_digits_are_not_sorted_then_parse_them_by_order():
    content = ["eightwothree"]
    result = run(content)
    assert result == "83"


def test_run_second_example():
    content = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    result = run(content)
    assert result == "281"


def test_single_match_spelled_out_digit():
    content = ["eight"]
    result = run(content)
    assert result == "88"


def test_number_appears_twice_at_different_positions():
    content = ["eight12eight4eight"]
    result = run(content)
    assert result == "88"
