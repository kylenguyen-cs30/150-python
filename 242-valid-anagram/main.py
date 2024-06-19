# 242. Valid Anagram
# Solved
# Easy
# Topics
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
#
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
#
#
# Constraints:
#
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# 2 dictionaries comparison. method
# def isAnagram(s: str, t: str) -> bool:
#     # Step 1: Check if the lengths are the same
#     if len(s) != len(t):
#         return False
#
#     # Step 2: Create dictionaries to count the frequency of characters
#     freq_s = {}
#     freq_t = {}
#
#     for char in s:
#         if char in freq_s:
#             freq_s[char] += 1
#         else:
#             freq_s[char] = 1
#
#     for char in t:
#         if char in freq_t:
#             freq_t[char] += 1
#         else:
#             freq_t[char] = 1
#
#     # Step 3: Compare the two dictionaries
#     return freq_s == freq_t


# this solution has O(nlog(n)) time for
# sorting and O(n) for comparison
def isAnagram(s, t) -> bool:
    return sorted(s) == sorted(t)


def test(testNum, s, t, expected):
    print("Test", testNum, "start")
    if isAnagram(s, t) == expected:
        print("Test", testNum, "passed")
    else:
        print("Test", testNum, "fail")


test(1, "anagram", "nagaram", True)
test(2, "rat", "car", False)
