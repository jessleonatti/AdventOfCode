from typing import Dict, List, Set, Tuple


with open("input.txt", "r") as f:
    lines = f.readlines()


def get_scratchcard_wins_per_card(card_number: int, winning_numbers: List[str], numbers_you_have: List[str]) -> int:
    matches = 0
    wins: Set[int] = set()
    for number in winning_numbers:
        if number in numbers_you_have:
            matches += 1
            wins.add(card_number+matches)
    return wins

def parse_line(line: str) -> Tuple[List[str], List[str]]:
    line = line.replace("\n", "")
    parts = line.split(" | ")
    more_parts = parts[0].split(":")
    winning_numbers = more_parts[1].strip()
    winning_numbers = winning_numbers.replace("  ", " ")
    numbers_you_have = parts[1].strip()
    numbers_you_have = numbers_you_have.replace("  ", " ")
    winning_numbers = winning_numbers.split(" ")
    numbers_you_have = numbers_you_have.split(" ")
    return winning_numbers, numbers_you_have

scratchcard_wins: Dict[int, int] = {}

for index, line in enumerate(lines):
    card_number = index + 1
    if int(card_number) not in scratchcard_wins.keys():
        scratchcard_wins[card_number] = 1
    else:
        scratchcard_wins[card_number] += 1
    winning_numbers, numbers_you_have = parse_line(line)
    wins = get_scratchcard_wins_per_card(card_number, winning_numbers, numbers_you_have)
    for win in wins:
        if win not in scratchcard_wins.keys():
            scratchcard_wins[win] = 0
        scratchcard_wins[win] += 1*scratchcard_wins.get(card_number)

print(f"Final scratchcratch card wins: {sum(scratchcard_wins.values())}")