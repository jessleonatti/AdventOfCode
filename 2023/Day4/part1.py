from typing import List


with open("input.txt", "r") as f:
    lines = f.readlines()


def calculate_points(winning_numbers: List[str], numbers_you_have: List[str]) -> int:
    matches = -1
    for number in winning_numbers:
        if number in numbers_you_have:
            matches += 1
            print(f"{number} in numbers you have. Matches: {matches}")
    return pow(2, matches) if matches != -1 else 0

points = 0
for line in lines:
    line = line.replace("\n", "")
    parts = line.split(" | ")
    more_parts = parts[0].split(":")
    winning_numbers = more_parts[1].strip()
    winning_numbers = winning_numbers.replace("  ", " ")
    numbers_you_have = parts[1].strip()
    numbers_you_have = numbers_you_have.replace("  ", " ")
    winning_numbers = winning_numbers.split(" ")
    numbers_you_have = numbers_you_have.split(" ")
    line_points = calculate_points(winning_numbers, numbers_you_have)
    print(f"Final line points: {line_points}")
    points += line_points

print(f"Points: {points}")