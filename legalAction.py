"""
This file will be used to 
Determine if a possible move
Is considered legal in the 
State space given the dimensions
Of the puzzle. The provided
Coordinates are based of the 
Earlier location of the 
Blank tile.
"""

def legalAction(x, y, n):
    """
    To be a legal action, the coordinate must be:
        1. Greater than or equal to 0
        2. Less than the n dimension of the puzzle
        3. For both x and y
    """
    legal = False

    if (x >= 0 and x < n) and (y >= 0 and y < n):
        legal = True
    
    return legal