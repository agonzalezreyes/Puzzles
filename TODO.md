## Algorithms
- [x] Big-O analysis
- [x] Sorting
- Hashing
- Handling large datasets

## Sorting
- [x] Know at least one nlog(n) sorting algorithm (Quicksort and merge sort)
- [x] Common sorting functions
### Questions:
1. What kind of input data are the efficient?
2. When are they not efficient? 
3. Efficiency in terms of runtime and space used?
4. In which  exceptional cases are insertion-sort and radix-sort better than Quicksort / MergeSort / HeapSort?

## Data Structures
- Know about most famous classes of NP-complete problems (traveling salesman and knapsack problems —  be able to recognize them)
- Trees, basic tree construction
- [x] Hash tables 
- [x] Stacks 
- [x] Arrays (Dynamic Array)
- [x] Linked Lists: Singly, Doubly, and Circular
- [x] Queues: Standard, Priority, Circular, Deque

## HashTables and Maps
**HashTable Applications:**
- write function to determine if a string contains repeated chars
- given a string of any length, find the most-used char
- determine if two strings are anagrams

**Time Complexity:**
Search - Average O(1), Amortized Worst O(n)
Insert - Average O(1), Amortized Worst O(n)
Delete - Average O(1), Amortized Worst O(n)

**Space Complexity:**
Average O(n)
Worst O(n)

Hash tables are (slightly) simpler to implement than search trees and have better average-case performance.

- **Notes:**
* Be able to implement one using only arrays 
* Know the O() characteristics of the standards library implementation for HashTables and Maps

## Trees
- Tree traversal algorithms: BFS and DFS, and difference between inorder, postorder, and preorder:
1. **Depth First Traversals:**
    (a) Inorder (Left, Root, Right)
    (b) Preorder (Root, Left, Right)
    (c) Postorder (Left, Right, Root)
2. **Breadth First or Level Order Traversal**

**Be familiar with:**
- [ ] **binary trees:** each node has at most two children, which are referred to as the left child and the right child.
- [ ] **n-ary trees:** an n-ary tree is a rooted tree in which each node has no more than n children; a binary tree is a special form of a N-ary tree; a trie is one of the most frequently used N-ary trees.
- [x] **trie-trees:** Every node of trie consists of multiple branches. Each branch represents a possible character of keys. We need to mark the last node of every key as leaf node. A trie node field value will be used to distinguish the node as leaf node (there are other uses of the value field)

**Be familiar with implementation of:**
- [ ] **binary search tree (BST):** worst-case for search/delete/insert is O(n) when the tree is skewed. 
- [ ] **balanced binary trees:** 
- [ ] **splay tree:** a self-balancing BST; brings the recently accessed item to the root of the tree, makes the recently searched item accessible in `O(1)` if needed to be accessed again. Example usage: in a program where we have millions or billions of keys and only few of them are accessed frequently. 
    Average time `O(logn)` where n is the number of entrie3s in the tree. Any operation can take `O(n)` in the worst-case. 
    Search operation: Splay tree does standard BST search, in addition to search, it also splays (moves a node to the root). When a search is successful, the node is splayed and becomes the new root. 
    
- [ ] **red/black tree:** a self-balancing BST; binary search tree with one extra bit of storage per node (color: RED or BLACK), ensure that no path is more than twice as long as any other, so tree is approx. balanced; node fields: color, key, left, right, and parent. If a node is red, both its children are black. 

- [ ] **AVL tree:** a self-balancing BST; binary search tree that is height balances - for each node the heights of the left and right subtrees differ by at most 1. 

**Red/black-tree vs AVL-tree:**
- AVL-trees are always at the optimal balanced point, but can slow down inserts and deletes because tey are more rigidly balanced than red/black trees. But has the dastest look times.
- Red/black trees are also self-balancing but can become slightly imbalanced to improve insert and delete times, with a small potential hit to search times. 
- Both have worst case time of `O(logn)`

- **Notes:**
* Know basic tree construction
* Tree manipulation algorithms

## Min/Max Heaps
### Heap
Data is stored in an array so that each key is guaranteed to be larger than its two children keys. No node in a heap-ordered tree has a key larger than the key at the root. 
- **Operations:**
* insert - `O(log(n))`
* extract - extracting max or min value `O(log(n))`
* heapify - n batched inserts `O(n)`
* delete - `O(log(n))`

### Min Heap
- Root node has the minimun value
- Value for each node is equal or greater than the value of its parent node
- A complete binary tree

### Max heap
- The root node has the maximun value 
- The value of each node is equal or less than the value of its parent node
- A complete binary tree

- **How are Min/Max Heaps represented?** A min/max heap is typically represented as an array.
    `Arr[0]` Returns the root node.
    `Arr[(i-1)/2]` Returns the parent node.
    `Arr[(2*i)+1]` Returns the left child node.
    `Arr[(2*i)+2]` Returns the right child node.
- **Time Complexity for Min/Max heaps:**
* `O(1)` getting max or min element 
* `O(logn)` removing max or min element
* `O(logn)` inserting an element, because we insert the value at the end of the tree and traverse up to remove violated property of min/max heap

- **Notes:**
* Understand their application and O() characteristics.
* Know when it makes sense to use one

## Graphs
- Graph algorithms for distance, search, connectivity, cycle-detection
- 3 basic ways to represent a graph in memory (objects and pointers, matrix, and adjacent list) — for each, know representation and its pros and cons 
- Basic graph traversal algorithms, BFS and DFS, their computational complexity, tradeoffs, and how to implement them.
1. **Depth-First Search (DFS)**
* explore aggressively, only retreat when necessary
* computes a topological ordering of a directed acyclic graph and strongly connected components of directed graphs
* linear runtime
* dijkstra
2. **Breadth-First Search (BFS)**
* explore nodes in layers
* runtime - linear time
* application - shortest paths
