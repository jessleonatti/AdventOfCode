# a through z items have priority 1 through 26.
# Their ASCII values start at 97 and end at 122.
# This difference is 96.
lowercase_ascii_difference = 96
# A through Z have items priority 27 through 52.
# Their ASCII values start at 65 and end at 90.
# This difference is 96.
uppercase_ascii_difference = 38


def priority(overlap):
    ascii_value = ord(overlap)
    if ascii_value > 90:
        # Lowercase letter
        return ascii_value - lowercase_ascii_difference
    else:
        # Uppercase letter
        return ascii_value - uppercase_ascii_difference


def make_groups(rucksacks):
    groups = []
    for i in range(0, len(rucksacks), 3):
        groups.append(
            (rucksacks[i].strip(), rucksacks[i + 1].strip(), rucksacks[i + 2].strip())
        )
    return groups


def main():
    with open("input.txt", "r") as f:
        rucksacks = f.readlines()

    groups = make_groups(rucksacks)

    total_priority = 0
    for group in groups:
        overlap = list(set(group[0]) & set(group[1]) & set(group[2]))[0]

        total_priority += priority(overlap)
    print(f"total priority: {total_priority}")


if __name__ == "__main__":
    main()
