with open("input.txt", "r") as f:
    lines = f.readlines()

calibration_values_sum = 0

for line in lines:
    # Find first digit
    for item in line:
        if item.isnumeric():
            first_digit = item
            break

    # Find second digit
    for index in range(len(line)-1, -1, -1):
        item = line[index]
        if item.isnumeric():
            second_digit = item
            break
    calibration_value = f"{first_digit}{second_digit}"
    print(f"calibration value: {calibration_value}")
    calibration_values_sum += int(calibration_value)

print(f"calibration values sum: {calibration_values_sum}")

