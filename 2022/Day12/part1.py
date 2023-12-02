import math
from typing import List, Set, Tuple
from queue import PriorityQueue


class Node:
    def __init__(self, row: int, column: int, value: str):
        self.row = row
        self.column = column
        self.value = value
        self.distance = 0


def get_neighbors(current: Tuple, grid: List[List[Tuple]], x_length: int, y_length: int):
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    result = []
    for direction in directions:
        neighbor_column = current[2] + direction[1]
        neighbor_row = current[1] + direction[0]
        if 0 <= neighbor_column < x_length and 0 <= neighbor_row < y_length:
            neighbor = grid[neighbor_row][neighbor_column]
            result.append(neighbor)
    return result


def visit_neighbors(
    current: Tuple,
    grid: List[List[Tuple]],
    to_visit: List[Tuple],
    visited: Set[Tuple],
    x_length: int,
    y_length: int,
):
    neighbors: List[Tuple] = get_neighbors(current, grid, x_length, y_length)
    for neighbor in neighbors:
        if (neighbor[1], neighbor[2]) in visited:
            continue

        difference = ord(neighbor[3]) - ord(current[3])
        if (
            current[3] == "S"
            or neighbor[3] == "S"
            or current[3] == "E"
            or neighbor[3] == "E"
        ):
            difference = 1

        if difference > 1 or difference < 0:
            # Step is more than 1. Can't visit it.
            continue
        # Can't go to E not from z
        if neighbor[3] == "E" and current[3] != "z":
            continue

        # Increase neighbors distance by 1
        new_distance = current[0] + 1
        updated_neighbor = list(neighbor)
        updated_neighbor[0] = new_distance
        neighbor = tuple(updated_neighbor)
        if neighbor[3] == "E" and current[3] == "z":
            # Found the destination
            to_visit.clear()
            return neighbor, visited

        to_visit.append(neighbor)
    return None, visited


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    # Make the grid
    grid: List[List[str]] = []
    start_position = None
    for i, line in enumerate(lines):
        row = []
        line = line.strip()
        for j, value in enumerate(line):
            if value == "S":
                start_position = i, j
            node = (0, i, j, value)
            row.append(node)
        grid.append(row)

    x_length = len(grid[0])
    y_length = len(grid)
    to_visit = PriorityQueue()
    to_visit.put(grid[start_position[0]][start_position[1]])
    visited = set()
    destination = None
    while to_visit or destination == None:
        current = to_visit.get()
        # print(f"{current[2]}")
        visited.add((current[1], current[2]))
        destination, visited = visit_neighbors(
            current, grid, to_visit, visited, x_length, y_length
        )
    print(f"destination: {destination}")


if __name__ == "__main__":
    main()
