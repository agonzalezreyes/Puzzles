"""
Print Binary Tree

Print a binary tree in an m*n 2D string array following these rules:

* The row number m should be equal to the height of the given binary tree.
* The column number n should always be an odd number.
* The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
* Each unused space should contain an empty string "".
* Print the subtrees following the same rules.

Example 1:
Input:
     1
    /
   2
Output:
[["", "1", ""],
 ["2", "", ""]]

Example 2:
Input:
     1
    / \
   2   3
    \
     4
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
 
Example 3:
Input:
      1
     / \
    2   5
   /
  3
 /
4
Output:
[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]

Note: The height of binary tree is in the range of [1, 10].
"""

from typing import List
from math import floor
from util import TreeNode as TreeNode

def printTree(root: TreeNode) -> List[List[str]]:
    m = get_height(root)
    # n defined by m
    n = 2**m - 1 # odd number requirement
    arr = [["" for i in range(n)] for j in range(m)]
    
    middle = (n+1)/2
    node_depth_pos = [(root, 1, middle)]
    for n, d, p in node_depth_pos:
        if n is not None:
            node_depth_pos.append((n.left, d+1, floor(p-middle/(2**d))))
            node_depth_pos.append((n.right, d+1, floor(p+middle/(2**d))))
            arr[d-1][int(p)-1] = str(n.data)
    return arr

def get_height(root: TreeNode):
    if root is None:
        return 0
    return max(get_height(root.left), get_height(root.right)) + 1

from util import Testing as t

tests = t.Testing("Print Binary Tree")

#Input:
#     1
#    /
#   2
output = [["", "1", ""],["2", "", ""]]
tree = TreeNode.TreeNode(1)
tree.left = TreeNode.TreeNode(2)
tests.addTest(output, printTree, tree)

#Input:
#     1
#    / \
#   2   3
#    \
#     4
output = [["", "", "", "1", "", "", ""], ["", "2", "", "", "", "3", ""], ["", "", "4", "", "", "", ""]]
tree = TreeNode.TreeNode(1)
tree.left = TreeNode.TreeNode(2)
tree.left.right = TreeNode.TreeNode(4)
tree.right = TreeNode.TreeNode(3)
tests.addTest(output, printTree, tree)

#Input:
#      1
#     / \
#    2   5
#   /
#  3
# /
#4
output = [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""], ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""], ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""], ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
tree = TreeNode.TreeNode(1)
tree.left = TreeNode.TreeNode(2)
tree.right = TreeNode.TreeNode(5)
tree.left.left = TreeNode.TreeNode(3)
tree.left.left.left = TreeNode.TreeNode(4)
tests.addTest(output, printTree, tree)

tests.run()
