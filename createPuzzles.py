"""
This file will create 100 solveable
n-puzzles in order to calculate the 
Efficiency of using each heuristic.
Puzzles are deemed solveable by 
Using the disorder parameter.
"""

from createPuzzle import createPuzzle
from calculateDisorder import calculateDisorder


# create N(100) puzzles
def createPuzzles(count, n):
    """
    count: 
        - the number of puzzles you want to generate
        - it will always be 100
    n: 
        - the dimension of the puzzle (nxn)
        - n will vary from 3,4,or 5
    """

    # store the puzzles
    puzzles = []

    # continue until 100 puzzles are solveable
    while len(puzzles) != count:
        puzzle = createPuzzle(n)

        disorderParameter = calculateDisorder(puzzle)

        if disorderParameter % 2 == 0:
            #print(disorderParameter)
            puzzles.append(puzzle)

    return puzzles

if __name__ == "__main__":
    puzzles = createPuzzles(100, 3)