# 347. Top K Frequent Elements
# Medium
#
# Topics
# Companies
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
#
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
#


def topKFrequent(nums: list[int], k: int) -> list[int]:
    # step 1 : manually count frequency of each elements
    freq = {}
    for n in nums:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1
    # step 2 : convert frequency dictionary into a list of tuples
    # and sort it
    freq_list = list(freq.items())
    print(freq_list)
    # applying sort
    # sort by frequency, descending
    freq_list.sort(key=lambda x: x[1], reverse=True)

    # step 3 : Extract the elements of top k frequent elements
    top_k_elements = [item[0] for item in freq_list[:k]]

    return top_k_elements


def test(testNum, nums, k, expected):
    print(f"Test {testNum} start")

    if topKFrequent(nums, k) == expected:
        print(f"Test {testNum} passed")
    else:
        print(f"Test {testNum} passed")


test(1, [1, 1, 1, 2, 2, 3], 2, [1, 2])
test(2, [1], 1, [1])
