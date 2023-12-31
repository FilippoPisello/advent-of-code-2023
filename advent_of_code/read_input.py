from pathlib import Path

ROOT = Path(__file__).parent.resolve()


def read_txt_input(day_number: int, user: str) -> list[str]:
    """Reads the input file for the given day number.

    Each line is an element of the returned list.
    """
    input_file = ROOT / f"day{day_number}/{user}/input.txt"
    content = input_file.read_text()

    ## uncomment for days 1 to 4 and later
    return content.splitlines()

    ## uncomment for day 5
    # return content.split("\n\n")
