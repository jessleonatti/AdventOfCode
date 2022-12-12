def calculate_signal_stength(cycle_count: int, x: int, sum_of_signal_strength: int):
    if cycle_count == 20 or (cycle_count - 20) % 40 == 0:
        signal_strength = cycle_count * x
        sum_of_signal_strength += signal_strength
    return sum_of_signal_strength


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    x = 1
    cycle_count = 1
    sum_of_signal_strength = 0
    for line in lines:
        line = line.strip()
        parts = line.split(" ")
        if len(parts) > 1:
            instruction, value = parts[0], parts[1]
        else:
            instruction = parts[0]

        sum_of_signal_strength = calculate_signal_stength(
            cycle_count, x, sum_of_signal_strength
        )

        # Increase cycle by 1
        if instruction == "noop":
            cycle_count += 1

        # Increase cycle by 1, check for specific cycle, then increase by 1 again
        # and modify value of X
        if instruction == "addx":
            cycle_count += 1

            sum_of_signal_strength = calculate_signal_stength(
                cycle_count, x, sum_of_signal_strength
            )

            cycle_count += 1
            x += int(value)

    print(f"Sum of signal strength: {sum_of_signal_strength}")


if __name__ == "__main__":
    main()
