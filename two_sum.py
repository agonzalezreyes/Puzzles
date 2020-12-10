# Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

#Example 1:
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#
#Example 2:
#Input: nums = [3,2,4], target = 6
#Output: [1,2]
#
#Example 3:
#Input: nums = [3,3], target = 6
#Output: [0,1]
#
#Constraints:
#2 <= nums.length <= 103
#-109 <= nums[i] <= 109
#-109 <= target <= 109
#Only one valid answer exists.

# OPTION 1: try all the pairs in the array and see if any of them add up to the target number. trying all possible pairs is O(n^2) in the worst-case scenario. But since there is no structures used, space complexity is O(1). It is a correct solution but not good because there are better solutions.
def sumsToTarget1(nums, target):
    solution = []
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            sum = nums[i] + nums[j]
            if sum == target:
                solution.append(i)
                solution.append(j)
                break
    return solution

# OPTION 2: create a hash set of all the elements in the nums array in order to scan over the array and check for each element nums[i] if there is another element nums[j] in such that nums[j] = target - nums[i].
# Make sure to handle the case where there are duplicated elements in nums array and not to pait an element with itself.
# Solution time complexity is O(n) since there are n insertions and n lookups of the hash set.
# Space complezity is O(n) with the creation of the hash set.
# Considered "good" solution.
def sumsToTarget2(nums, target):
    values_dict = dict()
    for index, curr in enumerate(nums):
        delta = target - curr
        if delta in values_dict:
            i = values_dict[delta]
            return [i, index]
        values_dict[curr] = index
    return []


from util import Testing as t

tests = t.Testing("Two Sum to Target")

nums = [2,7,11,15]
target = 9
answer = [0,1]
tests.addTest(answer, sumsToTarget1, (nums, target))
tests.addTest(answer, sumsToTarget2, (nums, target))

nums = [3,2,4]
target = 6
answer = [1,2]
tests.addTest(answer, sumsToTarget1, (nums, target))
tests.addTest(answer, sumsToTarget2, (nums, target))

nums = [3,3]
target = 6
answer = [0,1]
tests.addTest(answer, sumsToTarget1, (nums, target))
tests.addTest(answer, sumsToTarget2, (nums, target))

tests.run()
