import sys

class Vertex(object):
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxsize # default
        self.visited = False
        self.previous = None
    
    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight
    
    def get_connections(self):
        return self.adjacent.keys()
    
    def get_id(self):
        return self.id
    
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]
    
    def set_distance(self, dist):
        self.distance = dist
    
    def get_distance(self):
        return self.distance
    
    def set_previous(self, prev):
        self.previous = prev
    
    def set_visited(self):
        self.visited = True
    
    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([n.id for n in self.adjacent])

    def __lt__(self, other): # <
        return self.get_distance() < other.get_distance()

    def __le__(self, other): # <=
        return self.get_distance() <= other.get_distance()

class Graph(object):
    def __init__(self):
        self.V_dict = {}
        self.num_vertices = 0
    
    def __iter__(self):
        return iter(self.V_dict.values())
    
    def add_vertex(self, node):
        self.num_vertices += 1
        new_vertex = Vertex(node)
        self.V_dict[node] = new_vertex
        return new_vertex
    
    def get_vertex(self, node):
        if node in self.V_dict:
            return self.V_dict[node]
        else:
            return None
        
    def add_edge(self, former, to, cost=0):
        if former not in self.V_dict:
            self.add_vertex(former)
        if to not in self.V_dict:
            self.add_vertex(to)
        
        self.V_dict[former].add_neighbor(self.V_dict[to], cost)
        self.V_dict[to].add_neighbor(self.V_dict[former], cost)
        
    def get_vertices(self):
        return self.V_dict.keys()
    
    def set_previous(self, current):
        self.previous = current
    
    def get_previous(self):
        return self.previous

