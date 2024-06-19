# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


# Constraints:

# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109


def merge(nums1, m, nums2, n):
    # newNums = []

    index1 = m - 1
    index2 = n - 1
    index = (m + n) - 1

    while index1 >= 0 and index2 >= 0:
        # check if nums1 is bigger than nums2
        if nums1[index1] > nums2[index2]:
            nums1[index] = nums1[index1]
            index1 -= 1
        else:
            nums1[index] = nums2[index2]
            index2 -= 1

        index -= 1

    # if there are any elements left in nums2
    while index2 >= 0:
        nums1[index] = nums2[index2]
        index -= 1
        index2 -= 1

    print(",".join(map(str, nums1)))
    print(",".join(map(str, nums2)))


def test(testNum, nums1, m, nums2, n, expected):
    print("Test", testNum, "start")
    merge(nums1, m, nums2, n)

    # check the result
    for index in range(len(nums1)):
        if nums1[index] != expected[index]:
            print("Test", testNum, "failed")
            return

    print("Test ", testNum, " passed")


test(1, [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6])
test(2, [1], 1, [], 0, [1])
test(3, [0], 0, [1], 1, [1])
