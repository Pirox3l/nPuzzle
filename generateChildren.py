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
from modifyPuzzle import modifyPuzzle

def generateChilden(currentNode, exploredSet, n, heuristic):

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

    # when the "currentNode" is removed from the 
    # priority queue and deemed optimal, it becomes
    # explored and is added to the explored set

    # For the same index i, there is only movement
    # In one direction since a tile can only move
    # Up, down, left, or left, not diagonally
    rowMovements = [-1,0,1,0]
    columnMovements = [0,-1,0,1]

    actions = {
        1: "Left",
        2: "Down",
        3: "Right",
        4: "Up" 
    }

    blankX = currentNode.blank[0]
    blankY = currentNode.blank[1]

    newChildren = []

    for i in range(4):
        # determine possible new position
        newX = blankX + rowMovements[i]
        newY = blankY + columnMovements[i]

        # check if position is legal
        legal = legalAction(newX, newY, n)
        
        if legal:
            # make a new node given the new coordinates
            childNode = modifyPuzzle(currentNode, newX, newY, actions[i+1], heuristic)
            
            # check if this new node has already been explored: if not, add it to newChildren
            # we don't want to add a node to the frontier if already explored
            if ((childNode.puzzle).flatten()) not in exploredSet:
                newChildren.append((childNode.puzzle).flatten()) 

    # the nodes in newChildren will be added to frontier pq
    return newChildren
