import ctypes
"""
Dynamic Array

Similar to Python list
"""

class DynamicArray(object):
    def __init__(self):
        self.n = 0 # actual elements count
        self.capacity = 1 # default capacity
        self.A = self.make_array(self.capacity)
    
    def __len__(self):
        return self.n
    
    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError('Index is out of bounds!')
        return self.A[k]
    
    def __str__(self):
        string = "["
        for k in range(self.n):
            string += str(self.A[k])
            if k != self.n - 1:
                string += ", "
        string += "]"
        return string
    
    def append(self, element):
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        self.A[self.n] = element
        self.n += 1
    
    def insertAt(self, item, index):
        if index < 0 or index > self.n:
            raise IndexError('insertAt(): Enter a valid index.')
            return
            
        if self.n == self.capacity:
            self._resize(2*self.capacity)
            
        for i in range(self.n-1, index-1, -1):
            self.A[i+1] = self.A[i]
            
        self.A[index] = item
        self.n += 1
    
    """
    Deletes item from end of array
    """
    def delete(self):
        if self.n == 0:
            raise IndexError('delete(): Array is empty, deletion not possible')
            return
        
        self.A[self.n-1] = 0
        self.n -= 1

    """
    Deletes item at index given
    """
    def removeAt(self, index):
        if self.n == 0:
            raise IndexError('removeAt(): array is empty, removal not possible')
            return
        if index < 0 or index >= self.n:
            raise IndexError('removeAt(): Index out of bounds!')
            return
        
        if index == self.n - 1:
            self.A[index] = 0
            self.n -= 1
            return
        
        for i in range(index, self.n-1):
            self.A[i] = self.A[i+1]
        
        self.A[self.n-1] = 0
        self.n -= 1

    """
    Resize internal array to capacity given
    """
    def _resize(self, capacity):
        new_A = self.make_array(capacity)
        for k in range(self.n):
            new_A[k] = self.A[k]
        self.A = new_A
        self.capacity = capacity
    
    """
    Returns new array with new capacity
    """
    def make_array(self, capacity):
        return (capacity * ctypes.py_object)()
    

