# individual tree node class
class Node(object):
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

"""

Depth First Traversals

"""

"""
Inorder traversal usage: for Binary Search Trees, it gives nodes in non-decreasing order. To get nodes of BTS in non-decreasing order, a variation of inorder traversal where inorder traversal is reversed.
"""
def inorder(root, _callback):
    if root:
        inorder(root.left, _callback)
        _callback(root.value)
        inorder(root.right, _callback)

"""
Postorder traversal usage: to delete a tree, get postfix expression of an expression tree
"""
def postorder(root, _callback):
    if root:
        postorder(root.left, _callback)
        postorder(root.right, _callback)
        _callback(root.value)

"""
Preorder traversal usage: used to create a copy of the tree; get prefix expression of an expression tree.
"""
def preorder(root, _callback):
    if root:
        _callback(root.value)
        preorder(root.left, _callback)
        preorder(root.right, _callback)

"""

Breadth First or Level Order Traversal
aka Level Order Binary Tree Traversal
"""


"""
Level Order Traversal Method 1:

Time Complexity: O(n^2) in worse case
O(n) for a skewed tree where n is the number of nodes

Call Stack Space Complexity: O(n) for worst case.
O(n) space for a skewed tree
O(logn) space for a balanced tree
"""
# level order traversal of tree
def level_order_1(root, _callback):
    h = get_height(root)
    for i in range(1, h+1):
        given_level_call(root, i, _callback)

def given_level_call(root, level, _callback):
    if root is None:
        return
    
    if level == 1:
        _callback(root.value)
    elif level > 1:
        given_level_call(root.left, level-1, _callback)
        given_level_call(root.right, level-1, _callback)

# calculate the heigth of a tree--the number of nodes along the longest path starting from root node all the way to the leaf node that it is the farthest
def get_height(node):
    if node is None:
        return 0
    left_height = get_height(node.left)
    right_height = get_height(node.right)
    
    if left_height > right_height:
        return left_height + 1
    else:
        return right_height + 1


"""
Level Order Traversal Method 2: Using Queue

For each node, the first node is visited and then it's child nodes are put in a FIFO Queue

Time Complexity: O(n) where n is number of nodes in the binary tree
Space Complexity: O(n) where n is number of nodes in the binary tree
"""
from Queue import Queue

def level_order_2(root, _callback):
    if root is None:
        return
    
    q = Queue()
    q.enqueue(root)
    
    while q.getSize() > 0:
        node = q.dequeue()
        _callback(node.value)
        
        if node.left is not None:
            q.enqueue(node.left)
        if node.right is not None:
            q.enqueue(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

def simple_print(value):
    print(value, end=" ")

# 1 2 4 5 3
print("preorder:")
preorder(root, simple_print)
print()

# 4 2 5 1 3
print("inorder:")
inorder(root, simple_print)
print()

# 4 5 2 3 1
print("postorder:")
postorder(root, simple_print)
print()
print()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# 1 2 3 4 5
print("level_order_1: ")
level_order_1(root, simple_print)
print()
# 1 2 3 4 5
print("level_order_2: ")
level_order_2(root, simple_print)
print()
