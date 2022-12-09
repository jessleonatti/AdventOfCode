def split_rucksack(rucksack):
    total_size = len(rucksack)
    compartment_size = int(total_size / 2)
    return set(rucksack[:compartment_size]), set(rucksack[compartment_size:])


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


def main():
    with open("input.txt", "r") as f:
        rucksacks = f.readlines()

    total_priority = 0
    for rucksack in rucksacks:
        compartment1, compartment2 = split_rucksack(rucksack.strip())
        overlap = list(compartment1.intersection(compartment2))[0]

        total_priority += priority(overlap)
    print(f"total priority: {total_priority}")


if __name__ == "__main__":
    main()
