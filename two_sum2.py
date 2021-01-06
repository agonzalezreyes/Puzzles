"""
Two Sum Boolean Version
Given an array of integers nums and an integer target, return True or False depending whether there are two numbers such that they add up to target.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

"""
OPTION 1: Sort the array and use binary search.
Time complexity is O(n log n) because it takes O(n log n) time to sort the array using sort() and the cost of n binary searches is O(n log n).
The space compolexity depends on the sorting algorithm -- O(log n) for quicksort, and O(1) for heapsort.
"""
from Algorithms.Search import binary_search

def sumsToTarget_BS(nums, target):
    sorted = nums.copy()
    sorted.sort()
    for i in range(len(sorted)):
        delta = target - sorted[i]
        j = binary_search(sorted, delta, 0, len(sorted))
        if j >= 0:
            if (j != i) or (i > 0 and sorted[i-1] == sorted[i]) or (i < len(sorted)-1 and sorted[i+1] == sorted[i]):
                return True
    return False

"""
OPTION 2: Runtime complexity depends on the sorting algorithm -- standard sorting would be O(n log n); using radix sort the time would take O(n log U) where U is the largest element of the array.
The space complexity is O(log n) if using quicksort or radix sort, while O(1) for heapsort.
This solution is faster than sort & binary search function, and can be faster asymptotically if using radix sort.
"""
def sumsToTarget_inward(nums, target):
    nums.sort()
    left = 0
    right = len(nums)-1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return True
        elif sum < target:
            left = left + 1
        else:
            right = right - 1
    return False

# Checks:

from util import Testing as t

tests = t.Testing("Two Sum - Boolean")

nums = [2,7,11,15]
target = 9
answer = True #[0,1]
params = (nums, target)
tests.addTest(answer, sumsToTarget_BS, params)
tests.addTest(answer, sumsToTarget_inward, params)

nums = [3,2,4]
target = 6
answer = True # [1,2]
tests.addTest(answer, sumsToTarget_BS, (nums, target))
tests.addTest(answer, sumsToTarget_inward, (nums, target))

nums = [3,3]
target = 6
answer = True # [0,1]
tests.addTest(answer, sumsToTarget_BS, (nums, target))
tests.addTest(answer, sumsToTarget_inward, (nums, target))

nums = [3]
target = 6
answer = False # No Solution
tests.addTest(answer, sumsToTarget_BS, (nums, target))
tests.addTest(answer, sumsToTarget_inward, (nums, target))

tests.run()
