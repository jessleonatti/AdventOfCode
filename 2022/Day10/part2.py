from typing import List


def draw_pixels(cycle_count: int, x: int, screen: List[List[str]]):
    pixel_column = cycle_count % 40
    if pixel_column in (x - 1, x, x + 1):
        pixel_row = cycle_count // 40
        screen[pixel_row][pixel_column] = "#"
    return screen


def print_screen(screen: List[List[str]]):
    for row in screen:
        print(f"{''.join(row)}\n")


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    x = 1
    cycle_count = 0

    screen = []
    for _ in range(6):
        row = []
        for _ in range(40):
            row.append(".")
        screen.append(row)

    for line in lines:
        line = line.strip()
        parts = line.split(" ")
        if len(parts) > 1:
            instruction, value = parts[0], parts[1]
        else:
            instruction = parts[0]

        # Draw pixels
        screen = draw_pixels(cycle_count, x, screen)

        # Increase cycle by 1
        if instruction == "noop":
            cycle_count += 1

        # Increase cycle by 1, check for specific cycle, then increase by 1 again
        # and modify value of X
        if instruction == "addx":
            cycle_count += 1

            # Draw pixels
            screen = draw_pixels(cycle_count, x, screen)

            cycle_count += 1
            x += int(value)

    print_screen(screen)


if __name__ == "__main__":
    main()
