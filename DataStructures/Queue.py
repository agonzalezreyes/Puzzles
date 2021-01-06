"""
Queue

An ordered list in which insertions are done at one end (rear) and deletions are done at other end (front) -- First In First Out (FIFO) or Last In Last Out (LILO).

Example uses:
CPU scheduling; Disk Scheduling

Max. size of the queue must be defined prior to init.

Time Complexities:
enqueue(): O(1)
dequeue(): O(1)
isEmpty(): O(1)
getSize(): O(1)
"""

class Queue(object):
    def __init__(self, limit=10):
        self.queue = []
        self.front = None
        self.rear = None
        self.limit = limit
        self.size = 0

    def isEmpty(self):
        return self.size <= 0
        
    def isFull(self):
        return self.size >= self.limit

    def enqueue(self, data):
        if self.isFull():
            return -1
        else:
            self.queue.append(data)
        
        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size
        
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        
        item = self.queue.pop(0)
        self.size -= 1
        
        if self.size == 0:
            self.front = self.rear = 0
        else:
            self.rear = self.size - 1
        
        return item

    def getSize(self):
        return self.size

    def __str__(self):
        if len(self.queue) == 0:
            return "Empty Queue!"
        return ' '.join([str(s) for s in self.queue])
