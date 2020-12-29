# TODO: Circular Linked List

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class CircularLinkedList(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head
    
    def add(self, data):
        new_node = Node(data)
        if self.head.data is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
    
    def remove(self, data):
        curr = self.head
        if curr.data is not None:
            if curr.data == data: # node is head
                if curr.next and curr.next.next != self.head:
                    # more two in list
                    self.head = curr.next
                    self.tail.next = self.head
                    curr = None
                else: # two or less than two items in list
                    if curr.data == curr.next.data:
                        self.head = Node(None)
                        self.tail = Node(None)
                        self.head.next = self.tail
                        self.tail.next = self.head
                        return
                    self.head = curr.next
                    self.tail = self.head
                    self.head.next = self.head
                    self.tail.next = self.head
                    curr = None
            else: # node in middle or end
                while curr and curr.next is not self.head:
                    prev = curr
                    curr = curr.next
                    if curr.data == data:
                        prev.next = curr.next
                        curr = None

    def print(self):
        curr = self.head
        if self.head.data is None:
            print("Empty Circular Linked List!")
            return
        else:
            print(str(curr.data), end=' ')
            while curr.next != self.head:
                curr = curr.next
                print(str(curr.data), end=' ')
            print()
    
    def get_array(self):
        arr = []
        curr = self.head
        if curr.data is not None:
            arr.append(curr.data)
            while curr.next != self.head:
                curr = curr.next
                arr.append(curr.data)
        return arr

