import math

## Graph, each key in dict points to a dict that contains all items and the distances between them
graph = {"start": {"1": 2, "2": 1}, 
         "1": {"start": 2, "2": 3, "3": 1, "4": 4},
         "2": {"start": 1, "1": 3, "4": 5},
         "3": {"1": 1, "4": 1},
         "4": {"1": 4, "2": 5, "3": 1, "end": 1},
         "end": {"4": 1}}

visited = []

## Djikstra checks all possible paths to return the shortest
# Check first node for all connecting nodes, record shortest path
# check all neighbours for next shortest path
# iterate through all nodes until a single shortest path is found
def djikstra(graph, start_node):
    #Unvisited
    #shorted
    #while unvisited  (checks all unvisted nodes while they still exist)
    pass

## returns all paths that reach end by not going to an alreadt visited node
def show_all_possible():
    pass

djikstra()