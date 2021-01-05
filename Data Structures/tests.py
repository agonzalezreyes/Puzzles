
"""
Linked Lists
"""

from DoublyLinkedList import DoublyLinkedList
from CircularLinkedList import CircularLinkedList

clist = CircularLinkedList()
print(clist)
clist.add(4)
print(clist)
clist.add(10)
print(clist)
clist.add(2)
clist.add(5)
print(clist)
a = clist.get_array()
print(a)

newList = DoublyLinkedList()
print(newList)
newList.insert_front(1)
newList.insert_front(2)
newList.insert_end(10)
print(newList)
newList.remove(1)
print(newList)
newList.remove(10)
print(newList)
newList.remove(2)
a = newList.get_array()
print(a)

"""
Queues
"""
from Queue import Queue
from PriorityQueue import PriorityQueue
from CircularQueue import CircularQueue
from Deque import Deque

# ----- Standard Queue ----- #
q = Queue()
q.enqueue(110)
assert(q.queue[q.rear] == 110)
assert(q.queue[q.front] == 110)
assert(q.dequeue() == 110)
assert(q.getSize() == 0)
assert(q.dequeue() == None)

size = 10
for i in range(size):
    q.enqueue(i)

assert(size == q.getSize())
assert(q.queue[q.rear] == 9)

# ----- Priority ----- #
p = PriorityQueue()
p.insert(1, 1)
#print("Insert val=1 priority=1:")
assert(p.peek() == 1)
p.insert(2, 1)
#print("Insert val=2 priority=1:")
assert(p.peek() == 1)
p.insert(3, 2)
#print("Insert val=3 priority=2:")
assert(p.peek() == 3)
p.insert(4, 1)
#print("Insert val=4 priority=1:")
assert(p.peek() == 3)
assert(p.pop() == 3)
assert(p.pop() == 1)
assert(p.pop() == 2)
assert(p.pop() == 4)
assert(p.peek() is None)
p.insert(10, 10)
assert(p.peek() == 10)
#print(p)
assert(p.pop() == 10)
#print(p)

# ----- Circular ----- #
cq = CircularQueue(5)
assert(cq.enqueue(14) != -1) # successful enqueue
assert(cq.enqueue(22) != -1) # successful enqueue
assert(cq.enqueue(13) != -1) # successful enqueue
assert(cq.enqueue(16) != -1) # successful enqueue
assert(cq.enqueue(25) != -1) # successful enqueue
assert(cq.enqueue(100) == -1) # cq is full!
#print('Queue:' + str(cq))
assert(cq.dequeue() == 14)
assert(cq.dequeue() == 22)
#print('Queue:' + str(cq))
assert(cq.enqueue(9) != -1) # successful enqueue
assert(cq.enqueue(20) != -1) # successful enqueue
assert(cq.isFull() == True)
assert(cq.enqueue(5) == -1) # failed enqueue, cq is full!
assert(cq.enqueue(5) == -1) # failed enqueue, cq is full!
#print('Queue:' + str(cq))
assert(cq.dequeue() == 13)
assert(cq.dequeue() == 16)
assert(cq.dequeue() == 25)
assert(cq.dequeue() == 9)
assert(cq.dequeue() == 20)
assert(cq.isFull() == False)
assert(cq.isEmpty() == True)

# ----- Deque ----- #
d = Deque(4)
assert(d.insertFront(1) == 1) # successful insertion
assert(d.insertRear(5) == 1) # successful insertion
assert(d.insertRear(3) == 1) # successful insertion
assert(d.insertRear(10) == 1) # successful insertion
assert(d.insertFront(20) == -1) # failed insertion, full Deque
assert(d.removeRear() == 10)
assert(d.removeFront() == 1)
assert(d.removeFront() == 5)
assert(d.removeFront() == 3)
assert(d.insertFront(3) == 1)
assert(d.removeRear() == 3)
assert(d.isEmpty() == True)
assert(d.isFull() == False)


"""
Stack implementation with a list
"""
from Stack import Stack

s = Stack()
assert(s.isEmpty() == True)
s.push(4)
s.push('dog')
assert(s.peek() == 'dog')
s.push(True)
print(s)
assert(len(s) == 3)
assert(s.isEmpty() == False)
s.push(8.4)
print(s)
assert(s.pop() == 8.4)
assert(s.pop() == True)
print(s)
assert(len(s) == 2)
assert(s.pop() == 'dog')
assert(s.pop() == 4)
assert(len(s) == 0)
print(s)


"""
HashTable
"""
from HashTable import HashTable

hashTable = HashTable()
item = "hello"
hashTable.insert("key1", item)
hashTable.insert("key2", "123")
hashTable.insert("key2", 2021)
print(hashTable)

import unittest

class HashTableTests(unittest.TestCase):

    def setUp(self):
        self.hashTable = HashTable()

    def test_hash(self):
        self.assertEqual(self.hashTable.hash("hola"), self.hashTable.hash("hola"))
        self.assertTrue(self.hashTable.hash("hola") < self.hashTable.capacity)
        
    def test_insert(self):
        self.assertEqual(len(self.hashTable), 0)
        self.hashTable.insert("test_key", "test_val")
        self.assertEqual(self.hashTable.size, 1)
        self.assertEqual(self.hashTable.buckets[self.hashTable.hash("test_key")].value, "test_val")
    
    def test_find(self):
        self.assertEqual(len(self.hashTable), 0)
        item = "hello"
        self.hashTable.insert("key1", item)
        self.assertEqual(item, self.hashTable.find("key1"))
        items = ["list", "in", "an", "array"]
        self.hashTable.insert("key2", items)
        self.assertEqual(items, self.hashTable.find("key2"))
    
    def test_remove(self):
        self.assertEqual(self.hashTable.size, 0)
        item = "item to test"
        self.hashTable.insert("key1", item)
        self.assertEqual(1, len(self.hashTable))
        self.assertEqual(item, self.hashTable.remove("key1"))
        self.assertEqual(0, len(self.hashTable))
        self.assertEqual(None, self.hashTable.remove("undefined"))
        
    def test_capacity(self):
        CAP = 1000
        for i in range(0, CAP):
            self.assertEqual(i, len(self.hashTable))
            self.hashTable.insert("key"+str(i), "value"+str(i))
        self.assertEqual(len(self.hashTable), CAP)
        for i in range(0, CAP):
            self.assertEqual(CAP-i, len(self.hashTable))
            self.assertEqual(self.hashTable.find("key"+str(i)), self.hashTable.remove("key"+str(i)))
    
    def test_extra(self):
        self.assertEqual(len(self.hashTable), 0)
        self.hashTable.insert('abc', 20)
        self.assertEqual(len(self.hashTable), 1)
        self.hashTable.insert('fgh', 35)
        self.assertEqual(len(self.hashTable), 2)
        self.hashTable.insert('you', 'tube')
        self.assertEqual(len(self.hashTable), 3)
        
        self.assertEqual(20, self.hashTable.remove('abc'))
        self.assertEqual(len(self.hashTable), 2)
        # removing previously removed item should give None
        self.assertEqual(None, self.hashTable.remove('abc'))
        self.assertEqual(len(self.hashTable), 2)

unittest.main()

