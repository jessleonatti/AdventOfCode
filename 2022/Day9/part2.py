from typing import Tuple, Set, List


def move_knots(
    knots: List[Tuple], direction: str, steps: int, visited: List[Set[Tuple]]
):
    for _ in range(steps):
        knots[0] = move_knot(knots[0], direction)
        for i in range(len(knots) - 1):
            knots[i + 1] = move_t(knots[i], knots[i + 1])
            visited[i + 1].add(knots[i + 1])
    return knots, visited


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


def move_t(h: Tuple, t: Tuple) -> Tuple:
    if h == t:
        return t

    x_difference = abs(h[0] - t[0])
    y_difference = abs(h[1] - t[1])

    # H and T are in the same column
    if h[0] == t[0]:
        if y_difference != 1:
            direction_to_move = find_direction_to_move_row(h, t)
            return move_knot(t, direction_to_move)

    # H and T are in the same row
    if h[1] == t[1]:
        if x_difference != 1:
            direction_to_move = find_direction_to_move_column(h, t)
            return move_knot(t, direction_to_move)

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
        # print(f"{t_list}")
    elif h[0] > t[0] and h[1] < t[1]:
        # Move down 1 and righ 1
        t_list[0] += 1
        t_list[1] -= 1
    return tuple(t_list)


def find_direction_to_move_row(h: Tuple, t: Tuple):
    if h[1] < t[1]:
        # Move down
        return "D"
    if h[1] > t[1]:
        # Move up
        return "U"


def find_direction_to_move_column(h: Tuple, t: Tuple):
    if h[0] < t[0]:
        # Move left
        return "L"
    if h[0] > t[0]:
        # Move right
        return "R"


def diagonally_touching(x_difference, y_difference) -> bool:
    return x_difference == 1 and y_difference == 1


def main():
    with open("input.txt", "r") as f:
        moves = f.readlines()

    knots: List[Tuple] = [(0, 0) for _ in range(10)]
    visited: List[Set[Tuple]] = []
    for knot in knots:
        visited.append({knot})

    for move in moves:
        move = move.strip()
        direction, steps = move.split(" ")
        knots, visited = move_knots(knots, direction, int(steps), visited)

    print(f"tail visited: {len(visited[9])}")


if __name__ == "__main__":
    main()
