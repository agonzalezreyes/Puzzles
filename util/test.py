from Testing import *

"""
Linked Lists
"""
from DoublyLinkedList import DoublyLinkedList
from CircularLinkedList import CircularLinkedList

clist = CircularLinkedList()
clist.print()
clist.add(4)
clist.print()
clist.add(10)
clist.print()
clist.add(2)
clist.add(5)
clist.print()
clist.remove(4)
clist.print()
clist.remove(2)
clist.print()
clist.add(11)
clist.add(15)
clist.print()
clist.remove(15)
clist.print()
clist.remove(5)
clist.print()
clist.remove(10)
clist.print()
clist.remove(11)
clist.print()
a = clist.get_array()
print(a)

newList = DoublyLinkedList()
newList.insert_front(1)
newList.insert_front(2)
newList.insert_end(10)
newList.print()
newList.remove(1)
newList.print()
newList.remove(10)
newList.print()
newList.remove(2)
a = newList.get_array()
print(a)


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
from Sorting import bubble_sort, insertion_sort, merge_sort, quicksort, timsort, selection_sort, heap_sort, tree_sort

tests = Testing("Sorting")
input = [8, 2, 6, 4, 5]
expected = [2, 4, 5, 6, 8]

tests.addTest(expected, bubble_sort, input, title="bubble_sort")
tests.addTest(expected, insertion_sort, input, title="insertion_sort")
tests.addTest(expected, merge_sort, input, title="merge_sort")
tests.addTest(expected, quicksort, input, title="quicksort")
tests.addTest(expected, selection_sort, input, title="selection_sort")
tests.addTest(expected, heap_sort, input, title="heap_sort")
# TODO: fix timsort
# TODO: tree_sort

tests.run()
