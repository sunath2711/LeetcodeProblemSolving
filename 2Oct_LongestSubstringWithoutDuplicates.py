class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right = 0,0
        myset = set()
        max_length = 0

        for right in range(len(s)):

            while s[right] in myset:
                myset.remove(s[left])
                left+=1
            myset.add(s[right])
            max_length=max(max_length, right-left+1)

        return max_length
