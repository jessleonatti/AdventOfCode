with open("input.txt", "r") as f:
    lines = f.readlines()

max = 0
current_elf_calories = 0
for line in lines:
    if line == "\n":
        if current_elf_calories > max:
            max = current_elf_calories
        current_elf_calories = 0
        continue
    current_elf_calories += int(line)

print(f"max: {max}")
