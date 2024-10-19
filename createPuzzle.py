"""
This file creates the random nxn puzzle board by
Making use of the 'random' library and the 
Function 'shuffle()' to randomly arrange the
Integers of the board. In our boards, the 
Integer '0' will represent the blank tile
While the remaining numbers will represent
Their respective tiles. We implement numpy
Arrays to add extra tools. As visible in 
The function below, the array is resized to
The specific problem; this may not be necessary
But it can always be flattened if needed.
"""

import random
import numpy as np

def createPuzzle(n):

    # Create the arrangement of the tiles
    puzzle = np.array([i for i in range(0,n**2)])
    random.shuffle(puzzle)

    # Arrange it in a board-like form
    puzzle.resize((n,n))

    return puzzle

# Driver
if __name__ == "__main__":
    puzzle = createPuzzle(3)
    print(puzzle)

"""
# Fancy Printout (if needed)
print(f"+---+---+---+")
print(f"| {puzzle[0][0]} | {puzzle[0][1]} | {puzzle[0][2]} |")
print(f"+---+---+---+")
print(f"| {puzzle[1][0]} | {puzzle[1][1]} | {puzzle[1][2]} |")
print(f"+---+---+---+")
print(f"| {puzzle[2][0]} | {puzzle[2][1]} | {puzzle[2][2]} |")
print(f"+---+---+---+")
"""
