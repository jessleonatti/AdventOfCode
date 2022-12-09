import typing


def parse_lines(lines):
    for i, line in enumerate(lines):
        if line == "\n":
            break
    return lines[:i], lines[i + 1 :]


def make_stacks(stacks_input):
    number_of_stacks = int(stacks_input[-1].strip().split("   ")[-1])
    stacks_input = stacks_input[:-1]

    # Initialize each stack
    stacks: typing.Dict[int, list] = {}
    for i in range(1, number_of_stacks + 1):
        stacks[i] = []

    # Go through the rows backwars and add each crate to its stack
    for row in reversed(stacks_input):
        row = parse_row(row)
        for i, letter in enumerate(row):
            i += 1
            if letter != "x":
                stacks.get(i).append(letter)

    return stacks


def parse_row(row: str):
    row = row.replace("\n", "")
    row = row.replace("    [", "[x] [")
    row = row.replace("]    ", "] [x]")
    row = row.replace("]     ", "] [x] ")
    row = row.replace("     ", " [x] ")
    row = row.replace("[", "")
    row = row.replace("]", "")
    row = row.split(" ")
    return row


def parse_instruction(instruction: str):
    instruction = instruction.replace("move", "")
    instruction = instruction.replace("from", "")
    instruction = instruction.replace("to", "")
    instruction = instruction.replace("  ", " ")
    instruction = instruction.strip()
    parts = instruction.split(" ")
    return int(parts[0]), int(parts[1]), int(parts[2])


def make_moves(
    stacks: typing.Dict[int, list], quantity: int, source: int, destination: int
):
    stack = stacks[source]
    crates = stack[-quantity:]
    stacks[source] = stack[:-quantity]
    stacks[destination].extend(crates)


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    stacks, instructions = parse_lines(lines)
    stacks = make_stacks(stacks)

    for instruction in instructions:
        quantity, source, destination = parse_instruction(instruction)
        make_moves(stacks, quantity, source, destination)
    print("".join([stack[-1] for stack in stacks.values()]))


if __name__ == "__main__":
    main()
