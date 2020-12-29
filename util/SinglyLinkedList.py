"""
Singly Linked List
"""
class ListNode(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    
    def get_data(self):
        return self.data
        
    def get_next(self):
        return self.next_node
        
    def set_next(self, new_next):
        self.next_node = new_next

def makeList(array):
    head = ListNode(data=array[0])
    for i in array[1:]:
        ptr = head
        while ptr.next_node:
           ptr = ptr.next_node
        ptr.next_node = ListNode(data=i)
    return head

def get_array(list):
    content = []
    temp = list
    while temp:
        content.append(temp.data)
        temp = temp.next_node
    return content

def printList(list):
    content = ""
    temp = list
    while temp:
        content += str(temp.data)
        temp = temp.next_node
        if temp:
            content += "->"
    print(content)

class SinglyLinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = ListNode(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count
        
    def search(self, data):
        current = self.head
        found = False
        while current and found == False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found == False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
    

