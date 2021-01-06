"""
HashTable Applications:
- write function to determine if a string contains repeated chars
- given a string of any length, find the most-used char
- determine if two strings are anagrams

Time Complexity:
Search - Average O(1), Amortized Worst O(n)
Insert - Average O(1), Amortized Worst O(n)
Delete - Average O(1), Amortized Worst O(n)

Space Complexity:
Average O(n)
Worst O(n)

Hash tables are (slightly) simpler to implement than search trees and have better average-case performance.
"""

# in a more complex implementation, the capacity is prime and it can be changed
INITIAL_CAPACITY = 50 # goot for simplicity, bad for scalability

class HashNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def __str__(self):
        return "[" + str(self.key) + " : " + str(self.value) + "]"
"""
Node has a next field bc it is part of a Linked List. Since the hashtable uses separate chaining, each bucket wil contain a linkedlist of nodes containing the objects stores at that index. It is a method of collision resolution.

If there are two keys with the same hash value, it is a collision. If we just wrote it to that index it would overwrite it. But with separate chaining, we have a LinkedList at each index of our buckets array, containing all keys for a given index. If we need to look for one ot those, we iterate over the linkedlist to find the Node matching the requested key.
There are more efficient ways of handling collisions but separate chaining is simple.
"""

class HashTable(object):
    def __init__(self):
        self.capacity = INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        string = ""
        for i in range(len(self.buckets)):
            node = self.buckets[i]
            if node is None:
                continue
            string += "[Bucket "+str(i)+"]"
            while node is not None:
                string += " --> "
                string += str(node)
                node = node.next
            string += "\n"
        return string

    """
    ord() - returns an integer representing the Unicode character.
    """
    def hash(self, key):
        hashsum = 0
        # loop thru all chars in the key
        for index, char in enumerate(key):
            # (index plus lenght of key)^(current char code)
            hashsum += (index + len(key)) ** ord(char)
            # modulus to maintain hashsum in the range of [0, self.capacity - 1]
            hashsum = hashsum % self.capacity
        return hashsum
    """
    1. increase self.size of hash table
    2. calculate index of key using hash()
    3. get bucket with index from self.buckets
    4. if bucket at index is empty, create a new node for that bucket
    5. else, there is a collision which means there is already a linkedlist node at that indes. Loop thru linked list and add node to the end.
    """
    def insert(self, key, value):
        self.size += 1 # 1
        index = self.hash(key) # 2
        node = self.buckets[index] # 3
        
        if node is None: # 4
            self.buckets[index] = HashNode(key, value)
        else: # 5
            prev_node = node
            while node is not None:
                prev_node = node
                node = node.next
            prev_node.next = HashNode(key, value)
    
    """
    1. calculate index for key provided using hash()
    2. go to bucket at index
    3. loop thru nodes in linked list until key is found, or until we reach the end of the linked list
    4. if found return value of hashnode, else return None
    """
    def find(self, key):
        index = self.hash(key) # 1
        node = self.buckets[index] # 2
        
        while node is not None and node.key != key: # 3
            node = node.next
        
        if node is not None: # 4
            return node.value
        else:
            return None

    """
    removing element from hashtable is like removing element from a linked list
    1. calculate index with hash() and get node at index
    2. loop thru linkedlist until end or until key is found
    3. if found remove node from linnked list and return node value
    4. else if not found return None
    """
    def remove(self, key):
        index = self.hash(key) # 1
        node = self.buckets[index]
        
        prev_node = None
        while node is not None and node.key != key: # 2
            prev_node = node
            node = node.next
        
        if node is not None: # key found
            self.size -= 1
            result = node.value
            
            # remove from linkedlist
            if prev_node is None:
               self.buckets[index] = node.next # none of the next match
            else: # delete by skipping over
                prev_node.next = prev_node.next.next
        
            return result
    
        else: # key not found
            return None

