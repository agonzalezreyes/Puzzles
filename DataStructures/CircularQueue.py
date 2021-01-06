"""
Circular Queue, aka Ring Buffer

Operations FIFO (First in First Out) and last position connected back to the first position.

self.front - index of front item on queue
self.rear - index of last item on queue

enqueue(value) - insert item at the rear position
dequeue() - remove front element of the queue

Time complexity: enQueue() and deQueue() are O(1)

Applications:
- memory management
- traffic system
- CPU scheduling
"""

class CircularQueue(object):
    def __init__(self, size):
        self.max_size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1 # condition for empty queue
    
    def __str__(self):
        if self.isEmpty():
            return "Circular Queue is Empty!"
        elif self.rear >= self.front:
            return ' '.join([str(self.queue[i]) for i in range(self.front, self.rear + 1)])
        else:
            return ' '.join([str(self.queue[i]) for i in range(self.front, self.max_size)]) + ' ' + ' '.join([str(self.queue[i]) for i in range(0, self.rear + 1)])

    def enqueue(self, value):
        if self.isFull():
            return -1
        elif self.isEmpty():
        # queue is empty, insert first item
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = value
        else: # insert at rear
            self.rear = (self.rear + 1) % self.max_size
            self.queue[self.rear] = value
        return 1 # success

    def dequeue(self):
        if self.isEmpty():
            return None

        result = self.queue[self.front]
        if self.front == self.rear: # there's only one item
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        return result
        
    def isEmpty(self):
        return self.front == -1
    
    def isFull(self):
        return (self.rear + 1) % self.max_size == self.front

