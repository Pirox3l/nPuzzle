"""
This file generates child states
Given the current puzzle state. 
Using legalAction, it determines
If the generated state is legal
And should be considered as a 
Child node. A child is also only
Added if it has not yet been 
Previously explored in A*.
"""

# function to calculate blank

from legalAction import legalAction

def generateChilden(currentNode, exploredSet, n):

    """
    In general, there are 4 possible children
    From a given puzzle state. Although, this 
    Only occurs when the blank is in the center.
    When the blank is in a corner there are 2
    Legal moves, and the other 4 occassions
    Have 3 possible moves (edge not corner). 
    In such events, the blank can either move
    Up, down, left, or right. 
    """

    # For the same index i, there is only movement
    # In one direction since a tile can only move
    # Up, down, left, or left, not diagonally
    rowMovements = [-1,0,1,0]
    columnMovements = [0,-1,0,1]

    blankX = currentNode.blank[0]
    blankY = currentNode.blank[1]

    newChildren = []

    for i in range(4):
        # determine possible new position
        newX = blankX + rowMovements[i]
        newY = blankY + columnMovements[i]

        # check if position is legal
        legal = legalAction(newX, newY, n)
        
        # INCOMPLETE HERE:
        # make a new node given the new coordinates
        # check if this new node has already been explored
        # if not, add it to newChildren
    
    return
