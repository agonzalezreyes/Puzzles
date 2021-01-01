"""
Tree Node Class
"""
import queue as q
from copy import deepcopy as deepcopy
import sys

class TreeNode(object):
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.level = None
    
    def __str__(self):
        return str(self.data)
    
    def visit(self):
        sys.stdout.write(self.data)
    
    def get_num_nodes(self):
        total = 0
        if self.left:
            total += self.left.get_num_nodes()
        if self.right:
            total += self.right.get_num_nodes()
        return total + 1
    
    @classmethod
    def create_tree(cls, depth):
        tree = TreeNode('X')
        cls.create_tree_helper(tree, depth, 1)
        return tree
    
    @classmethod
    def create_tree_helper(cls, node, depth, cur):
        if cur == depth:
            return
        node.left = TreeNode("X")
        node.right = TreeNode("XX")
        cls.create_tree_helper(node.left, depth, cur+1)
        cls.create_tree_helper(node.right, depth, cur+1)

    def get_height(self):
        return TreeNode.get_height_helper(self)
    
    @classmethod
    def get_height_helper(self, node):
        if not node:
            return 0
        else:
            return max(TreeNode.get_height_helper(node.left), TreeNode.get_height_helper(node.right)) + 1
    
    def fill_tree(self, height):
        TreeNode.fill_tree_helper(self, height)
    
    @classmethod
    def fill_tree_helper(self, node, height):
        if height <= 1:
            return
        if node:
            if not node.left:
                node.left = TreeNode(' ')
            if not node.right:
                node.right = TreeNode(' ')
            TreeNode.fill_tree_helper(node.left, height-1)
            TreeNode.fill_tree_helper(node.right, height-1)
            
    def pprint(self):
        all_layers = self.get_height()
        tree = deepcopy(self)
        tree.fill_tree(all_layers)
        # BFS queue
        queue = q.Queue()
        queue.put(tree) # add root
        layer = 1
        # BFS
        while not queue.empty():
        
            copy = q.Queue()
            while not queue.empty():
                copy.put(queue.get())
            
            first_in_layer = True
            edges_str = ""
            extra_spaces = False
            
            while not copy.empty():
            
                node = copy.get()
                
                # spacing
                delta_layers = all_layers - layer
                front_spaces = pow(2, delta_layers + 1) - 2
                middle_spaces = pow(2, delta_layers + 2) - 2
                dash_count = pow(2, delta_layers) - 2
                    
                if dash_count < 0:
                    dash_count = 0
                    
                middle_spaces = middle_spaces - (2*dash_count) + 1
                front_spaces = front_spaces - dash_count
                padding = 2
                front_spaces += padding
                if first_in_layer:
                    edges_str += " " * padding
                
                # edges layer
                edge_symbol = "/" if node.left and node.left.data else " "
                if first_in_layer:
                    edges_str += " " * int(pow(2, delta_layers) - 1) + edge_symbol
                else:
                    edges_str += " " * int(pow(2, delta_layers + 1) + 1) + edge_symbol
                
                edge_symbol = "\\" if node.right and node.right.data else " "
                edges_str += " " * int(pow(2, delta_layers + 1) - 3) + edge_symbol

                # handle dashes
                dash_left = " " if node.left and node.left.data is None else "_"
                dash_right = " " if node.right and node.right.data is None else "_"

                # extra spacing for when node lengths do not match or are even
                extra = 0
                if extra_spaces:
                    extra = 1
                    extra_spaces = False
                
                # account for data len
                data_len = len(str(node.data))
                if data_len > 1:
                    if data_len % 2 == 1: # odd
                        if dash_count > 0:
                            dash_count -= ((data_len-1)/2)
                        else:
                            middle_spaces -= ((data_len - 1)/2)
                            front_spaces -= ((data_len - 1)/2)
                            if data_len != 1:
                                extra_spaces = True
                    else: # even
                        if dash_count > 0:
                            dash_count -= (data_len/2)-1
                            extra_spaces = True
                        else:
                            middle_spaces -= (data_len - 1)
                            front_spaces -= (data_len - 1)
                # print node with or without dashes
                if first_in_layer:
                    print((" " * int(front_spaces)) + (dash_left * int(dash_count)) + str(node.data) + (dash_right * int(dash_count)), end='')
                    first_in_layer = False
                else:
                    print((" " * int(middle_spaces-extra)) + (dash_left * int(dash_count)) + str(node.data) + (dash_right * int(dash_count)), end='')
                        
                if node.left is not None:
                    queue.put(node.left)
                if node.right is not None:
                    queue.put(node.right)

            if not queue.empty():
                print("\n" + edges_str)
                    
            layer += 1
        print()
                        
