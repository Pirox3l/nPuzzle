"""
This file will be the entire
Execution of the N-Puzzle 
Problem. It makes use of 
All previously defined 
Helper-Functions. This
File is a test for 1 puzzle.
"""

from createPuzzles import createPuzzles
from generateChildren import generateChilden
from modifyPuzzle import modifyPuzzle
from node import node
from priorityQueue import priorityQueue
from findBlank import findBlank
from manhattanDistance import manhattanDistance

def NPuzzle(n):
    """
    n = 3: 8-puzzle
    n = 4: 15-puzzle
    n = 5: 24-puzzle
    """

    # loop for heuristic afterwards

    # create 1 puzzles
    puzzles = createPuzzles(1, n)

    print((puzzles[0]))

    # find blank tile
    blank = findBlank(puzzles[0])

    # calculate an example heuristic for this puzzle
    hn = manhattanDistance(puzzles[0])

    # create the exploredSet
    exploredSet = set()

    # create the frontier pq
    frontier = priorityQueue()

    # create the intitial puzzle node
    initialState = node(None, puzzles[0], blank, None, 0, hn)

    initialState.print_node()

    # add initialState to pq
    frontier.push(initialState)

    # if not goal state continue until pq is empty even though this is excessive
    while not frontier.is_empty():
            
        # remove from frontier
        optimalNode = frontier.pop()

        # add to exploredSet
        exploredSet.add(tuple((optimalNode.puzzle).flatten()))

        # check if goalState 
        check = manhattanDistance(optimalNode.puzzle)

        if check == 0:
            return optimalNode

        else:
            # generate children
            newFrontiers = generateChilden(optimalNode, exploredSet, n, "2")

            # add these to the frontier
            for childNode in newFrontiers:
                frontier.push(childNode)

    return


if __name__ == "__main__":
    on = NPuzzle(3)

    while on is not None:
        on.print_node()
        on = on.parent