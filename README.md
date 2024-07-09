# DragonFjord A-Puzzle-A-Day Solver

This repository contains a solver for the DragonFjord A-Puzzle-A-Day puzzle. The solver reads the current date, modifies the grid accordingly, and finds all possible solutions for placing the given shapes on the grid.

## How to Run

1. Clone the repository.
2. Navigate to the repository directory.
3. Run the solver with the following command:
   ```bash
   python3 solver.py
   ```

The solver will generate and print all possible solutions for today's puzzle.

## Example Output

```
Solution 1:
U U r r r S  
  U r S S S  
U U r S B B B
t   f f B B B
t t d f f f L
t d d L L L L
t d d   

...

Execution time: X.XXXX seconds
Total shapes placement attempts: XXXX
```

## Code Overview


### Functions

1. **`make_todays_grid()`**: Creates the grid for the current day with the day and month removed.
2. **`can_place(grid, block, top_left_x, top_left_y)`**: Checks if a block can be placed on the grid at the specified position.
3. **`place(grid, block, top_left_x, top_left_y)`**: Places a block on the grid and returns the new grid.
4. **`print_grid(grid)`**: Prints the grid to the console.
5. **`rotate(block)`**: Rotates a block 90 degrees clockwise.
6. **`mirror(block)`**: Mirrors a block horizontally.
7. **`get_orientations(block)`**: Gets all unique orientations of a block.
8. **`recursion(grid, shapes, blocks_placed=0, solutions=[], attempts_counter=None)`**: Recursively tries to place all shapes on the grid.

### Execution Flow

1. The grid is created for today's date.
2. The shapes are defined.
3. The initial grid is printed.
4. The recursive function is called to find all solutions.
5. The solutions are printed along with the execution time and the total number of shape placement attempts.

### Dependencies

- `time`: For measuring execution time.
- `functools.lru_cache`: For caching function results.
- `datetime.date`: For getting today's date.

