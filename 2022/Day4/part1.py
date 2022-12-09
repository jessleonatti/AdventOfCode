
def get_elf_sections(pair: str):
    elf1, elf2 = pair.split(",")
    first_elf_section = tuple(elf1.split("-"))
    second_elf_section = tuple(elf2.split("-"))
    return first_elf_section, second_elf_section

def is_fully_contained(first_section, second_section):
    first_section_range = set(range(int(first_section[0]), int(first_section[1])+1))
    second_section_range = set(range(int(second_section[0]), int(second_section[1])+1))
    return first_section_range.issubset(second_section_range) or second_section_range.issubset(first_section_range)

def main():
    with open("input.txt", "r") as f:
        pairs = f.readlines()

    fully_contained = 0
    # pairs = pairs[:4]
    for pair in pairs:
        first_elf_section, second_elf_section = get_elf_sections(pair)

        if is_fully_contained(first_elf_section, second_elf_section):
            fully_contained += 1
    print(f"fully contained: {fully_contained}")

if __name__ == "__main__":
    main()