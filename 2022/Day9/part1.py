from typing import Tuple, Set


def move_knots(h: Tuple, t: Tuple, direction: str, steps: int, t_visited: Set[Tuple]):
    for _ in range(steps):
        h = move_knot(h, direction)
        t = move_t(h, t, direction)
        t_visited.add(t)
    return h, t, t_visited


def move_knot(knot: Tuple, direction: str) -> Tuple:
    knot_list = list(knot)
    if direction == "R":
        knot_list[0] += 1
    elif direction == "L":
        knot_list[0] -= 1
    elif direction == "U":
        knot_list[1] += 1
    elif direction == "D":
        knot_list[1] -= 1
    return tuple(knot_list)


def move_t(h: Tuple, t: Tuple, direction: str) -> Tuple:
    # H and T are overlapping
    if h == t:
        return t

    x_difference = abs(h[0] - t[0])
    y_difference = abs(h[1] - t[1])

    # H and T are in the same column
    if h[0] == t[0]:
        if y_difference != 1:
            return move_knot(t, direction)

    # H and T are in the same row
    if h[1] == t[1]:
        if x_difference != 1:
            return move_knot(t, direction)

    # Touching diagonally
    if diagonally_touching(x_difference, y_difference):
        return t

    # Move T diagonally
    t_list = list(t)
    if h[0] > t[0] and h[1] > t[1]:
        # Move up 1 and right 1
        t_list[0] += 1
        t_list[1] += 1
    elif h[0] < t[0] and h[1] > t[1]:
        # Move up 1 and left 1
        t_list[0] -= 1
        t_list[1] += 1
    elif h[0] < t[0] and h[1] < t[1]:
        # Move down 1 and left 1
        t_list[0] -= 1
        t_list[1] -= 1
    elif h[0] > t[0] and h[1] < t[1]:
        # Move down 1 and righ 1
        t_list[0] += 1
        t_list[1] -= 1
    return tuple(t_list)


def diagonally_touching(x_difference, y_difference) -> bool:
    return x_difference == 1 and y_difference == 1


def main():
    with open("input.txt", "r") as f:
        moves = f.readlines()

    # H and T start at 0,0
    h: Tuple = (0, 0)
    t: Tuple = (0, 0)
    t_visited: Set[Tuple] = set()
    t_visited.add(t)

    for move in moves:
        move = move.strip()
        direction, steps = move.split(" ")
        h, t, t_visited = move_knots(h, t, direction, int(steps), t_visited)

    print(f"tail visited: {len(t_visited)}")


if __name__ == "__main__":
    main()
