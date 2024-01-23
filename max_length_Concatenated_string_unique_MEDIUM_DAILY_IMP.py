# You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

# Return the maximum possible length of s.
# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All the valid concatenations are:
# - ""
# - "un"
# - "iq"
# - "ue"
# - "uniq" ("un" + "iq")
# - "ique" ("iq" + "ue")
# Maximum length is 4.

class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        n = len(arr)
        out = [""]
        op = 0
        
        for word in arr:
            for i in out:
                newResult = i+word
                if len(newResult)!=len(set(newResult)): continue
                out.append(newResult)
                op = max(op, len(newResult))
        return op
