"""
This file generates the new puzzle
State given the legal blank tile 
Movement. With the new puzzle matrix
It creates a new node with the 
Required data.
"""

from copy import deepcopy
from node import node
from manhattanDistance import manhattanDistance
from misplacedTiles import misplacedTiles
from swap import swap

def modifyPuzzle(parentNode, newX, newY, action, heuristic):
    
    """
    Given the optimal expansion node from the 
    Priority Queue (parentNode) and the legal
    Operation defined by newX and newY, create
    A new node for possible expansion by 
    Modifying the original puzzle and applying
    The defined action. The heuristic cost
    Is determined by which heuristic is 
    Being used (1,2, or 3).

    parentNode: the optimal node whose puzzle is modified
    newX: the new x value of the blank tile
    newY: the new y value of the blank tile
    action: "Up", "Left", "Down", or "Right"
    heuristic: either 1, 2, or 3 as specified
    """

    # using deepcopy since we want a new memory address and
    # dont want to be linked to the original matrix
    modifiedPuzzle = deepcopy(parentNode.puzzle)

    # now modify the puzzle by swapping tiles
    # the blank tile is swapped with [newX, newY]
    modifiedPuzzle[parentNode.blank[0]][parentNode.blank[1]], modifiedPuzzle[newX][newY] = modifiedPuzzle[newX][newY], modifiedPuzzle[parentNode.blank[0]][parentNode.blank[1]]

    # now calculate the heuristic for the new puzzle
    if heuristic == "1":
        hn = misplacedTiles(modifiedPuzzle)
    elif heuristic == "2":
        hn = manhattanDistance(modifiedPuzzle)
    else:
        hn = swap(modifiedPuzzle)

    # now make the new node with the modified puzzle
    newNode = node(parentNode, modifiedPuzzle, [newX, newY], action, parentNode.gn + 1, hn)

    return newNode