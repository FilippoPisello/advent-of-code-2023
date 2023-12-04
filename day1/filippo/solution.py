from pathlib import Path


def main():
    text = read_txt_input(1)
    output = run(text)
    print(output)


mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def run(text: list[str]) -> str:
    total = 0
    for line in text:
        matches = {}

        for spelled_out_digit, digit in mapping.items():
            newstring = line.replace(spelled_out_digit, "!" * len(spelled_out_digit))
            for index, char in enumerate(newstring):
                if char == "!":
                    matches[index] = digit

        for index, char in enumerate(line):
            if char.isdigit():
                matches[index] = int(char)

        if not matches:
            number = 0
        else:
            matches = sorted(matches.items(), key=lambda x: x[0])
            number = int(f"{matches[0][1]}{matches[-1][1]}")
        total += number

    return str(total)


ROOT = Path(__file__).parent.parent.resolve()


def read_txt_input(day_number: int) -> list[str]:
    """Reads the input file for the given day number.

    Each line is an element of the returned list.
    """
    input_file = ROOT / "input.txt"
    content = input_file.read_text()
    return content.splitlines()


if __name__ == "__main__":
    main()
