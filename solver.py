"""Script for solving DragonFjord A-Puzzle-A-Day for today's date"""
import time
from functools import lru_cache
from datetime import date


L_SHAPE = [
    ['L', 'X'],
    ['L', 'X'],
    ['L', 'X'],
    ['L', 'L']
]
U_SHAPE = [
    ['U', 'X', 'U'],
    ['U', 'U', 'U']
]

S_SHAPE = [
    ['X', 'S', 'S'],
    ['X', 'S', 'X'],
    ['S', 'S', 'X']
]

D_SHAPE = [
    ['X', 'd'],
    ['d', 'd'],
    ['d', 'd']
]
R_SHAPE = [
    ['r', 'r', 'r'],
    ['r', 'X', 'X'],
    ['r', 'X', 'X']
]
B_SHAPE = [
    ['B', 'B'],
    ['B', 'B'],
    ['B', 'B']
]
F_SHAPE = [
    ['X', 'f'],
    ['f', 'f'],
    ['f', 'X'],
    ['f', 'X']
]
T_SHAPE = [
    ['t', 'X'],
    ['t', 't'],
    ['t', 'X'],
    ['t', 'X']
]


def make_todays_grid() -> list[list[str]]:
    """Create a grid with the current day and month removed."""
    todays_date = date.today()
    day = todays_date.day
    month = todays_date.month
    grid = [["1", "2", "3", "4", "5", "6", " "],
            ["7", "8", "9", "10", "11", "12", " "],
            ["1", "2", "3", "4", "5", "6", "7"],
            ["8", "9", "10", "11", "12", "13", "14"],
            ["15", "16", "17", "18", "19", "20", "21"],
            ["22", "23", "24", "25", "26", "27", "28"],
            ["29", "30", "31", " ", " ", " ", " "]]
    for i in range(2):
        for j in range(len(grid[i])):
            if grid[i][j] == str(month):
                grid[i][j] = " "

    for i in range(2, len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == str(day):
                grid[i][j] = " "
    return grid


def can_place(grid, block, top_left_x, top_left_y) -> bool:
    """Check if a block can be placed on the grid at position (x, y)."""
    block_height = len(block)
    block_width = len(block[0])
    grid_height = len(grid)
    grid_width = len(grid[0])

    if top_left_y + block_height > grid_height or top_left_x + block_width > grid_width:
        return False

    for i, row in enumerate(block):
        for j, cell in enumerate(row):
            if cell != 'X':
                y = top_left_y + i
                x = top_left_x + j

                if not grid[y][x].isnumeric():
                    return False
    return True


def place(grid, block, top_left_x, top_left_y) -> list:
    """Place a block on the grid at position (x, y) and return the new grid."""
    new_grid = [row[:] for row in grid]
    for i, row in enumerate(block):
        for j, cell in enumerate(row):
            if cell != 'X':
                y = top_left_y + i
                x = top_left_x + j
                new_grid[y][x] = cell
    return new_grid


def print_grid(grid) -> None:
    """Print the grid."""
    for row in grid:
        print(" ".join(row))
    print(" ")


def rotate(block) -> list[list[str]]:
    """Rotate a block 90 degrees clockwise."""
    return [list(row) for row in zip(*block[::-1])]


def mirror(block) -> list:
    """Mirror a block horizontally."""
    return [row[::-1] for row in block]


@lru_cache(maxsize=None)
def get_orientations(block) -> list[list[list]]:
    """Get all unique orientations of a block."""
    orientations = set()
    current = block
    for _ in range(4):
        orientations.add(tuple(map(tuple, current)))
        current = rotate(current)
    current = mirror(block)
    for _ in range(4):
        orientations.add(tuple(map(tuple, current)))
        current = rotate(current)
    return [list(map(list, orientation)) for orientation in orientations]


def recursion(grid, shapes, blocks_placed=0, solutions=None, attempts_counter=None) -> None:
    """Recursively try to place all shapes on the grid."""
    if solutions is None:
        solutions = [0]
    if attempts_counter is None:
        attempts_counter = [0]
    if blocks_placed == len(shapes):
        solutions[0] += 1
        print(f"Solution {solutions[0]}:")
        print_grid(grid)
        return

    current_shape = shapes[blocks_placed]
    orientations = get_orientations(tuple(map(tuple, current_shape)))

    for orientation in orientations:
        for y, row in enumerate(grid):
            for x in range(len(row)):
                if can_place(grid, orientation, x, y):
                    new_grid = place(grid, orientation, x, y)
                    attempts_counter[0] += 1
                    recursion(new_grid, shapes, blocks_placed +
                              1, solutions, attempts_counter)

    return


if __name__ == "__main__":
    date_grid = make_todays_grid()

    all_shapes = [L_SHAPE, U_SHAPE, S_SHAPE, D_SHAPE,
                  R_SHAPE, B_SHAPE, F_SHAPE, T_SHAPE]

    print("Starting grid:")
    print_grid(date_grid)

    start_time = time.time()

    solutions_found = [0]
    attempts = [0]

    recursion(date_grid, all_shapes, solutions=solutions_found,
              attempts_counter=attempts)

    end_time = time.time()

    if not solutions_found[0]:
        print("Failed to place all shapes on the grid")

    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.4f} seconds")
    print(f"Total shapes placement attempts: {attempts[0]}")
