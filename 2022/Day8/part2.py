from typing import List


def find_most_scenic_tree(grid: List[List]):
    size_of_row = len(grid[0])
    number_of_rows = len(grid)
    max_scenic_score = 0
    # Go through all rows
    for row_number, row in enumerate(grid):
        if row_number == 0 or row_number == number_of_rows - 1:
            # All trees have one 0 score, so total is 0. Can't be the max.
            continue

        # For each row, go through each tree
        for position, tree in enumerate(row):
            # First and last tree in row have one 0 score, so total is 0. Can't be the max.
            if position == 0 or position == size_of_row - 1:
                continue

            scenic_score = get_scenic_score(
                position, tree, row_number, row, grid, number_of_rows, size_of_row
            )

            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

    return max_scenic_score


def get_scenic_score(
    current_position: int,
    current_tree: int,
    row_number: int,
    row: List[int],
    grid: List[List],
    number_of_rows: int,
    size_of_rows: int,
):
    return (
        left_scenic_score(current_position, current_tree, row)
        * right_scenic_score(current_position, current_tree, row, size_of_rows)
        * top_scenic_score(current_position, current_tree, row_number, grid)
        * bottom_scenic_score(
            current_position, current_tree, row_number, grid, number_of_rows
        )
    )


def left_scenic_score(current_position: int, current_tree: int, row: List[int]):
    # Start to the left of the current tree
    position = current_position - 1
    score = 0
    # Loop until the beginning of the row
    while position >= 0:
        tree = row[position]
        score += 1
        if tree >= current_tree:
            # This tree is taller than the current tree,
            # so no more trees can be seen
            break
        position -= 1
    return score


def right_scenic_score(
    current_position: int, current_tree: int, row: List[int], size_of_rows: int
):
    # Start to the right of the current tree
    position = current_position + 1
    score = 0
    # Loop until the end of the row
    while position < size_of_rows:
        tree = row[position]
        score += 1
        if tree >= current_tree:
            # This tree is taller than the current tree,
            # so no more trees can be seen
            break
        position += 1
    return score


def top_scenic_score(
    current_position: int, current_tree: int, row_number: int, grid: List[List]
):
    # Start row above current row
    row_index = row_number - 1
    score = 0
    # Loop until the first row
    while row_index >= 0:
        tree = grid[row_index][current_position]
        score += 1
        if tree >= current_tree:
            # This tree is taller than the current tree,
            # so no more trees can be seen
            break
        row_index -= 1
    return score


def bottom_scenic_score(
    current_position: int,
    current_tree: int,
    row_number: int,
    grid: List[List],
    number_of_rows: int,
):
    # Start row below current row
    row_index = row_number + 1
    score = 0
    # Loop until the last row
    while row_index < number_of_rows:
        tree = grid[row_index][current_position]
        score += 1
        if tree >= current_tree:
            # This tree is taller than the current tree,
            # so no more trees can be seen
            break
        row_index += 1
    return score


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    grid = []
    for line in lines:
        line = line.strip()
        row = [int(value) for value in line]
        grid.append(row)

    most_scenic_tree = find_most_scenic_tree(grid)
    print(f"most scenic tree: {most_scenic_tree}")


if __name__ == "__main__":
    main()
