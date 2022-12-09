import sys


def reset_current_marker(last_index, current_marker, current_marker_characters):
    current_marker = current_marker[last_index + 1 :]
    current_marker_characters.clear()
    for i, character in enumerate(current_marker):
        current_marker_characters[character] = i
    return current_marker, current_marker_characters


def find_end_of_marker(marker_size):
    with open("input.txt", "r") as f:
        lines = f.read()

    current_marker_characters = {}
    current_marker = ""
    start_index = 0
    for character in lines:
        if character in current_marker_characters.keys():
            # Character is already in marker. Remove all characters up
            # to the original instance of the character and add this
            # one to the end.
            last_index = current_marker_characters[character]

            current_marker, current_marker_characters = reset_current_marker(
                last_index, current_marker, current_marker_characters
            )

        # Add character to current marker
        current_marker += character
        current_marker_characters[character] = len(current_marker) - 1
        start_index += 1

        # Check for final marker
        if len(current_marker) == marker_size:
            break

    print(f"current marker: {current_marker}")
    print(f"index: {start_index}")


def main():
    args = sys.argv[1:]
    if args[0] == "part1":
        find_end_of_marker(4)
    elif args[0] == "part2":
        find_end_of_marker(14)
    else:
        print(f"Invalid args {args}.")


if __name__ == "__main__":
    main()
