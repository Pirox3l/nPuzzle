"""
This file finds the location of 
The blank tile in a puzzle.
"""

import numpy as np

def findBlank(puzzle):

    coords = np.argwhere(puzzle == 0)
    x = coords[0][0]
    y = coords[0][1]

    return [x,y]
