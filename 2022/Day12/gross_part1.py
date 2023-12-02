import math
from typing import List, Set, Tuple
# from operator import attrgetter


class Node:
    def __init__(self, coordinates: Tuple, value: str, x_length: int, y_length: int, grid):
        self.value = value
        self.distance = math.inf
        self.visited = False
        self.neighbors = self.neighbors(coordinates, x_length, y_length, grid)

    def neighbors(self, coordinates: Tuple, x_length: int, y_length: int, grid):
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        result = []
        for direction in directions:
            neighbor_coordinates = [coordinates[0] + direction[0], coordinates[1] + direction[1]]
            # print(f"neighbor: {neighbor}")
            if 0 <= neighbor_coordinates[0] < x_length and -y_length < neighbor_coordinates[1] <= 0:
                neighbor = grid[neighbor_coordinates[0]][neighbor_coordinates[1]]
                result.append(neighbor)
        print(f"Neighbors of {self.value}: {result}\n")
        return result


def visit_neighbors(node: Node):
    print(f"Current node {node.value} with coordinates: {node.coordinates}")
    for neighbor in node.neighbors:
        print(f"Neighbor {neighbor.value} with coordinates {neighbor.coordinates}")
        if neighbor.visited:
            print(f"Neighbor visited, skipping...")
            continue

        # The distance to this neighbor is the current node's
        # distance plus the difference in the ASCII values
        if node.value == "S" or node.value == "E" or neighbor.value == "S" or neighbor.value == "E":
            difference = 1
        else:
            difference = ord(neighbor.value) - ord(node.value)
        if difference < 0:
            difference = math.inf
        new_distance = node.distance + difference
        print(f"New distance: {new_distance}")
        neighbor.visited = True

        if new_distance < neighbor.distance:
            neighbor.distance = new_distance

        if new_distance < min_neighbor.distance:
            min_neighbor = neighbor

    print(f"Min neighbor: {min_neighbor.coordinates}\n\n")
    return min_neighbor

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    
    # Make the grid
    grid: List[List[Node]] = []
    for i, line in enumerate(lines):
        row = []
        line = line.strip()
        for j, value in enumerate(line):
            row.append(value)
        grid.append(row)

    # Make nodes
    unvisited: Set[Node] = set()
    y_length = len(grid)
    x_length = len(grid[0])
    start_node = None
    for i, row in enumerate(grid):
        for j, item in enumerate(row):
            node = Node((j, -i), item, x_length, y_length, grid)
            if (i, j) == (0, 0):
                start_node = node
            unvisited.add(node)


    # start = (0, 0)
    # start_node = grid[0][0]
    start_node.distance = 0
    start_node.visited = True
    # start_node.value = "`"
    current_node = start_node

    has_unvisited = len(unvisited) != 0
    while has_unvisited:
        unvisited.remove(current_node)
        current_node = visit_neighbors(current_node, grid)
        has_unvisited = len(unvisited) != 0
        




if __name__ == "__main__":
    main()
