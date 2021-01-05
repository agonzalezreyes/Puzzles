"""
Note on Time Complexity:

When dividing an array of length n in two, the total number of divisions before reaching a one element array is log2(n).
This is often simplified because the logarithms of different bases are effectively equivalent when discussing algorithm analysis.

In Big-O complexity analysis, it doesn't actually matter what the logarithm base is. (they are asymptotically the same, i.e. they differ by only a constant factor):
    O(log_2 N) = O(log_{10} N) = O(log_e N)
Most of the time when mathematicians talk about logs, they implicitly mean to base e. Computer Scientists would tend to favour base 2, but it doesn't actually matter.

Source: https://stackoverflow.com/questions/6701809/base-of-logarithms-in-time-complexity-algorithms
"""


# ---- BASIC: Selection sort, Bubble sort, and Insertion sort ---- #

"""
Selection Sort:

Time complexity:
- Worst/Average/Best: O(n^2)

Has no actual applications because O(n^2).
"""
def selection_sort(array):
    for i in range(len(array)):
        min_i = i
        for j in range(i+1, len(array)):
            if array[min_i] > array[j]:
                min_i = j
        array[i], array[min_i] = array[min_i], array[i]
    return array

"""
Bubble Sort: the largest element in the list will "bubble up" towards its correct position at the end.

Time complexity:
- Worst and Average case are O(n^2) since it contains nested for-loops.
- Best case (when already sorted) is O(n).

Overall, it is a simple but slow algorithm.
Only advantage over insertion sort is that it is a little bit easier to implement.
"""
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

"""
Insertion Sort: Builds the sorted array one element at a time by comparing each with the rest of the elements and inserting into its correct position.

Time Complexity:
- Average and Worst case are O(n^2)
- Best case (when its already sorted) is O(n).

Considered more efficient that bubble sort.
More efficient when N is small, about < 30.
"""
def insertion_sort(array):
    for index in range(1, len(array)):
        key = array[index]
        prev_index = index-1
        
        while prev_index >= 0 and key < array[prev_index]:
            array[prev_index+1] = array[prev_index]
            prev_index -= 1

        array[prev_index+1] = key

    return array

# ---- STANDARD: Mergesort, Quicksort ---- #

"""
Merge Sort: merge() is called for each half, and has linear runtime complexity O(n) by looking at each element at most once. Then, merge_sort() splits input array recursively and calls merge for each half; halved until a single element remains, the number of halving operations performed is log_2(n). Thus, the total runtime is O(n*log_2(n)) for worst-case.

Time Complexity:
- Worst/Average/Best: O(n*log_2(n))
Space Complexity:
- Requires O(n) space

Allocation and de-allocation of extra space used in merge sort increases the running time.
It is a very efficient algorithm that scale well as the size of the input array grows.
But for small arrays, bubble sort and insertion sort are faster.

Mergesort preferred over Quicksort for Linked Lists because:
- Linked List nodes may not be adjacent in memory, plus we can isert items in themiddle in O(1) extra space and O(1) time. Hence, merge operation of merge sort can be implemented wihtout extra space for linked lists.
- We cannot do random access in linked lists, and Quicksort requires a lot of this type of access. For linked lists, we have to travel each node to reach the node we are looking for since we do not have a continuous memory block. Thus, the cost increases for quicksort. On the other hand, mergesort accesses data sequentially and the need of random access is low.
"""
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

"""
Quicksort: the input array is partitioned in linear time O(n), and this repeats recursively for an average of log_2(n) times. Hence the final time complexity is O(n*log_2(n)).
Theoretically, the worst-case scenario is O(n^2), and there is no guarantee it will achieve the average runtime complexity. Further, it trades off memory space for speed.

Time Complexity:
- Worst case: O(n^2)
- Average and Best case: O(n*log_2(n))

Quicksort is preferrred over Mergesort for sorting arrays because:
- Quicksort is in-place while mergesort requires O(n) space
- Allocation and de-allocation of extra space used in merge sort increases the running time.
- Both quicsort and mergesort have average case of O(n*log_2(n)) but mergesort loses due to space complexity of O(n).
- Quicksort is cache-friendly since it has good locality of reference when used for arrays.
- When Quicksort is tail recursive, tail call optimization is done.
"""
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

# ---- VARIOUS ---- #

"""
Heapsort

Time Complexity:
- For _heapify() it is O(log(n))
- For heap_sort() it is O(n)
- Hence, overall Best/worst/average cases: O(nlog(n))

Space complexity is O(1).

Applications:
- Sort a nearly sorter, or K sorted, array
- k largest or samllest elements in an array

Heapsort has limited uses because Quicksort and Mergesort are better in practive.
"""
def _heapify(array, length, i):
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
        array[i], array[largest] = array[largest], array[i]
        # root
        _heapify(array, length, largest)

def heap_sort(array):
    lenght = len(array)
    # max heap
    for i in range(lenght, -1, -1):
        _heapify(array, lenght, i)
    # extract element
    for i in range(lenght-1, 0, -1):
        # swap
        array[i], array[0] = array[0], array[i]
        _heapify(array, i, 0)
    return array

"""
Timsort: A combination of insertion sort and merge sort.
On average, runtime complexity is of O(nlog_2(n)) just like merge sort and quicksort. The log comes from doubling down the size of the run to perform each linear merge.
Best case scenario is O(n), better than merge sort and matches quicksort's best-case.
For worst-case, it is O(nlog_2(n)) which surpases quicksort's O(n^2).
Timsort performs O(nlog_2(n)) regardless of structure of the input array. Unlike quicksort which can run O(n^2). timsort is also very fast for small arrays since it turns into insertion sort.

Time Complexity:
- Worst complexity: n*log(n)
- Average complexity: n*log(n)
- Best complexity: n

Space complexity: n
"""
def timsort_insertion(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    for index in range(left+1, right+1):
        element = array[index] # element we want to position correctly
        prev_i = index - 1
        while prev_i >= left and array[prev_i] > element:
            array[prev_i+1] = array[prev_i]
            prev_i -= 1
        array[prev_i+1] = element
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

"""
Radix Sort: A non-comparative sorting algorithm. It avoids comparison by creating and distributing elements into buckets according to their radix.

Sorting technique that sorts the elements by:
(1) grouping the individual digits of the same place value; and (2) sorting the elements according to their increasing/decreasing order.

Time Complexity:

Because radix sort is not comparison based, it is not bounded by O(nlogn) running time — in fact, radix sort can perform in linear time.

Worst-case performance: O(w*n), where w is the number of bits required to store each key.
Worst-case space complexity: O(w+n)

Radix sort will operate on n d-digit numbers where each digit can be one of at most b different values (since b is the base being used). For example, in base 10, a digit can be 0,1,2,3,4,5,6,7,8,or 9.

Radix sort uses counting sort on each digit. Each pass over n d-digit numbers will take O(n+b) time, and there are d passes total. Therefore, the total running time of radix sort is O(d(n+b)). When d is a constant and b isn't much larger than n (in other words, b=O(n)), then radix sort takes linear time.

Source: https://brilliant.org/wiki/radix-sort/
"""
import math
# counting_sort time complexity: O(n+k)
def counting_sort(A, digit, radix):
    output = [0] * len(A)
    C = [0] * int(radix)
    
    for i in range(0, len(A)):
        ith_digit = int(A[i]/radix**digit)%radix
        C[ith_digit] = C[ith_digit] + 1
        # array C is not the val of the # of elments in A that equal to i
    # change array C to get commulative # of digits up to index in C
    for i in range(1, radix):
        C[i] = C[i] + C[i-1]
        # now C has the number of elements <= i
    
    for i in range(len(A)-1, -1, -1): # reverse traversal
        ith_digit = int(A[i]/radix**digit)%radix
        C[ith_digit] = C[ith_digit] - 1
        output[C[ith_digit]] = A[i]

    return output

def radix_sort(A, radix=10):
    largest = max(A)
    output = A
    digits = int(math.floor(math.log(largest, radix)+1))
    for i in range(digits):
        output = counting_sort(output, i, radix)
    return output

"""
Tree Sort: Worst case time complexity is O(nlog(n)) using balanced binary search tree; O(n^2) using unbalanced binary search tree. Average and best time complexity is O(nlog(n)).
Worst case space complexity: O(n)
"""
class Node:
    def __init__(self, val):
        self.left_child = None
        self.right_child = None
        self.data = val

# TODO: implement tree_sort
def tree_sort(array):
    pass
