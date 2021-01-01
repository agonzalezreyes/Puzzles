"""
Deque: A Double Ended Queue - insertion and deletion at both ends of the queue.

"""

class Deque(object):
    def __init__(self, size=10):
        self.queue = []
        self.max_size = size
        
    def __str__(self):
        if self.isEmpty():
            return "Empty Deque!"
        return ' '.join([str(s) for s in self.queue])
    
    def isEmpty(self):
        return len(self.queue) <= 0
    
    def isFull(self):
        return len(self.queue) >= self.max_size
        
    def insertFront(self, value):
        if self.isFull():
            return -1 # failure
        self.queue.insert(0, value) # insert at index 0
        return 1 # success
    
    def insertRear(self, value):
        if self.isFull():
            return -1 # failure
        self.queue.append(value) # insert at last index ~ append
        return 1 # success

    def removeFront(self):
        if self.isEmpty():
            return None
        return self.queue.pop(0) # return elem at index 0

    def removeRear(self):
        if self.isEmpty():
            return None
        return self.queue.pop() # return last elem inserted
