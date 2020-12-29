"""
Doubly Linked List
"""

class DoublyNode(object):
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        if self.head is None:
            self.head = DoublyNode(data)
        else:
            node = DoublyNode(data)
            self.head.previous = node
            node.next = self.head
            self.head = node

    def insert_end(self, data):
        node = DoublyNode(data)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = node
        node.previous = curr
    
    def remove(self, data):
        curr = self.head
        if curr is None:
            return
        if curr.next is not None:
        # there are at least two items in list
            if curr.data == data: # remove head
                curr.next.previous = None
                self.head = curr.next
                curr.next = None
                return
            else:
                while curr.next is not None:
                    if curr.data == data:
                        break
                    curr = curr.next
                if curr.next:
                    curr.previous.next = curr.next
                    curr.next.previous = curr.previous
                    curr.next = None
                    curr.previous = None
                else:
                    curr.previous.next = None
                    curr.previous = None
                return
        else: # item to be removed is the only item in list
            self.head = None
            curr = None

    def print(self):
        curr = self.head
        while curr is not None:
            print(str(curr.data), end=' ')
            curr = curr.next
        print()
        
    def get_array(self):
        arr = []
        curr = self.head
        if curr is not None:
            while curr:
                arr.append(curr.data)
                curr = curr.next
        return arr
