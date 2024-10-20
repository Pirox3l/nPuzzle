"""
This file will calculate the 
Third heuristic score for the
Number of swaps required to 
Solve the puzzle. Since this
Heurisitc is a solution to 
A relaxed problem, then it
Is an admissible heuristic
For the original problem.
"""

from createPuzzle import createPuzzle

def swap(puzzle):
    flat = puzzle.flatten()
    
    # count swaps
    swaps = 0
    
    # size of puzzle (number of values to check)
    dimension = len(flat)

    for i in range(dimension): 

        """
        This loop continues until position i has 
        the correct tile value. In the process, 
        the incorrect tile at position i will be
        moved to its correct location by subtracting
        its value by 1. Until the correct tile is 
        swapped to position i, this will continue.
        It is important to note that the maximum number 
        of swaps required is 8 but is often less since
        swapping two tiles in one move can place them
        both in the correct position.  
        """

        while flat[i] != 0 and flat[i] != i + 1:
            # the correct location for the tile at square i
            correct_pos = flat[i] - 1
            
            # swap the value at i to its correct location
            flat[i], flat[correct_pos] = flat[correct_pos], flat[i]
            
            # add swaps
            swaps = swaps + 1 
   
    return swaps

# Driver:
if __name__ == "__main__":
    puzzle = createPuzzle(3)
    swaps = swap(puzzle)
    print(puzzle)
    print(swaps)

"""
A good test case:
[[0 3 4]
 [6 7 8]
 [1 5 2]]
8
"""