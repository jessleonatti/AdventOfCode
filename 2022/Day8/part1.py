from typing import List


def find_visible_trees(grid: List[List]):
    visible_trees = 0
    size_of_row = len(grid[0])
    number_of_rows = len(grid)
    # Go through all rows
    for row_number, row in enumerate(grid):
        if row_number == 0 or row_number == number_of_rows - 1:
            # All trees in first and last row are visible
            visible_trees += size_of_row
            continue

        # For each row, go through each tree
        for position, tree in enumerate(row):
            # First and last tree in row is visible
            if position == 0 or position == size_of_row - 1:
                visible_trees += 1
                continue

            if is_visible(position, tree, row_number, row, grid, number_of_rows):
                visible_trees += 1

    return visible_trees


def is_visible(
    current_position: int,
    current_tree: int,
    row_number: int,
    row: List[int],
    grid: List[List],
    number_of_rows: int,
):
    # Is it visible from the left?
    if is_visible_from_left(current_position, current_tree, row):
        return True

    # Is it visible from the right?
    if is_visible_from_right(current_position, current_tree, row):
        return True

    # Is it visible from the top?
    if is_visible_from_top(current_position, current_tree, row_number, grid):
        return True

    # Is it visible from the bottom?
    if is_visible_from_bottom(
        current_position, current_tree, row_number, grid, number_of_rows
    ):
        return True
    return False


def is_visible_from_left(current_position: int, current_tree: int, row: List[int]):
    left_of_tree = row[:current_position]
    for tree in left_of_tree:
        if tree >= current_tree:
            return False
    return True


def is_visible_from_right(current_position: int, current_tree: int, row: List[int]):
    right_of_tree = row[current_position + 1 :]
    for tree in right_of_tree[::-1]:
        if tree >= current_tree:
            return False
    return True


def is_visible_from_top(
    current_position: int, current_tree: int, row_number: int, grid: List[List]
):
    row_index = 0
    while row_index < row_number:
        tree = grid[row_index][current_position]
        if tree >= current_tree:
            return False
        row_index += 1
    return True


def is_visible_from_bottom(
    current_position: int,
    current_tree: int,
    row_number: int,
    grid: List[List],
    number_of_rows: int,
):
    row_index = number_of_rows - 1
    while row_index > row_number:
        tree = grid[row_index][current_position]
        if tree >= current_tree:
            return False
        row_index -= 1
    return True


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    grid = []
    for line in lines:
        line = line.strip()
        row = [int(value) for value in line]
        grid.append(row)

    visible_trees = find_visible_trees(grid)
    print(f"visible trees: {visible_trees}")


if __name__ == "__main__":
    main()
