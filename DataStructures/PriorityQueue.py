"""
Priority Queue using binary heap.

Time Complexities:
peek() runs in O(1)
insert() and pop() run in O(log n)
"""

class PriorityQueue(object):
    def __init__(self):
        # each node is tuple (value, priority, in_counter)
        self.nodes = [None] # first item is not used
        self.in_counter = 0

    def __str__(self):
        if len(self.nodes) == 1:
            return "Empty Priority Queue!"
        items = self.get_array()
        return ' '.join([str(s) for s in items])

    def get_array(self):
        if len(self.nodes) == 1:
            return []
        return [str(s) for s in self.nodes if s != None]

    # higher priority comparison, if equal then insertion counter value
    def _is_higher_node(self, node1, node2):
        return node1[1] > node2[1] or (node1[1] == node2[1] and node1[2] < node2[2])
    
    def _heapify(self, nn_index):
        while 1 < nn_index:
            new_node = self.nodes[nn_index]
            parent_index = nn_index // 2
            parent_node = self.nodes[parent_index]
            if self._is_higher_node(parent_node, new_node):
                break
            # swap
            temp = parent_node
            self.nodes[parent_index] = new_node
            self.nodes[nn_index] = temp
            # continue
            nn_index = parent_index
        
    def insert(self, value, priority):
        nn_index = len(self.nodes) # new node index
        self.in_counter += 1
        new_node = (value, priority, self.in_counter)
        self.nodes.append(new_node)
        self._heapify(nn_index) # order the node
    
    def peek(self):
        if len(self.nodes) == 1: # if we only have None item
            return None
        # return value of Node at index 1 (after None)
        return self.nodes[1][0]
    
    def pop(self):
        if len(self.nodes) == 1:
            return None
        
        result = self.nodes[1][0] # value of node is [0]
        
        empty_index = 1
        while (empty_index * 2) + 1 < len(self.nodes):
            left_child_i = empty_index * 2
            right_child_i = empty_index * 2 + 1
            
            left_child_n = self.nodes[left_child_i]
            right_child_n = self.nodes[right_child_i]
            
            if len(self.nodes) <= right_child_i or self._is_higher_node(left_child_n, right_child_n):
                self.nodes[empty_index] = left_child_n
                empty_index = left_child_i
            else:
                self.nodes[empty_index] = right_child_n
                empty_index = right_child_i
        
        last_node_i = len(self.nodes) - 1
        self.nodes[empty_index] = self.nodes[last_node_i]
        self._heapify(empty_index)
        
        self.nodes.pop()
        
        return result
