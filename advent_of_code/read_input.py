from pathlib import Path

ROOT = Path(__file__).parent.resolve()


def read_txt_input(day_number: int) -> list[str]:
    """Reads the input file for the given day number.

    Each line is an element of the returned list.
    """
    input_file = ROOT / f"day{day_number}" / "input.txt"
    content = input_file.read_text()
    return content.splitlines()
