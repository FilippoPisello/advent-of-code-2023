# Advent of Code 2023

Hosting the solutions for Advent of Code 2023 for some members of Picnic Technologies France.

## How to use

### Folder structure

The setup should be the following:

- A folder in `advent_of_code/` named `day<number>`, unless already existing.
- A folder in `advent_of_code/day<number>/` named `<your-name>`.
- Four files:
  - `advent_of_code/day<number>/<your-name>/__init__.py`
  - `advent_of_code/day<number>/<your-name>/solution.py`
  - `advent_of_code/day<number>/<your-name>/input.txt`
  - [Optional] `advent_of_code/day<number>/<your-name>/tests.py`

### File structure

File `advent_of_code/day<number>/<your-name>/solution.py` should contain either:

- A function called `main`: if you opt for a setup where you use one function for both parts.
- At least one function between `main_part_one` and `main_part_two`: if you want to have distinct functions for the two parts, so that you can run each independently.

Anyway, all of these functions must respect the following:

- Takes a single argument `problem_input`, which is a `list[str]` where each element corresponds to a line of the original problem input.
- Return whatever the result of your solution is.

### Running your solution

By setting up as described, you can run your solutions as described below. The script will take care of feeding the input for the right day to your solution and print its result.

In case you opted for a single `main` function, use:

```bash
python -m advent_of_code <day-number> <your_name>
```

Otherwise, to run a part specific main, use:

```bash
python -m advent_of_code <day-number> <your_name> --part <1 or 2>
```

### Running tests

You can also run your tests by using the keyword `--test`:

```bash
python -m advent_of_code <day-number> <your_name> --test
```
