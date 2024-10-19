"""
This file calculates the disorder
Parameter of a given puzzle. A
Puzzle is only solveable if the
Value of the parameter is even.
Solveable puzzles are kept
While the rest are discarded.
Another file will implement 
This to continue generating 
Puzzles until 100 are solveable.
"""

from createPuzzle import createPuzzle
import numpy as np

def calculateDisorder(puzzle):
    """
    To calculate the disorder parameter
    We will start from the first index
    And see how many values after it 
    Have a lesser value. This is repeated
    For all tiles but the last. Since the
    Blank is encoded as 0, the program
    Will ignore 0 in the comparisons.
    """

    # To make things easier flatten the puzzle
    flat = puzzle.flatten()
    disorderParameter = 0

    # Calculate disorder
    for i in range(len(flat)):
        for j in range(i+1, len(flat)):
            if (flat[j] != 0) and (flat[i] > flat[j]):
                disorderParameter = disorderParameter + 1

    return disorderParameter

# Driver: testing disorder calculation
puzzle = createPuzzle(3)
disorderParameter = calculateDisorder(puzzle)

print(puzzle)
print(disorderParameter)

"""
Some Testing Results: 
=====================

[[7 8 5]
 [6 0 4]
 [2 3 1]]
25

=====================

[[1 2 3]
 [4 5 6]
 [8 7 0]]
1

=====================

[[0 1 2]
 [3 4 5]
 [6 7 8]]
0

=====================

[[7 3 8]
 [6 5 4]
 [0 1 2]]
22
=====================
"""