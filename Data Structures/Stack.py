"""
Stack implementation with an array
A Stack technically works as a LIFO Queue

Can also be implemented with: list, collections.deque, queue.LifoQueue

isEmpty() – Returns whether the stack is empty – Time Complexity : O(1)
size() – Returns the size of the stack – Time Complexity : O(1)
peek() – Returns a reference to the top most element of the stack – Time Complexity : O(1)
push(g) – Adds the element ‘g’ at the top of the stack – Time Complexity : O(1)
pop() – Deletes the top most element of the stack – Time Complexity : O(1)
"""

class Stack(object):
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        last = self.peek()
        self.items.remove(last)
        return last
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
        
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
