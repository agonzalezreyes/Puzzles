import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from DataStructures.Graph import Graph
import heapq

# get shortest path from v.previous
def shortest(v, path):
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

"""
Steps:
1. set initial node's distance to 0 and infinity to all other
2. mark all nodes unvisited (done in Vertex())
3. set initial node as current, and create a list of the unvisited nodes called the unvisited list consisiting of all the nodes using tuple pair (distance, v)
4. for the current node, consider all of its unvisited neighbors and calculate their tentative distances; compare the new calculated tentative distance to current assigned value and set the shortest distance.
5. after considering all neighbors of the current node, mark the current node as visited and remove it from unvisted list. For each new node visit, we rebuild the heap: pop all items, refill the unvisited_queue, and then heapify it.
6. a visited node will never be checked again.
7. if there is no unvisited node, the algorithm finished. Else, go back to step 4.
8. shortest() to get all predecessors starting from the target node
"""
def dijkstra(a_graph, start):
    # starting node gets distance = 0
    start.set_distance(0)
    
    # priority queue
    unvisited_q = [(v.get_distance(), v) for v in a_graph]
    heapq.heapify(unvisited_q)
    
    while len(unvisited_q):
        # get vertex with smallest distance
        uv = heapq.heappop(unvisited_q)
        curr = uv[1]
        curr.set_visited()
        
        for next in curr.adjacent:
            # skip if visited already
            if next.visited: # step 6
                continue
               
            # new tentative distance
            new_distance = curr.get_distance() + curr.get_weight(next)
            
            if new_distance < next.get_distance(): # assign if shorter
                next.set_distance(new_distance)
                next.set_previous(curr)
                print("updated : current = " + str(curr.get_id()) + " next = " + str(next.get_id()) + " new_distance = " + str(next.get_distance()))
            else:
                print("NOT updated : current = " + str(curr.get_id()) + " next = " + str(next.get_id()) + " new_distance = " + str(next.get_distance()))
        # rebuild heap
        while len(unvisited_q): # pop every item
            heapq.heappop(unvisited_q)
        # put add vertices not visited into queue
        unvisited_q = [(v.get_distance(), v) for v in a_graph if not v.visited]
        heapq.heapify(unvisited_q)

g = Graph()
g.add_vertex('a')
g.add_vertex('b')
g.add_vertex('c')
g.add_vertex('d')
g.add_vertex('e')
g.add_vertex('f')

g.add_edge('a', 'b', 7)
g.add_edge('a', 'c', 9)
g.add_edge('a', 'f', 14)
g.add_edge('b', 'c', 10)
g.add_edge('b', 'd', 15)
g.add_edge('c', 'd', 11)
g.add_edge('c', 'f', 2)
g.add_edge('d', 'e', 6)
g.add_edge('e', 'f', 9)

print("Graph content:")
for v in g:
    for w in v.get_connections():
        v_id = v.get_id()
        w_id = w.get_id()
        print("(" + str(v_id) + ", "+ str(w_id) + ", " + str(v.get_weight(w)) + ")")

dijkstra(g, g.get_vertex('a'))

target = g.get_vertex('e')
path = [target.get_id()]
shortest(target, path)
print("shortest path: " + str(path[::-1]))
