class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        max_val = max(c.values())
        max_key = [key for key, value in c.items() if value == max_val][0]

        return max_key
        
