"""
This file will calculate the
First heuristic for the puzzle
Implementation. The heuristic
Is the number of misplaced tiles
As seen in the lecture slides.
"""

import numpy as np
from createPuzzle import createPuzzle

def misplacedTiles(puzzle):

    """
    The idea behind the validation is
    That the goal state should have 
    The value "tile" at index "tile-1"
    Since list[0] should be 1 and list[7]
    Should be 8. We don't consider "0" a
    Tile since it's a blank square and
    The placement of the blank could actually
    Be useful even if not in the bottom right.
    """

    heuristicScore = 0 
    flat = puzzle.flatten()

    for tile in flat:

        if (tile != 0) and (flat[tile-1] != tile):
            heuristicScore = heuristicScore + 1
    return heuristicScore


# Driver: 
if __name__ == "__main__":
    puzzle = createPuzzle(3)  
    h = misplacedTiles(puzzle)

    print(puzzle)
    print(h)
