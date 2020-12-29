"""
Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = 2->4->3 and l2 = 5->6->4
Output: 7->0->8
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
* The number of nodes in each linked list is in the range [1, 100].
* 0 <= Node.val <= 9
* It is guaranteed that the list represents a number that does not have leading zeros.
"""

# class ListNode(object):
#     def __init__(self, data=None, next_node=Node):
#         self.data = data
#         self.next_node = next_node

from util.SinglyLinkedList import ListNode, makeList, printList, get_array

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    head = None
    curr = None
    carry = 0
    
    while l1 or l2:
        data1 = 0 if l1 is None else l1.data
        data2 = 0 if l2 is None else l2.data

        sum = data1 + data2 + carry
        new_node = ListNode(data=sum % 10)
        carry = sum // 10

        # if first node
        if curr is None:
            head = new_node
            curr = new_node
        else: # if not first node
            curr.next_node = new_node
            curr = curr.next_node

        # move to next nodes for each list
        if l1 is not None:
            l1 = l1.next_node
        if l2 is not None:
            l2 = l2.next_node

    # create ListNode if carry has a left over
    if carry:
        curr.next_node = ListNode(carry)

    return head


from util import Testing as t

tests = t.Testing("Add Two Linked Lists")

l1 = [2, 4, 3]
l2 = [5, 6, 4]
out = [7, 0, 8]
list1 = makeList(l1)
list2 = makeList(l2)
result = addTwoNumbers(list1, list2)
tests.addTest(out, get_array, result)

l1 = [0]
l2 = [0]
out = [0]
list1 = makeList(l1)
list2 = makeList(l2)
result = addTwoNumbers(list1, list2)
tests.addTest(out, get_array, result)

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
out = [8,9,9,9,0,0,0,1]
list1 = makeList(l1)
list2 = makeList(l2)
result = addTwoNumbers(list1, list2)
tests.addTest(out, get_array, result)

tests.run()
