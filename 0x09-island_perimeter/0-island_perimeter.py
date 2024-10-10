#!/usr/bin/python3
"""Island perimeter computing module.
"""


def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes."""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
                    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Land found
                # Assume each land cell adds 4 sides
                perimeter += 4

                # Check if the land cell has a neighboring land cell above it
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2  # Subtract 2 sides for the shared border

                # Check if the land cell has a neighboring land cell to the left
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2  # Subtract 2 sides for the shared border
    return perimeter
