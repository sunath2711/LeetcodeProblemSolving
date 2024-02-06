# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

from collections import Counter
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_group = {}
        for word in strs:
            key = ''.join(sorted(word))

            if key in anagram_group:
                anagram_group[key].append(word)
            else:
                anagram_group[key] =[word]
        return list(anagram_group.values())

        


