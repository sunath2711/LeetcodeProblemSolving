#Given an array nums of integers, return how many of them contain an even number of digits.
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_even = 0
        for i in nums:
            count = 0
            while i!= 0:
                i = i // 10
                count += 1
            if count % 2 == 0:
                total_even += 1
        return total_even        
        
