# Bubble Sort: the largest emelent in the list will "bubble up" towards its correct position at the end. Worst and average case time complexity is O(n^2) since it contains nested for-loops; best case (when already sorted) is O(n). Overall, it is a simple but slow algorithm.
def bubble_sort(array):
    length = len(array)
    
    for i in range(length):
    
        is_sorted = True
        
        for j in range(length-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                is_sorted = False

        if is_sorted:
            break

    return array

input = [8, 2, 6, 4, 5]
output = bubble_sort(input)
print(output)

# Insertion Sort: Builds the sorted array one element at a time by comparing each with the rest of the elements and isnerting into its correct position.
# Runtime complexity is O(n^2) for average case and worst case. Best case (when its already sorted) is O(n).
# Considered more efficient that bubble sort.
def insetion_sort(array):
    for index in range(1, len(array)):
        key = array[index]
        prev_index = index-1
        
        while prev_index >= 0 and key < array[prev_index]:
            array[prev_index+1] = array[prev_index]
            prev_index -= 1

        array[prev_index+1] = key

    return array

print(insetion_sort(input))

# Merge Sort: merge() is called for each half, and has linear runtime complexity O(n) by looking at each element at most once. Then, merge_sort(0 splits input array recursively and calls merge for each half; halved until a single element remains, the number of halving operations performed is log_2(n). Thus, the total runtime is O(nlog_2(n)) for worst-case.
# It is a very efficient algorithm that scale well as the size of the input array grows. But for small arrays, bubble sort and insertion sort are faster.
# helper function
def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    result = []
    left_index = 0
    right_index = 0
    
    while len(result) < len(left) + len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
        
        if right_index == len(right):
            result += left[left_index:]
            break
        if left_index == len(left):
            result += right[right_index:]
            break

    return result
    
def merge_sort(array):
    if len(array) < 2:
        return array
    middle = len(array) // 2
    return merge(left=merge_sort(array[:middle]), right=merge_sort(array[middle:]))

print(merge_sort(input))

# Quicksort: the input array is partitioned in linear time O(n), and this repeats recursively for an average of log_2(n) times. Hence the final time complexity is O(nlog_2(n)). Theoretically, the worst-case scenario is O(n^2), and there is no guarantee it will achieve the average runtime complexity. Further, it trades off memory space for speed.
from random import randint

def quicksort(array):
    if len(array) < 2:
        return array
    low, same, high = [], [], []
    pivot = array[randint(0, len(array)-1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item > pivot:
            high.append(item)
        elif item == pivot:
            same.append(item)
    return quicksort(low) + same + quicksort(high)

print(quicksort(input))

# Timsort: a combination of insertion sort and merge sort.
# On average, runtime complexity is of O(nlog_2(n)) just like merge sort and quicksort. The log comes from doubling down the size of the run to perform each linear merge.
# Best case scenario is O(n), better than merge sort and matches quicksort's best-case.
# For worst-case, it is O(nlog_2(n)) which surpases quicksort's O(n^2).
# Timsort performs O(nlog_2(n)) regardless of structure of the input array. Unlike quicksort which can run O(n^2). timsort is also very fast for small arrays since it turns into insertion sort.
def timsort_insertion(array, left=0, right=None):
    if right is None:
        right = len(array)-1
    for i in range(left+1, right+1):
        key = array[i]
        prev_i = i-1
        while j >= left and array[prev_i] > key:
            array[prev_i+1] = array[prev_i]
            j -= 1
        array[prev_i+1] = key
    return array

def timsort(array):
    min_run = 32
    n = len(array)
    
    for i in range(0, n, min_run):
        timsort_insertion(array, i, min((i+min_run-1), n-1))

    size = min_run
    while size < n:
        for start in range(0, n, size*2):
            middle = start+size-1
            end = min((start+size*2-1),(n-1))
            # merge subarrays
            merged = merge(left=array[start:middle+1], right=array[middle+1:end+1])
            # put back into original array
            array[start:start + len(merged)] = merged
        size *= 2
    return array

# Selection Sort: time complexity is O(n^2)
def selection_sort(array):
    for i in range(len(array)-1):
        min_i = i
        for j in range(i+1, len(array)-1):
            if array[j] < array[min_i]:
                min_i = j
        temp = array[i]
        array[i] = array[min_i]
        array[min_i] = temp
    return array

print(selection_sort(input))

# Heapsort: Has O(nlog(n)) for best/worst/average cases. Space complexity is O(1).
def heapify(array, length, i):
    # largest value
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    # if there is left child
    if left < length and array[i] < array[left]:
        largest = left
    # if there is right child
    if right < length and array[largest] < array[right]:
        largest = right
    # root
    if largest != i:
        # swap
        temp = array[i]
        array[i] = array[largest]
        array[largest] = temp
        # root
        heapify(array, length, largest)

def heap_sort(array):
    lenght = len(array)
    # max heap
    for i in range(lenght, -1, -1):
        heapify(array, lenght, i)
    # extract element
    for i in range(lenght-1, 0, -1):
        # swap
        temp = array[i]
        array[i] = array[0]
        array[0] = temp
        heapify(array, i, 0)
    return array

print(heap_sort(input))

# Tree Sort: Worst case time complexity is O(nlog(n)) using balanced binary search tree; O(n^2) using unbalanced binary search tree. Average and best time complexity is O(nlog(n)).
# Worst case space complexity: O(n)
class Node:
    def __init__(self, val):
        self.left_child = None
        self.right_child = None
        self.data = val

def tree_sort(array):
    pass
