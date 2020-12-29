"""
Recursive Binary Search
"""
def binary_search(array, element, start=0, end=0):
    if start > end:
        return -1
    
    middle = (start + end) // 2
    
    if element == array[middle]:
        return middle
        
    if element < array[middle]:
        return binary_search(array, element, start, middle-1)
    else:
        return binary_search(array, element, middle+1, end)

"""
Iterative Binary Search
"""
def binary_search_iter(array, element):
    lhs = 0
    rhs = len(array)-1
    for i, val in enumerate(array):
        if (lhs > rhs):
            return -1
        else:
            middle = (lhs + rhs) // 2
            if array[middle] < element:
                lhs = middle+1
            if array[middle] > element:
                rhs = middle-1
            if array[middle] == element:
                return middle
    return None
    
"""
Regular Linear Search
"""
def linear_search(array, target):
    for i, val in enumerate(array):
        if val == target:
            return i
    return -1


