"""
Binary Search Tree
"""
from . import TreeNode

class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root == None:
            self.root = TreeNode(data)
        else:
            curr_node = self.root
            
            while True:
                if data < curr_node.data:
                    if curr_node.left:
                        curr_node = curr_node.left
                    else:
                        curr_node.left = TreeNode(data)
                        break
                elif data > curr_node.data:
                    if curr_node.right:
                        curr_node = curr_node.right
                    else:
                        curr_node.right = TreeNode(data)
                        break
                else:
                    break
    def BFS(self):
        self.root.level = 0
        queue = [self.root]
        out = []
        curr_level = self.root.level
        
        while len(queue) > 0:
            curr_node = queue.pop(0)
            if curr_node.level > curr_level:
                curr_level += 1
                out.append("\n")
            out.append(str(curr_node.data) + " ")
            
            if curr_node.left:
                curr_node.left.level = curr_level + 1
                queue.append(curr_node.left)
            if curr_node.right:
                curr_node.right.level = curr_level + 1
                queue.append(curr_node.right)
        print(out)

    # Inorder: Left, Root, Right
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(str(node.data))
            self.inorder(node.right)

    # Preorder: Root, Left, Right
    def preorder(self, node):
        if node is not None:
            print(str(node.data))
            self.preorder(node.left)
            self.preorder(node.right)

    # Postorder: Left, Right, Root
    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(str(node.data))


