
def get_elf_sections(pair: str):
    elf1, elf2 = pair.split(",")
    first_elf_section = tuple(elf1.split("-"))
    second_elf_section = tuple(elf2.split("-"))
    return first_elf_section, second_elf_section

def overlapped(first_section, second_section):
    first_section_range = set(range(int(first_section[0]), int(first_section[1])+1))
    second_section_range = set(range(int(second_section[0]), int(second_section[1])+1))
    first_intersect_second = first_section_range.intersection(second_section_range)
    second_intersect_first = second_section_range.intersection(first_section_range)
    return len(first_intersect_second) > 0 or len(second_intersect_first) > 0

def main():
    with open("input.txt", "r") as f:
        pairs = f.readlines()

    overlap = 0
    for pair in pairs:
        first_elf_section, second_elf_section = get_elf_sections(pair)

        if overlapped(first_elf_section, second_elf_section):
            overlap += 1
    print(f"overlap: {overlap}")

if __name__ == "__main__":
    main()