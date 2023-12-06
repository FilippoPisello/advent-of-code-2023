def main(problem_input: list[str]):
    total = 0
    for line in problem_input:
        calibration_values = []
        for _, char in enumerate(line):
            if char.isdigit():
                calibration_values.append(char)
        x = int(calibration_values[0] + calibration_values[
            len(calibration_values)-1])
        total = total + x

    return total