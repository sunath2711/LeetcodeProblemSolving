# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# Input: s = "leetcode"
# Output: 0
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        for index,char in enumerate(s):
            if char in count:
                count[char]['count'] += 1
            else:
                count[char] = {'count': 1, 'first_index': index}
        
        unique_chars = [char for char, info in count.items() if info['count'] == 1]
        print(unique_chars)

        if not unique_chars:
            return -1
        else:
            return min(count[char]['first_index'] for char in unique_chars)






        
