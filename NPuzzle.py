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
from node import node
from priorityQueue import priorityQueue
from findBlank import findBlank
from manhattanDistance import manhattanDistance
from misplacedTiles import misplacedTiles
from swap import swap

def NPuzzle(n, heuristic):
    """
    n = 3: 8-puzzle
    n = 4: 15-puzzle
    n = 5: 24-puzzle
    """

    # loop for heuristic afterwards

    # create 1 puzzles
    puzzles = createPuzzles(1, n)

    #print((puzzles[0]))

    # find blank tile
    blank = findBlank(puzzles[0])

    # calculate an example heuristic for this puzzle
    hn = heuristic(puzzles[0])

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
        check = heuristic(optimalNode.puzzle)

        if check == 0:
            return optimalNode

        else:
            # generate children
            newFrontiers = generateChilden(optimalNode, exploredSet, n, heuristic)

            # add these to the frontier
            for childNode in newFrontiers:
                frontier.push(childNode)

    return


if __name__ == "__main__":
    num_test = 100
    avg_cost = 0
    i = 0
    # solves num_test instances of the tile puzzle
    for heuristic in [misplacedTiles, manhattanDistance, swap]:
        while i < num_test:
            on = NPuzzle(3, manhattanDistance)
            avg_cost += on.fn
            
            on.print_node()
            while on.parent is not None:
                on.print_node()
                on = on.parent
            
        
            i+=1
        avg_cost = avg_cost/100
    print(f"Average cost:{avg_cost}")