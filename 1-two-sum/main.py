# Two Integer Sum
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
#
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
#
# Return the answer with the smaller index first.
#
# Example 1:
#
# Input:
# nums = [3,4,5,6], target = 7
#
# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].
#
# Example 2:
#
# Input: nums = [4,5,6], target = 10
#
# Output: [0,2]
# Example 3:
#
# Input: nums = [5,5], target = 10
#
# Output: [0,1]
# Constraints:
#
# 2 <= nums.length <= 1000
# -10,000,000 <= nums[i] <= 10,000,000
# -10,000,000 <= target <= 10,000,000


def twoSum(nums: list[int], target: int):
    hashTable = {}
    for index in range(len(nums)):
        found = target - nums[index]
        if found in hashTable:
            return [hashTable[found], index]
        else:
            hashTable[nums[index]] = index
    # return empty list if there are no found pair
    return []


def test(testNum, nums, target, expected):
    print(f"Test {testNum} start")

    result = twoSum(nums, target)
    if twoSum(nums, target) == expected:
        print(f"Test {testNum} passed")
    else:
        print(f"Test {testNum} fail")


test(1, [3, 4, 5, 6], 7, [0, 1])
test(2, [4, 5, 6], 10, [0, 2])
