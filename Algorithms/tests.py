import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from util.Testing import Testing

"""
Search
"""
from Search import linear_search, binary_search, binary_search_iter

tests = Testing("Search")
arr = [23, 4, 5, 8, 19, 1]
elem = 5
expected = 2

tests.addTest(expected, linear_search, (arr, elem), title="linear_search")
tests.addTest(expected, binary_search, (arr, elem, 0, len(arr)), title="linear_search")
tests.addTest(expected, binary_search_iter, (arr, elem), title="linear_search")

tests.run()

"""
Sorting
"""
from Sorting import bubble_sort, insertion_sort, merge_sort, quicksort, timsort, selection_sort, heap_sort, tree_sort, radix_sort
import numpy as np
from copy import deepcopy


np.random.seed(0)
input = np.random.randint(999, size=25).tolist()
expected = np.sort(deepcopy(input)).tolist()

print(input)
print(expected)

#input = [8, 2, 6, 4, 5]
#expected = [2, 4, 5, 6, 8]

tests = Testing("Sorting")

tests.addTest(expected, bubble_sort, input, title="bubble_sort")
tests.addTest(expected, insertion_sort, input, title="insertion_sort")
tests.addTest(expected, merge_sort, input, title="merge_sort")
tests.addTest(expected, quicksort, input, title="quicksort")
tests.addTest(expected, selection_sort, input, title="selection_sort")
tests.addTest(expected, heap_sort, input, title="heap_sort")
tests.addTest(expected, radix_sort, input, title="radix_sort")
tests.addTest(expected, timsort, input, title="timsort")
# TODO: fix radix_sort
# TODO: implement tree_sort

tests.run()

