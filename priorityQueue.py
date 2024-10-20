"""
This file will hold the Priority Queue
Implementation. For efficiency purposes,
We will be using a Heap Queue (heapq) which
Behaves identically to a PQ but much faster.
The priority queue will hold the puzzle state
Nodes where the node in the frontier (unexpanded)
With the lowest cost is the root and will
Be removed first. The built-in class
PritorityQueue could've also been used.
"""

import heapq

class priorityQueue():

    def __init__(self):
        self.queue = []

    def push(self, node): 
        heapq.heappush(self.queue, node)

    def pop(self): 
        heapq.heappop(self.queue)

    # since empty lists are considered "false" this is possible
        # Method to know if the Queue is empty
    def is_empty(self):
        if not self.queue:
            return True
        else:
            return False