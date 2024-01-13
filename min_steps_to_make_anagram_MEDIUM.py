# ou are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

# Return the minimum number of steps to make t an anagram of s.

# An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

#  Example 2:

# Input: s = "leetcode", t = "practice"
# Output: 5
# Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
# Example 3:

# Input: s = "anagram", t = "mangaar"
# Output: 0
# Explanation: "anagram" and "mangaar" are anagrams.

class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        i = 0
        s1_dict = {}
        while i < len(s):
            if s[i] in s1_dict:
                s1_dict[s[i]] += 1
            else:
                s1_dict[s[i]] = 1
            i+=1
        count = 0
        for char in t:
            if s1_dict.get(char, 0) > 0:
                s1_dict[char] -= 1
            else:
                count+=1

        return sum(s1_dict.values()) 
