# Advent of Code 2023
Hosting the solutions for Advent of Code 2023 for some members of Picnic Technologies France.


## How to use
You should have made the following:
- A folder in `advent_of_code/` named `day<number>`, unless already existing.
- A folder in `advent_of_code/day<number>/` named `<your-name>`.
- Three files:
  - `advent_of_code/day<number>/<your-name>/__init__.py`
  - `advent_of_code/day<number>/<your-name>/solution.py`
  - [Optional] `advent_of_code/day<number>/<your-name>/tests.py`

If the above is respected, you can **run your solution using the command**:
```bash
python -m advent_of_code <day-number> <your_name>
```
For example, *John* can run its solution for day 1 using:
```bash
python -m advent_of_code 1 john
```
You can also run your tests by simply adding `--test` to the above command:
```bash
python -m advent_of_code <day-number> <your_name> --test
```
