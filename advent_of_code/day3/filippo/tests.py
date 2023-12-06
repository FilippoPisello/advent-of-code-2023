from advent_of_code.day3.filippo.solution import extract_number_from_line


def test_if_single_number_in_row_then_it_is_extracted():
    line = "617*......"
    number = extract_number_from_line(line)
    assert number == 617


def test_if_two_numbers_in_row_then_both_are_extracted():
    line = "467..114.."
    numbers = extract_number_from_line(line)
    assert numbers == [467, 114]
