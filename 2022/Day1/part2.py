with open("input.txt", "r") as f:
    lines = f.readlines()

top_three = [0, 0, 0]
current_elf_calories = 0


def check_for_top_three(calories):
    # If calories is more the number 1, move others down and replace
    if calories > top_three[0]:
        top_three[2] = top_three[1]
        top_three[1] = top_three[0]
        top_three[0] = calories
        return

    # If calories is more than number 2, move other down and replace
    if calories > top_three[1]:
        top_three[2] = top_three[1]
        top_three[1] = calories
        return

    # If calories is more than number 3, just replace
    if calories > top_three[2]:
        top_three[2] = calories
        return


for line in lines:
    if line == "\n":
        check_for_top_three(current_elf_calories)
        current_elf_calories = 0
        continue
    current_elf_calories += int(line)

print(f"max: {top_three[0] + top_three[1] + top_three[2]}")
