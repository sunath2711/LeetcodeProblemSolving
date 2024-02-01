# Input: nums = [1,3,4,8,7,9,3,5,1], k = 2
# Output: [[1,1,3],[3,4,5],[7,8,9]]
# Explanation: We can divide the array into the following arrays: [1,1,3], [3,4,5] and [7,8,9].
# The difference between any two elements in each array is less than or equal to 2.
# Note that the order of elements is not important.
class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(0,len(nums),3):
            if nums[i+2] - nums[i] > k:
                return []
            result.append(nums[i:i+3]) 


        return result        
        
