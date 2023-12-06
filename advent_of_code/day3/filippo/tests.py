from advent_of_code.day3.filippo.solution import extract_numbers_from_line


def test_if_single_number_in_row_then_it_is_extracted():
    line = "617*......"
    number = extract_numbers_from_line(line)
    assert number == [617]


def test_if_two_numbers_in_row_then_both_are_extracted():
    line = "467..114.."
    numbers = extract_numbers_from_line(line)
    assert numbers == [467, 114]


def test_if_line_has_no_number_then_nothing_is_returned():
    line = "...*......"
    numbers = extract_numbers_from_line(line)
    assert numbers == []


def test_number_starting_and_ending_position_in_line_is_stored():
    line = "617*......"
    numbers = extract_numbers_from_line(line)
    assert numbers[0].starting_index == 0
    assert numbers[0].ending_index == 2
