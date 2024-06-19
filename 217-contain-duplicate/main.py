# 217. Contains Duplicate
# Solved
# Easy
# Topics
# Companies
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:
#
# Input: nums = [1,2,3,4]
# Output: false
# Example 3:
#
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true


def containDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    print(seen)
    return False


def test(testNum, nums, expected):
    print("Test", testNum, "start")

    if containDuplicate(nums) is not expected:
        print("Test", testNum, "fail")
        return

    print("Test", testNum, "passed")


test(1, [1, 2, 3, 1], True)
test(2, [1, 2, 3, 4], False)
test(3, [1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)
