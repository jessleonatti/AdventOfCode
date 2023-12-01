with open("input.txt", "r") as f:
    lines = f.readlines()

calibration_values_sum = 0

number_words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def check_for_number_word(word: str) -> str:
    for number_word, number in number_words.items():
        if number_word in word:
            return number
    return ""

for line in lines:
    # Find first digit
    running_word = ""
    for item in line:
        if item.isnumeric():
            first_digit = item
            break
        running_word += item
        number = check_for_number_word(running_word)
        print(f"number: {number}")
        if number != "":
            first_digit = number
            break


    # Find second digit
    running_word = ""
    for index in range(len(line)-1, -1, -1):
        item = line[index]
        if item.isnumeric():
            second_digit = item
            break
        running_word = f"{item}{running_word}"
        number = check_for_number_word(running_word)
        print(f"number: {number}")
        if number != "":
            second_digit = number
            break
    calibration_value = f"{first_digit}{second_digit}"
    print(f"calibration value: {calibration_value}")
    calibration_values_sum += int(calibration_value)

print(f"calibration values sum: {calibration_values_sum}")

