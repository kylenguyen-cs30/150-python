# 49. Group Anagrams
# Solved
# Medium
#
# Topics
# Companies
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically
# using all the original letters exactly once.
#
#
#
# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
#
# Input: strs = [""]
# Output: [[""]]
# Example 3:
#
# Input: strs = ["a"]
# Output: [["a"]]
#
#
# Constraints:
#
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.


def groupAnagrams(strs):
    # Create a dictionary to hold the list of anagram
    anagrams = {}

    # Iterate through each string in the input list
    for s in strs:
        # sort the string and use sorted strings as a key
        key = "".join(sorted(s))
        # print(key)

        # if the key is not in the dictionary, create a new entry
        if key not in anagrams:
            anagrams[key] = []

        # append the original string to the correct list based on the sorted key
        anagrams[key].append(s)

    # Return the value of the dictionary, which are the grouped anagrams
    return list(anagrams.values())


def test(testNum, strs, expected):
    print(f"Test {testNum} start")

    result = groupAnagrams(strs)

    sorted_result = sorted([sorted(group) for group in result])
    sorted_expected = sorted([sorted(group) for group in expected])

    if sorted_result == sorted_expected:
        print(f"Test {testNum} passed")
    else:
        print(f"Test {testNum} fail")


test(
    1,
    ["eat", "tea", "tan", "ate", "nat", "bat"],
    [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]],
)

test(
    2,
    [""],
    [[""]],
)

test(
    3,
    ["a"],
    [["a"]],
)
